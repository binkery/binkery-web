# Android LruCache 源码分析
- 2016-05-25 14:23:48
- Android
- android,lrucache,

<!--markdown--># LruCache 源码简单分析

前几天在公司组内做分享，本来想分享以下 Android 三级缓存的设计思路的，想画一个流程图分享一下，不过后来发现画一个流程图的工作量也不小啊～～，后来就改成了分享以下 LruCache 的分析了。

LruCache 位于 android.util 包下，属于 SDK 自动的工具类。Lru 的英文为 Least recently used，近期最少使用算法。设计的思路大致是这样的，在一个特定的缓存大小限制下，最近被使用的内容，很可能在未来再次被使用，而越长时间没被使用的内容，被使用的概率越底，基于这样的思路，最近被使用的内容被放在缓存的头部，这样减少了下次使用的查找时间，很长时间不被使用的内容被放在缓存的尾部，甚至在缓存超出预设的大小的时候，把尾部的内容从缓存中清楚掉。

## Fields 

android.util.LruCache 的代码很简洁，其重要的属性有下面三个。整个类的设计都是围绕着这三个变量来进行的。

* LinkedHashMap map
* int maxSize
* int size

LinkedHashMap 是这个类的核心，LinkedHashMap 是 HashMap 的子类，从名字上就可以看出，它首先是一个 HashMap，然后是一个 Linked 的 HashMap，Linked 的设计，也让它更加适合 LruCache 的实现。被 get() 的实例会被放到链表的开头。

## Methods

get() 和 put() 方法是咱们使用 LruCache 最经常用的方法，remove() 咱们直接使用的就比较少了。trimToSize() 是 LruCache 管理缓存内容的核心了，配合 size 和 maxSize 这两个变量，维护这这个缓存的大小。

### get()


    /**
     * Returns the value for {@code key} if it exists in the cache or can be
     * created by {@code #create}. If a value was returned, it is moved to the
     * head of the queue. This returns null if a value is not cached and cannot
     * be created.
     */
    public final V get(K key) {
        if (key == null) {
            throw new NullPointerException("key == null");
        }

        V mapValue;
        synchronized (this) {
            mapValue = map.get(key);
            if (mapValue != null) {
                hitCount++;
                return mapValue;
            }
            missCount++;
        }

        /*
         * Attempt to create a value. This may take a long time, and the map
         * may be different when create() returns. If a conflicting value was
         * added to the map while create() was working, we leave that value in
         * the map and release the created value.
         */

        // 创建一个默认的对象，create() 默认返回 null ，可自定义实现，返回一个默认的对象
        V createdValue = create(key);
        if (createdValue == null) {
            return null;
        }

        // 如果有默认对象，那么这个对象也是占用空间的
        synchronized (this) {
            createCount++;
            // 把创建的对象放入 map 中，返回 map 中的原对象
            mapValue = map.put(key, createdValue);
            // 由于 create() 方法没有同步保护，所以这里需要再次检查，一般情况下 mapValue 会是空的，但是在多线程下，有可能不为空。 
            if (mapValue != null) {
                // There was a conflict so undo that last put
                // 如果不为空，保留原对象
                map.put(key, mapValue);
            } else {
                // 计算创建的默认对象占用的空间
                size += safeSizeOf(key, createdValue);
            }
        }

        
        if (mapValue != null) {
            // 刚创建的默认对象需要做一些回收的操作，如果需要的话。
            entryRemoved(false, key, createdValue, mapValue);
            return mapValue;
        } else {
            // 如果默认的对象被放入到 map 中，需要重新检查和裁剪 map 大小。
            trimToSize(maxSize);
            return createdValue;
        }
    }

### put()


    /**
     * Caches {@code value} for {@code key}. The value is moved to the head of
     * the queue.
     *
     * @return the previous value mapped by {@code key}.
     */
    public final V put(K key, V value) {
        if (key == null || value == null) {
            throw new NullPointerException("key == null || value == null");
        }

        V previous;
        synchronized (this) {
            putCount++;
            // 计算将要放入的对象的大小
            size += safeSizeOf(key, value);
            // 把对象放入到 map 中，获取改 key 原对象
            previous = map.put(key, value);
            // 如果该 key 有原对象，减掉它占用的空间
            if (previous != null) {
                size -= safeSizeOf(key, previous);
            }
        }

        if (previous != null) {
            entryRemoved(false, key, previous, value);
        }
        // 重新检查和裁剪 map 大小
        trimToSize(maxSize);
        return previous;
    }


