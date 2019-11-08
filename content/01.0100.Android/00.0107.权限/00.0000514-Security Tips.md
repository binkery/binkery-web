# Security Tips
- Security Tips
- 2016-03-22 07:18:16

Android 系统提供了 N 多的安全机制(secutiry features)，来包含应用，系统和用户的数据安全。包括：

- 应用沙盒（Application Sandbox),应用沙盒保证每个应用都是相对独立的运行在系统之上。
- 应用框架实现了健全的通用安全功能（common security functionality)，比如 密码（cryptography）,权限（permissions）和安全的进程间通信（secure IPC)
- 一些NB的技术来降低通用内存管理错误（common memory management errors）的风险。比如：ASLR,NX,ProPolice,safe_iop,OpenBSD dlmalloc,OpenBSD calloc , and Linux mmap\_min\_addr。
- 加密的文件系统（encrypted filesystem)，保护数据丢失和被盗（lost or stolen）。
- 用户授权（user-granted permissions）机制来约束（restrict）系统功能和用户数据的访问。
- 应用扩展的权限（Application-defined），来控制每个应用的数据访问权限。

## 保存数据 Storing Data

大部分应用都需要在用户的手机上储存点数据。

### 内部存储

默认的，在内部存储（internal storage）创建的文件只属于你的应用。

不过，你应该避免在 IPC 文件中使用 MODE\_WORLD\_WRITEABLE 或者 MODE\_WORLD\_READABLE 模式，因为他们没有提供限制个别应用访问数据的能力，也没有任何对数据格式的控制。You should generally avoid using the MODE_WORLD_WRITEABLE or MODE_WORLD_READABLE modes for IPC files because they do not provide the ability to limit data access to particular applications, nor do they provide any control on data format. 

如果需要，可以使用 Content Provider 的方式向其他应用进程分享数据，它提供清晰的读和写权限，也提供了针对每个访问的动态权限授权。

对于敏感的数据（sensitive data），你可以选择使用对本地文件进行加密（encrypt local file)，但是需要使用一个应用不能直接访问的 key 。	java.security.KeyStore 这个类就提供了一个加密的机制，可以把密码加密后存储在文件里本地文件里。<http://stackoverflow.com/questions/3027273/how-to-store-and-load-keys-using-java-security-keystore-class>

### 外部存储 Using external storage

外部存储的安全等级就比较低了，所以不建议把一些比较隐私的数据存储到外部存储中。如果采用动态加载机制的应用，加载外部存储的可执行代码的时候，需要验证以下签名证书，以免加载恶意代码。

### Using Content Provider

Content Provider 对于数据的保护有比较严格的机制。如果 Provider 在 manifest 注册的时候设置 android:exported=false ，这么，这个 Provider 只能这个应用访问，其他应用无权访问。
如果你的 Provider 打算对其他应用分享数据，那么你可以给 Provider 的读和写分别定义权限，只有申请了对应权限的应用，才可以访问和操作数据。
如果你只打算在你的多个应用直接共享数据，那么可以设置 android:protectionLevel=signature ，这样，只有相同的证书签名的应用，才可以共享这些数据。
Content Provider 还提供一个 URI 权限机制，对某个资源的访问做出一个临时的授权。

## Using Permission

所有的 Android 应用都运行在沙盒里，应用通过申请权限，来获取访问和操作沙盒以外的资源。

### 申请权限 Requesting Permissions

关于权限的申请，Android 当然希望你尽量的避免申请权限了，但是实际情况，呵呵～～

### 自定义权限 Creating Permissions

一般，除非作为平台级的应用，像微信，微博这类的，大部分应用推荐使用 signature 的 protection level 来自定义权限。如果你需要创建一个危险的权限，那么有几个需要注意的。

- 因为危险的权限是需要用户手动授权的，所有，需要一个简明的文案来描述权限。
- 这个文案可能需要多语言支持
- 因为这不是一个系统定义的权限，用户可能会产生一些迷惑而放弃安装一些应用。这应该是 Google 想多了～～
- 可能在你的应用没安装前，申请权限的应用已经在安装了。

## 网络 Using Networking

对于用户的私人数据，网络是最有可能泄密的一个方式了。

### Using IP Networking

因为你不确定用户连的是什么样的 wifi，所以，有关敏感数据，尽量使用 HTTPS 来请求，Android 提供了 HttpsURLConnection 类来完成 HTTPS 请求。当然，一般第三方网络请求框架都给你做好了。
如果需要使用 Socket，Android 提供了 SSLSocket 类来支持安全的 socket 连接。
有些应用会在使用本地网络（localhost）的端口来对外分享数据，这样是比较危险的，这样的端口，对于设备上的所有进程都是共享的，可访问的。对于这种需求，Android 推荐使用 Service 来实现进程间的通信。

Also, one common issue that warrants repeating is to make sure that you do not trust data downloaded from HTTP or other insecure protocols. This includes validation of input in WebView and any responses to intents issued against HTTP.

### Using Telephony Networking

短信（SMS）是一个比较私人的，用户之间通信的工具，不是很适合应用通过它来传送数据。当然，技术上是可行的，但是不建议这么做。也不建议服务器通过短信的形式向客户端推送信息。通过短信推送信息是一个可行的推送技术方案，但是并不被建议这么使用。

短信的内容在用户设备上是没有进行任何加密的，所以，你的数据很可能被别人拿走，你也很可能拿到伪造的数据。

## Performing Input Validation

待完成。


## Handing User Data

你的应用可能会访问用户的私人数据，但是尽量不要保存这些私人数据到你的应用中，或者，如果你需要保留（keep）这些数据，尽量不要简单的存储在容易被别的应用获取的位置，已经使用一些手段防止别的应用解读这些数据。比如使用 hash 运算后的邮箱地址，而不是直接明文传输邮箱地址。

