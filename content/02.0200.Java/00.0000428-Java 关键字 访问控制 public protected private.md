# Java 关键字 访问控制 public protected private
- Java,关键字,public,private,protected,

Java 共有三个访问控制的关键字，public , protected , private . 但实际上，除了这三种访问控制权限外，还有另外一个权限，是默认的，就是当你没有定义成 public , protected , private 三个之中的一个的时候，是默认的权限。网上给它取的名字有很多，有人管它叫 default , 有人叫 package , 也有叫 friendly ，其实都是一个意思。

public , protected , private 是用来修饰类，变量和方法，用来标识对应的类，变量和方法在其他类的访问权限。

 - public 包内及包外的任何类均可以访问。这是最开放的权限。
 - protected 包内的任何类，子类也可以访问。
 - private 包内包外的任何类均不能访问，子类也不能访问。
 - default 包内的任何类都可以访问它，而包外的任何类都不能访问它,包括之类也不能访问。把它成为 package 很形象，只有包内是有权限的，包外的，哪怕是子类都没有权限。当然 friendly 也是很形象了。

访问权限描述里，有两个重点的，理解了为什么这样去做控制，就很好理解各个访问控制的区别了，不用死记硬背了。一个包，一个子类。Java 三大特性，封装，继承，多态，其中，这里跟封装有很大关系。封装的一个目的是把需要开放的开放出去，把不需要开放的隐藏掉，这样别人在调用你的 API 的时候，只需要知道某几个类，方法，变量，而不需要知道全部。这样可以约束开发者，也帮助开发者做好代码的架构和设计，提高内聚，降低耦合。

[Java 专题之关键字](http://www.binkery.com/archives/427.html)