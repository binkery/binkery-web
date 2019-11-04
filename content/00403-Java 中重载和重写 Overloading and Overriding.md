# Java 中重载和重写 Overloading and Overriding
- 2016-03-22 07:31:07
- Java
- java,重载,overriding,overloading,重写,

<!--markdown-->## 重载 Overloading

在一个类中，存在多个相同方法名的方法。以 System.out.println() 为例，没有任何参数，打印一行空行，传 String 对象就打印 String，传 int 就打印 int 的值，传 double 就打印 double 的值，传其他对象就打印该对象的 toString() 方法返回的字符串。


<!--more-->


1. 方法名字一定是相同的，不相同就是两个方法了（废话）。
2. 参数列表一定要不同。这是必须的。
3. 返回类型可以不同。这是随意的，两个 int 相加返回 int ，两个 float 相加返回 float，两个 String 相加返回 String，这都是 OK 的。
4. 可以任意的定义异常抛出。
5. 跟权限修饰符没有关系。

* int add(int a , int b);// 以这个方法为基准
* int add(int a, int b , int c);//参数列表不一样，个数不一样
* int add(int a , float b);//参数列表不一样，类型不一样
* float add(float a, float b);//参数列表不一样，类型不一样，返回类型也不一样。
* float add(int a , int b); // 这个是错误的，编译器会提示错误的。返回类型不一样，但是参数列表一样。

重载的时候需要注意基础数据类型和其封装类的自动装箱和拆箱。还需要注意参数子类和父类的继承关系。

## 重写 Overriding

重写是子类重新实现了父类的方法。

1. 方法名，参数列表与父类的方法一致，不一致就不是重写了，是重载。就是子类丰富了 API 。
2. 返回类型可以不一样，但必须是父类该方法的返回类型的子类。父类的返回类型是动物，子类不能返回植物，也不能返回桌子椅子，但可以返回猴子，猩猩啥的。
3. 可以修改方法的权限修饰，但只能往更开放的权限修改，或者保持一致。
4. 不能重写 private 的方法。父类 private 的方法，子类也有相同的方法，不叫重写，是两个方法。
5. 如果定义了异常抛出，子类只能定义父类方法的异常类的子类。
6. final 的方法不能被重写。

[Java 专题整理][1]


  [1]: http://www.binkery.com/archives/478.html