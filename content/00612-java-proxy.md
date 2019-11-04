# Java 动态代理 Proxy
- 2019.06.12
- Java
- Java,动态代理,反射
- Java动态代理,JavaProxy,Java反射代理

最近在阅读 Retrofit 的源代码，顺便整理一下 Java 反射类 Proxy 实现的动态代理。

在阅读 Retrofit 源代码之前，我一直以为 Retrofit 采用的是 **注解** 加 **注解处理器**（Annotation Processor）的方式来实现的网络请求的封装的，而事实上并不是这样的。Retrofit 的注解都是运行时注解（@Retention(RUNTIME)），而不是源代码注解（@Retention(RetentionPolicy.SOURCE)），这样就意味着，网络请求是在运行时通过反射的方式来组装的。

在组装网络请求时，用到了 Java 反射库中的 Proxy 来实现了动态代理。代码如下：

    public <T> T create(final Class<T> service) {
        Utils.validateServiceInterface(service);
        if (validateEagerly) {
            eagerlyValidateMethods(service);
        }

        // 动态代理

        return (T) Proxy.newProxyInstance(service.getClassLoader(), new Class<?>[] { service },
            new InvocationHandler() {
                private final Platform platform = Platform.get();
                private final Object[] emptyArgs = new Object[0];

                @Override
                public @Nullable Object invoke(Object proxy, Method method,
                @Nullable Object[] args) throws Throwable {
                // If the method is a method from Object then defer to normal invocation.
                // 特殊的，比如 equals 方法，Object 自身的方法
                if (method.getDeclaringClass() == Object.class) {
                    return method.invoke(this, args);
                }
                if (platform.isDefaultMethod(method)) {
                // 平台的方法，
                    return platform.invokeDefaultMethod(method, service, proxy, args);
                }
                // service 的方法，这里应该就是咱们接口定义的方法
                return loadServiceMethod(method).invoke(args != null ? args : emptyArgs);
            }
        });
    }

Retrofit.create() 方法的入参是 Class<T\> ，返回类型是 T ，这里的 T 是泛型。我们只写了个接口，并没有具体的实现类，而 create 方法却可以返回一个实现类，这里就是动态代理。

## Proxy.newProxyInstance 方法

**Proxy.newProxyInstance(ClassLoader ,Class<?>[] , InvocationHandler )** 方法入参为一个 ClassLoader ，一个 Class 数组，一个 InvocationHandler ，返回类型是 Object 。也就是通过这个方法，它会返回一个集成了给定接口的类的对象。

这个方法有三行核心的代码，第一行通过获取一个继承了所有接口的类；第二行获得该类的某个指定构造器；第三行通过构造器实例化对象。

    public static Object newProxyInstance(ClassLoader loader, Class<?>[] interfaces, InvocationHandler h) throws IllegalArgumentException {
        if (h == null) {
            throw new NullPointerException();
        }

        /*
         * Look up or generate the designated proxy class.
         */
        Class<?> cl = getProxyClass0(loader, interfaces);   // 1 获得类

        /*
         * Invoke its constructor with the designated invocation handler.
         */
        try {
            // constructorParams 的定义：
            // private final static Class[] constructorParams =
            //  { InvocationHandler.class };
            final Constructor<?> cons = cl.getConstructor(constructorParams);  // 2 获得构造器
            return newInstance(cons, h); // 3 实例化对象
        } catch (NoSuchMethodException e) {
            throw new InternalError(e.toString());
        }
    }

    
## Proxy.getProxyClass0 方法

通过 **Proxy.getProxyClass0(ClassLoader , Class<?> )** 方法，返回一个集成了所有接口（interface）的类（class）对象。方法体里， proxyClass 是最终被返回的类对象。这个方法比较长，但是咱们可以分几个大的步骤。

1. 各种校验，对各个接口进行校验
2. 从缓存里获取 **proxyClass** 对象。毕竟 proxyClass 的创建肯定是很费资源的，所以缓存是必要的。
3. 如果缓存里没有的话，就需要自己创建代理类对象，核心是调用 generateProxy 方法。调用这个方法前，需要做一些准备工作，确定代理类所在的包，获得代理类所有继承的方法，已经方法的返回类型，抛出的异常等等。
4. finally 语句块就是善后处理工作了。

