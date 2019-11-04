# Maven Build 生命周期
- 2014-11-21 03:09:19
- 操作系统与开发环境
- 生命周期,maven,

<!--markdown-->Maven 有三个 Build 生命周期，default , clean , site . default 生命周期处理项目的部署，clean 处理项目的清理，site 处理生成项目的文档。


<!--more-->


每个 build lifecycle 定义了不同的构建阶段。default build lifecycle 的主要的阶段有：

 - validate 校验 ，校验项目是否是正确的，必要的信息是否都是可用的
 - compile 编译，编译代码
 - test 测试，使用相应的单元测试框架进行测试，这些测试可以在代码打包和部署前执行。
 - package 打包，把编译完成的代码打包
 - integration-test 集成测试，如果需要的话，执行和部署安装包到一个可以进行集成测试的环境，执行集成测试。
 - verify 验证,验证包是否是有效的，是否遇见质量问题
 - install 安装，把包安装到本地的仓库，以便其他项目使用
 - deploy 部署，在一个集成环境或者发布环境（integration or release environment）执行，拷贝最终的包到远程的仓库，以便和其他开发者和项目分享。

运行命令 ’mvn deploy‘ 会执行包括 deploy 之前的所有步骤。生命周期中的各个阶段会顺序执行，Maven 也提供了你个性化的定义，你可以跳过中间的某些步骤。但是还是建议能保持整体的生命周期顺序，这样也方便维护和他人学习，使用。