如果需要一个 GUID，不要简单的使用用户的手机号，或者 IMEI 号当成用户的 GUID，这样会很不安全，因为这样的号码其他的应用也很轻松可以获取到，而且很容易泄露用户的手机号或者 IMEI 号，给用户的安全带来一定的威胁。<http://android-developers.blogspot.com/2011/03/identifying-app-installations.html> 这一篇文章详细介绍这方面的知识。

## WebView 的使用

Webview 的使用也需要注意防范一些常见的网页安全问题（common web security issues) ，比如 cross-site-script(JavaScript inJection) , 也就是跨域的脚本注入。如果你的应用中的 WebView 可以不需要使用 JavaScript，尽量不要调用 setJavaScriptEnabled() 方法。

addJavaScriptInterface() 方法提供了 JavaScript 代码调用 Java 代码的方式，所以使用的时候，一定要确保网页是可信的（trustworthy)。

通过WebView 访问了一些用户的敏感数据，可以使用 clearCache() 的方法，清空存储在本地的缓存，也可以在服务端添加 no-cache 的 header，这样 WebView 是不会缓存对应的数据的。

Android 4.4 以前的 webkit 存在一些已知的安全问题。作为一个临时的方案（workaround)，你只能确保 WebView 加载的是可信的内容。像微信，QQ 之类的，通过一个 WebView 打开用户分享的一个连接，他们就不是简单的使用 WebView 直接打开了。我没有详细分析过，不过粗略的预测，他们对不容的内容有不同的安全级别。有可信的内容，比如通过微信的平台制作的连接，有不可信的内容，比如就是一个普通的连接，他们的处理方式是不一样的。
有关 SSL 可以阅读 <http://developer.android.com/training/articles/security-gms-provider.html> 了解更多知识。

### 管理证书

一般来说，当用户登陆应用后，应用不要存储用户的密码在本地，而是使用一个 short-lived ,service-specific authorization token. Android 提供了相关的 API : AccountManager 。通过　AccountManager ，你可以让你的多个应用使用同一个账号登陆，避免多次登陆，分别管理的问题。如果你只有一个应用，可以使用　KeyStore 来存储。

## 密码的使用　Using Cryptography

Android 提供了丰富的加密算法（a wide array of algorihms）。HTTPS , HttpsURLConnection ,SSLSocket 都是现成的。Cipher 类也提供了　AES 和　RSA 算法，这些也是现成的。随机数的生成算法有　SecureRandom，密码钥匙的生成有　KeyGenerator。KeyStore 可以用来存储 key。

## 进程间通信的使用 Using Interprocess Communication

尽量使用　Intent，Service 的　Binder 或者　Messenger，以及　BroadcastReceiver 来实现进程间通信，尽量不要使用　network socket 和　共享文件（shared files) 的方式。

如果你的 service 不想分享数据给其他应用，使用 android:exported = false 的方式注册。这样能保证在相同 UID 下，数据的安全。如果需要和其他应用分享数据，那么和 Content Provider 一样，通过定义权限，和设置权限等级的方式可以限制其他非法应用对数据的访问。

### Using Intent

一般，你会通过 sendBroadcast(),sendOrderBroadcast() 或者一个显示的 intent 把消息传递到一个应用组件（application component)。注意，使用有序广播的时候，不是所有的接收者都有可能接收到你的广播，如果你明确需要某个接收者收到这个广播，需要使用显示的 intent。对于广播，可以给 Intent 添加权限限制，保证拥有合法授权的组件能收到这个 Intent。

### Using Service

如果只需要在自己的应用使用的 service，可以通过添加 android:exported 的方式限制其他应用访问。
如果需要对其他应用开放，可以通过定义权限的方式，只有获得授权的应用有权与 service 进行交互。
service 还可以通过 checkCallingPermission() 方法要验证调用者是否获取相应的权限。

### Using binder and messenger interface

尽量使用 Binder 和 Messenger 。Binder 和 Messenger 没有单独的权限设置，他们依附于对于的 Activity 和 Service，如果需要的话，可以通过 checkCallingPermission() 方法来验证权限。

### Using Broadcast Receivers

BroadcastReceiver 默认的可以接收到任何应用发起的广播。不过你可以通过添加权限的方法，来限制，或者说过滤广播。

## 动态加载代码 Dynamically Loading Code

Android 官网各种建议，各种提示动态加载的危险和风险，但是并不影响开发者的热情，因为 Android作为应用层开发，技术就那么点了，玩完了就没别的完了，所以各路高手只能集中在某几个比较有技术含量的领域了，动态加载就是其中的一个。

动态加载技术依赖于 Java 的类加载机制（Class Loader），在 Android 上的运用主要是插件化编程和热修复等。这使用动态加载的时候，需要注意的是，对要加载的 dex 文件，或者 apk 做一个验证。因为这些被加载进来的代码最终是运行在你的应用里的，如果这些文件是不可信的，那么这些代码可能就是一些恶意代码了。

## Serurity in a Virtural Machine 

Dalvik 是一个 Android 运行时虚拟机，跟其他虚拟机一样，Android 也存在一些安全问题，但是一般情况下，开发者并不需要关心这些。

- <http://www.securingjava.com/toc.html>　 
- <https://www.owasp.org/index.php/Java_Security_Resources>

## Security in Native Code

Android 使用的是　Linux kernel，所以和大部分的　Linux 开发碰见的安全问题是相似的，更多可以阅读：<http://www.dwheeler.com/secure-programs>。比较大的不同是　Android 的沙盒机制，这和普通的 Linux 开发有稍微不同的区别。






