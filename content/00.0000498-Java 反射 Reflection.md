# Java 反射 Reflection
- 2016-03-21 10:11:18
- Java
- java,反射,reflection,

<!--markdown-->
## 几个重要的 API

* java.lang.Class
* java.lang.reflect.Constructor
* java.lang.reflect.Field
* java.lang.reflect.Method
* java.lang.reflect.Modifier

## 获取 Class 对象

使用反射的第一步，就是需要获取 Class 对象。获取 Class 对象有三种方法。

假设咱们在 com.haodf.android.entity 包下有个 Doctor 类。

### 1 Class.forName()

     Class clazz = Class.forName("com.haodf.android.entity.Doctor");

### 2 每个 Java 类都有 class 属性。

     Class clazz = Doctor.class;

### 3 每个 Java 对象都有 getClass() 方法

     Doctor doctor = new Doctor();
     Class clazz = doctor.getClass();

## 通过反射实例化对象

一般咱们实例化一个对象是通过 new 关键词来完成的。除了 new 之外，咱们还可以通过反射来构建对象。
通过反射构建对象有两种方式，一种是直接使用 Class.newInstance() 方法。

    Object object = clazz.newInstance();

这种方式是使用了该类的默认的无参构造器来实例化一个对象。如果该类没有无参构造器，这个方法会抛出一个异常。
还有一种方式是获取构造器。

    Constructor<T> getConstructor(Class...<?> parameterTypes) 
    Constructor[]<?> getConstructors()
    Constructor<T> getDeclaredConstructor(Class...<?> parameterTypes)
    Constructor[]<?> getDeclaredConstructors()

第一个和第三个是通过指定的参数类型，返回特定的构造器。第二个和第四个是返回所有构造器。
Declared 和 没有 Declared 的区别是，没有 Declared 返回是是 pubilc 的构造器，有 Declared 就包含了任何的构造器。

获取了 Contructor 对象后，可以使用 Contructor.newInstance() 方法来构造对象了。

    T newInstance(Object... args)

比如： 

    Contructor doctorContructor = clazz.getConstructor();
    Object doctorObj = personContructor.newInstance();// 注意：这里返回的是 Object ，不是 Doctor

## 访问和修改对象的属性和方法

属性和方法都是类的成员，一般属性也被称为成员变量，方法也被称为成员函数。这个体现在 Field 和 Method 都继承于 java.lang.reflect.Member 接口。

获取 Field 和 Method 的方式和构造器大致相似，这里不多说。

假设咱们的 Doctor 类里有个 age 成员变量，这个变量是 private 的，也就是咱们不能直接访问得到，更不能修改。但是咱们现在又期望能修改这个变量的值。


    Field field = clazz.getDeclaredField("age"); // 因为 age 是 private 的，所以咱们使用 declared 的方式
    field.setAccessible(true); // 同样因为 age 是 private 的，咱们需要设置它为可访问的。
    field.set(doctorObj,50); // doctorObj 为咱们上面获取到的对象

这样子，咱们就修改了 doctorObj 的 age 属性。

下面是调用 Doctor 的 setAge 方法

    Method method= clazz.getMethod("setAge");
    method.invoke(doctorObj,50);

## 反射的使用场景

* 设计模式

    在一些设计模式里，会使用反射机制，通过这样的方式来降低代码的耦合度。
    
* 修改和访问隐藏的属性和方法

    这个也经常用到，比如上面提到的 Doctor 类，这个类不是咱们写的，咱们也没有权限去修改这个类，但是咱们又有修改 age 属性这个需求，那么可以使用反射这种黑科技。不过这样子确实破坏了代码的设计。

## 其他相关的知识点

反射一开始不是很好理解，需要对其他一些相关的知识点也有所了解。

* class 文件
* 类加载

## 链接

* [java反射详解](http://www.cnblogs.com/rollenholt/archive/2011/09/02/2163758.html)
* [JAVA中的反射机制](http://blog.csdn.net/liujiahan629629/article/details/18013523)