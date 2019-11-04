# Android SparseArray 系列
- 2015-03-06 13:55:30
- Android
- android,sparsearray,性能优化,

<!--markdown-->SparseArray 是 android.util 包里的一个工具。SparseArray 是 Integer 到 Object 的一个映射，可以在某些场合替换HashMap\<Integer,\<E\>\>。


<!--more-->


从名字上，SparseArray 首先是一个 Array ， 第二，它不是普通的 Array 。它的不普通表现在它是为了节省内存开销而存在的一种数组。

假设现在有这样的情况，我们定义了一个长度为100的数组，虚拟机为我们开辟了100个单位的内存空间，但是我们只使用了很少（假设是5个）的一些单元，这样就造成了内存空间的浪费。而 SparseArray 是一个优化的数组，它的 key 是 Integer 类型而不是其他类型，是因为这个数组是按照 key 值的大小来排序的。按照 key 值大小排序的好处是查找的时候，可以使用二分查找，而不是蛮力的遍历整个数组。这也是为什么 SparseArray 适合替换 HashMap\<Integer,\<E\>\>，而不是任何 HashMap 的原因了。在这种情况下，原本需要100个单位内存空间而 SparseArray 只占用了5个单位的内存（实际比5个单位要大一些，因为还有一些逻辑控制的内存消耗）。key 值被当成了数组下标的功能来使用了。

有几个我觉得应该注意的情况。

1. SparseArray 在某些场合下可以用来替换 HashMap\<Integer,\<E\>\>

2. SparseArray 是有一定的性能上的消耗的，并不适合当成包含大量元素的容器。The implementation is not intended to be appropriate for data structures that may contain large numbers of items. 

3. SparseArray 不是线程安全的。

4. SparseArray  插入数据按 key 大小顺序插入，使用对 key 进行二分查找

5. SparseArray 对删除做了一个优化，不会直接立即删除一个元素，而是把该位置的值设置成 DELETED ，尝试 reuse

最后这里还有个建议，网上对 SparseArray 的描述挺多的，Android 官方文档也有详细的介绍，但是其实 SparseArray 这个类的代码不多，花点时间看看它是怎么实现的，搞明白了，就很清楚什么时候该用什么时候不该用了。