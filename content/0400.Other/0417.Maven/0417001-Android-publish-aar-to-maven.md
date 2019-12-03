# Android 发布 aar 到 maven 服务器
- Android,aar,maven,publish,组件化,gradle
- 2018.07.26

最近在搞组件化开发，那么组件化的第一个步骤就是打包上传 aar 到 maven 服务器上，然后在主项目中通过依赖去引入。每一个独立的功能模块被打成一个个 aar 包。独立编译，独立管理。

## 组件化开发

组件化开发已经流行了很长时间了，而我们的项目到现在才开始比较正式的开搞，算是比较晚了。但是总算开始了。

组件化开发是把一个个独立的功能模块，单独编译打包，这样每个功能模块就像一个个组件，在最后发布的时候，合并到主项目来。

理论上都很简单，最难的就是业务解耦了，这得看每个项目业务的复杂程度了。除了业务解耦，我需要为团队提供的就是一个整体的框架和平台。包括开发环境的支持。

基于之前的经验，我为我们负责的两个客户端分别新建了两个 libs 项目。每一个 libs 项目里，包含一个 app 的 application module 和若干个 library module。每一个 library module 就是一个功能模块，他们会单独编译打包，然后上传到 maven 服务器上。

## maven 服务器

我在很早之前就在团队申请了一台服务器，并且架设了 maven 镜像服务器。nexus 的架设很简单，理解几个基本的知识点就可以了。一个 maven 有一个 public 的地址，是一个 group。一个 group 包含若干个 host ，也就是代理，每个 host 代理一个外网服务器，比如 jcenter，ali 的啊，华为的 maven 服务器。然后还有一个 snapshot 和一个 release ，是私有服务器，我们自己开发的 aar 就是上传到 snapshot 和 release 上。

	repositories {
    	maven {
        	url 'http://xxx.xxx:8081/repository/maven-public/'
    	}
	}

在 Gradle 脚本中修改一下 maven 的地址，这样打包的时候，下载依赖啥的都是在内网解决，速度就快了很多。

## maven plugin

一开始在上传 aar 的时候，我使用的是 maven plugin 这个插件。一开始是挺好用的，因为当我的 libs 项目中只包含了一个 library module的时候，并没有出现任何问题。但是后来在做第二个 library module 的时候，就出现问题了。我在每个 library module 的 build.gradle 脚本中，都增加 maven plugin 的应用并且写了 uploadArchives 。但是我发现，当我想发布 B library module 的时候，他会先打包上传 A library module 。为了这个问题，我折腾了很久。虽然我发现可以通过命令行 ./gradlew :b:uploadArchives 来上传 B module 的 aar，但是这不是我想要的，确实影响效率。

## maven publish plugin

后来我才用了 maven-publish 这个插件。这个插件也最终解决了我的问题。我可以在图形界面上很通过双击特定的目标，来上传对应 module 的 aar。

这过程中也碰见了一些问题，最后也都解决了，也整理了一套比较通用的脚本，可以满足我们项目的需求。

### 多个 library module 重复编写 build.gradle 的问题

每一个 library module 都需要一个 build.gradle ,这个 build gradle 文件中有很多都是相同或者相似的，gradle 文件又具有那种难记的特点，在大量进行重复拷贝的时候，如果多了点少了点，很难看出来的。那么我需要想办法管理起来。

在我 project 的根目录下，新建了一个 sample.gradle 文件。这个文件大概是这样的

	apply plugin: 'com.android.library'
	apply plugin: 'maven-publish'

	android{
		// android 的通用配置
	}

	task sourceJar(type:Jar){
		from android.sourceSets.main.java.srcDirs
		classifier "sources"
	}

	publishing{
		publications{
			// 忽略 N 多行代码
		}
		repositories{
			// 忽略 N 多行代码
		}
	}

然后我在 A module 的 build.gradle 里，只需要这样写

	ext.moduleName = 'xxx'
	ext.libSnapshot = true
	ext.libVersionName = '1.0.0'
	apply from: '../sample.gradle'

	dependencies{
		// ...
	}


这样里，每个 module 只需要配置好各自的 module name，并且管理好自己的 version name，其他的东西都在 sample.gradle 中。


### 每个 module 都有 res 前缀约束

为了避免资源 id 冲突，每个 module 都需要有个前缀的约束。这个的实现很简单，我们默认前缀为 module 的名字。在 sample.gradle 中，有这样的配置

	android{
		resourcePrefix "$moduleName" + '_'
	}

这样就可以。


### snapshot 和 release 不同的 maven 地址。

在使用 maven plugin 的时候，snapshot 和 relase 不同的 maven 地址很容易配置，根据 version name 的后缀就自动匹配了。但是 maven-publish plugin 并不是这样的。于是我们需要这样配置

	publishing{
		repositories{
			maven{
				if(libSnapshot){
					url 'http://xxx.xxx/repository/maven-snapshots/'
				}else{
					url 'http://xxx.xxx/repository/maven-releases/'
				}
				credentials{
					username 'xxx'
					password 'xxx'
				}
			}
		}
	}



### maven publish pom 依赖缺失的问题

maven publish 插件生成 pom 文件的时候，缺少了依赖的信息。于是我们需要给他添加进去。

    pom.withXml {
        def dependenciesNode = asNode().appendNode('dependencies')
        configurations.compile.allDependencies.each {
            if (it.group != null && (it.name != null || "unspecified".equals(it.name)) && it.version != null) {
                def dependencyNode = dependenciesNode.appendNode('dependency')
                dependencyNode.appendNode('groupId', it.group)
                dependencyNode.appendNode('artifactId', it.name)
                dependencyNode.appendNode('version', it.version)
            }
        }
    }


## 总计

我目前为止，我们的 gradle 脚本已经基本搞定了，管理起来并没有那么复杂。剩下的就是需要给团队普及一下，大概介绍一下整体的思路已经怎么操作。
