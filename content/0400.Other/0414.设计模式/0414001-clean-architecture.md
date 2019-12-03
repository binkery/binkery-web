# Android 开发的整洁架构
- Android,开发,架构
- 2018.08.03

这位作者提出了整洁架构 Clean Architecture。什么是整洁架构，作者给出的解释是这样的，Generally in Clean, code is separated into layers in an onion shape with one dependency rule: The inner layers should not know anything about the outer layers. Meaning that the dependencies should point inwards.大概意思就是代码会被分成很多层，内层不需要知道任何外层的细节。

这位作者提出了整洁架构 Clean Architecture。什么是整洁架构，作者给出的解释是这样的，Generally in Clean, code is separated into layers in an onion shape with one dependency rule: The inner layers should not know anything about the outer layers. Meaning that the dependencies should point inwards.大概意思就是代码会被分成很多层，内层不需要知道任何外层的细节。

## 整洁架构带来的好处

 * Independent of Frameworks
 * Testable.
 * Independent of UI.
 * Independent of Database.
 * Independent of any external agency.

## 对 Android 意味着什么

在 Android ，我们一般会把代码分成三层

 * Outer: Implementation layer 实现层
 * Middle: Interface adapter layer 接口适配层
 * Inner: Business logic layer 业务逻辑层

实现层的代码主要是调用 framewrok API 。包括创建 Activity ，Fragment，链接数据库，发起网络请求等。

接口适配层是连接实现层和业务逻辑层的中间那层，（废话～～

最重要的层是业务逻辑层。这是你真正解决你想要解决的问题的地方，这一层不包含任何特定于框架的代码，你应该能够在没有模拟器的情况下运行它。通过这种方式，您可以拥有易于测试、开发和维护的业务逻辑代码。这是清洁体系结构的主要好处。

每一层，在核心层之上，也负责将模型转换为低层模型，然后底层就可以使用它们。内部层不能引用属于外层的模型类。然而，外层可以使用和引用来自内层的模型。同样，这是由于我们的依赖规则。它确实创建了开销，但是确保代码在层之间解耦是必要的。


接下来是如何构建一个干净的 Android 项目 <https://medium.com/@dmilicic/a-detailed-guide-on-developing-android-apps-using-the-clean-architecture-pattern-d38d71e94029> ， 文章比较长，但非常值得一读。