### remove()

remove() 方法的源码就不贴了，相比之下，get() 和 put() 会比较重要一些，而且看明白了 get() 和 put() ，remove() 也就没什么问题了。

### trimToSize(int maxSize)

最长时间没有被使用的内容，在缓存大小超出预设的大小的情况下，这些内容会被移除，从而维护整个 cache 在一个 maxSize 的范围内。


    /**
     * @param maxSize the maximum size of the cache before returning. May be -1
     *     to evict even 0-sized elements.
     */
    private void trimToSize(int maxSize) {

        // 一个 while true 循环，每次循环获得 map 的最后一个 Entry 对象。
        // 移除这个 entry 对象，重新计算大小，直到 size < maxSize

        while (true) {
            K key;
            V value;
            synchronized (this) {
                if (size < 0 || (map.isEmpty() && size != 0)) {
                    throw new IllegalStateException(getClass().getName()
                            + ".sizeOf() is reporting inconsistent results!");
                }

                if (size <= maxSize) {
                    break;
                }

                // BEGIN LAYOUTLIB CHANGE
                // get the last item in the linked list.
                // This is not efficient, the goal here is to minimize the changes
                // compared to the platform version.
                Map.Entry<K, V> toEvict = null;
                for (Map.Entry<K, V> entry : map.entrySet()) {
                    toEvict = entry;
                }
                // END LAYOUTLIB CHANGE

                if (toEvict == null) {
                    break;
                }

                key = toEvict.getKey();
                value = toEvict.getValue();
                map.remove(key);
                size -= safeSizeOf(key, value);
                evictionCount++;
            }

            entryRemoved(true, key, value, null);
        }
    }



### sizeOf() 

一般需要重写，返回每个内容的大小，需要配合 maxSize 使用，一般你需要注意的是，maxSize 的单位要和这个 sizeOf() 的单位保持一致。

### create() 

 在 get() 调用中，可能需要调用 create() 创建默认对象。但是这个方法不是在一个同步语句块中调用的，所以要注意线程安全的问题，具体建议详细看看 get() 的方法是怎么处理的。非常值得阅读，原谅我没有这个表达能力描述~~


    /**
     * Called after a cache miss to compute a value for the corresponding key.
     * Returns the computed value or null if no value can be computed. The
     * default implementation returns null.
     *
     * <p>The method is called without synchronization: other threads may
     * access the cache while this method is executing.
     *
     * <p>If a value for {@code key} exists in the cache when this method
     * returns, the created value will be released with {@link #entryRemoved}
     * and discarded. This can occur when multiple threads request the same key
     * at the same time (causing multiple values to be created), or when one
     * thread calls {@link #put} while another is creating a value for the same
     * key.
     */
    protected V create(K key) {
        return null;
    }

### entryRemoved()

在有对象被从 map 中移除的时候会调用，一般情况下这个方法是需要重写的。这个方法有一个很有用的使用场景，因为这个方法总是在 map 中有对象被移除的时候调用，包括了新的对象替代旧的对象的时候，这个地方如果增加一个回调机制，应该能实现类似于图片下载完成后，替换默认图片的功能。

## 总结

LruCache 就是对一个 LinkedHashMap 的封装，刨掉对 size 的各种计算，就是一个加了同步保护的 linkedHashMap。重点就看 LruCache 是怎么衡量每个对象的 size，以及维护自己的 size 在 maxSize 的范围内。


## DiskLruCache

Android 没有官方的 DiskLruCache 实现。但是基本设计的思路是一样的，如果你能理解 LruCache 的使用，看 DiskLruCache 的话，无非就是代码量大了几个数量级而已。LruCache 维护的是一个 LinkedHashMap，DiskLruCache 维护的是一个文件目录。