下面是 getProxyClass0() 方法，我做了一些删减。

    private static Class<?> getProxyClass0(ClassLoader loader,
                                           Class<?>... interfaces) {
        if (interfaces.length > 65535) {
            throw new IllegalArgumentException("interface limit exceeded");
        }

        // 最终要返回的对象，代理类
        Class<?> proxyClass = null; 

        /* collect interface names to use as key for proxy class cache */
        String[] interfaceNames = new String[interfaces.length];

        // for detecting duplicates
        Set<Class<?>> interfaceSet = new HashSet<>();

        // 1. 各种校验
        for (int i = 0; i < interfaces.length; i++) {
            /*
             * Verify that the class loader resolves the name of this
             * interface to the same Class object.
             */
            String interfaceName = interfaces[i].getName();
            Class<?> interfaceClass = null;
            try {
                interfaceClass = Class.forName(interfaceName, false, loader);
            } catch (ClassNotFoundException e) {
            }
            if (interfaceClass != interfaces[i]) {
                throw new IllegalArgumentException(
                    interfaces[i] + " is not visible from class loader");
            }

            /*
             * Verify that the Class object actually represents an
             * interface.
             */
            if (!interfaceClass.isInterface()) {
                throw new IllegalArgumentException(
                    interfaceClass.getName() + " is not an interface");
            }

            /*
             * Verify that this interface is not a duplicate.
             */
            if (interfaceSet.contains(interfaceClass)) {
                throw new IllegalArgumentException(
                    "repeated interface: " + interfaceClass.getName());
            }
            interfaceSet.add(interfaceClass);

            interfaceNames[i] = interfaceName;
        }

       
        // 2. 从 loaderToCache 里，获得 proxyClass ，这里代码有省略
        List<String> key = Arrays.asList(interfaceNames);

        Map<List<String>, Object> cache;
        synchronized (loaderToCache) {
            cache = loaderToCache.get(loader);
        }
        synchronized (cache) {
            do {
                Object value = cache.get(key);
                if (value instanceof Reference) {
                    proxyClass = (Class<?>) ((Reference) value).get();
                }
                if (proxyClass != null) {
                    return proxyClass;
                }
            } while (true);
        }

        // 3. 创建代理类
        try {
            // 定义代理类的包
            String proxyPkg = null;     // package to define proxy class in

            
            for (int i = 0; i < interfaces.length; i++) {
                int flags = interfaces[i].getModifiers();
                if (!Modifier.isPublic(flags)) {
                    // 这里省略了代码
                    // 如果接口定义不是 public 的，那么接口需要在同一个包下
                }
            }

            if (proxyPkg == null) {
                // if no non-public proxy interfaces, use the default package.
                // 如果没有非 public 的接口，那么使用默认的包
                proxyPkg = "";
            }

            {
                // Android-changed: Generate the proxy directly instead of calling
                // through to ProxyGenerator.
                // 获得接口定义的所有方法。这里 Android 和 Java 有一些不一样。
                List<Method> methods = getMethods(interfaces);
                Collections.sort(methods, ORDER_BY_SIGNATURE_AND_SUBTYPE);
                validateReturnTypes(methods);
                List<Class<?>[]> exceptions = deduplicateAndGetExceptions(methods);

                Method[] methodsArray = methods.toArray(new Method[methods.size()]);
                Class<?>[][] exceptionsArray = exceptions.toArray(new Class<?>[exceptions.size()][]);

                /*
                 * Choose a name for the proxy class to generate.
                 */
                final long num;
                synchronized (nextUniqueNumberLock) {
                    num = nextUniqueNumber++;
                }
                String proxyName = proxyPkg + proxyClassNamePrefix + num;
                // 生成代理类
                proxyClass = generateProxy(proxyName, interfaces, loader, methodsArray,
                        exceptionsArray);
            }
            // add to set of all generated proxy classes, for isProxyClass
            proxyClasses.put(proxyClass, null);

        } finally {
            // 省略代码
        }
        return proxyClass;
    }


generateProxy 是一个 native 方法。

    private static native Class<?> generateProxy(String name, Class<?>[] interfaces,
                                                 ClassLoader loader, Method[] methods,
                                                 Class<?>[][] exceptions);

## Proxy.getMethods

**Proxy.getMethods(Class<?>[])**用来获得代理类应该集成的所有方法。因为接口可能存在继承，所以这里需要用到递归。

    private static List<Method> getMethods(Class<?>[] interfaces) {
        List<Method> result = new ArrayList<Method>();
        try {
            result.add(Object.class.getMethod("equals", Object.class));
            result.add(Object.class.getMethod("hashCode", EmptyArray.CLASS));
            result.add(Object.class.getMethod("toString", EmptyArray.CLASS));
        } catch (NoSuchMethodException e) {
            throw new AssertionError();
        }

        getMethodsRecursive(interfaces, result);
        return result;
    }

    private static void getMethodsRecursive(Class<?>[] interfaces, List<Method> methods) {
        for (Class<?> i : interfaces) {
            getMethodsRecursive(i.getInterfaces(), methods);
            Collections.addAll(methods, i.getDeclaredMethods());
        }
    }

## Proxy.newInstance

实例化代理类的一个关键是，每个代理类都有一个特殊的构造器，也就是每个代理类都有一个 InvocationHandler 对象，在调用代理类的方法的时候，实际调用的是 InvocationHandler 的方法。这样，我们只需要实现 InvocationHandler 就可以实现动态代理了。

 > Each proxy class has one public constructor that takes one argument,
 > an implementation of the interface {@link InvocationHandler}, to set
 > the invocation handler for a proxy instance.  Rather than having to use
 > the reflection API to access the public constructor, a proxy instance
 > can be also be created by calling the {@link Proxy#newProxyInstance
 > Proxy.newProxyInstance} method, which combines the actions of calling
 > {@link Proxy#getProxyClass Proxy.getProxyClass} with invoking the
 > constructor with an invocation handler.

    private static Object newInstance(Constructor<?> cons, InvocationHandler h) {
        try {
            return cons.newInstance(new Object[] {h} );
        } catch (IllegalAccessException | InstantiationException e) {
            throw new InternalError(e.toString());
        } catch (InvocationTargetException e) {
            Throwable t = e.getCause();
            if (t instanceof RuntimeException) {
                throw (RuntimeException) t;
            } else {
                throw new InternalError(t.toString());
            }
        }
    }

## 总结

整个代码整理下来，我们大概知道，动态代理主要有两个核心的类，一个是 **Proxy** 类，一个是 **InvocationHandler** 类。通过 Proxy 类，我们可以获得一个接口的代理对象，调用代理对象的方法时，会转交给 InvocationHandler 来处理，于是，我们只需要实现 InvocationHandler 来实现具体的业务逻辑。

这样就可以把方法的定义和方法的实现分离。
