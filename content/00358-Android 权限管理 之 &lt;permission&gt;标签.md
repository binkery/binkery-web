# Android 权限管理 之 &lt;permission&gt;标签
- 2014-11-20 06:08:34
- Android
- android,权限,permission,

<!--markdown-->Declares a security permission that can be used to limit access to specific components or features of this or other applications. 声明一个可以被用来限制应用自身或者其他应用访问某些组件或者功能的安全权限。


<!--more-->


    <permission 
    android:description="string resource" 
    android:icon="drawable resource" 
    android:lebel="string resource" 
    android:name="string" 
    android:permissionGroup="string" 
    android:protectionLevel=["normal" | "dangerous" | "signature" | "signatureOrSystem"]/>

- android:description 一个比label更长更详细一些的用户可读的描述。这个属性必须是一个 string 资源的引用。

- android:icon 就是一个icon。

- android:label 权限的一个描述，虽然可以直接使用 string ， 但是还是建议使用 string 资源的应用。

- android:name 权限的名字，这个名字将在相应的 <uses-permission> 标签中被使用。这个名字必须是唯一的。推荐使用这个样子的格式： com.example.project.PERMITTED_ACTION 

- android:permissionGroup 把这个权限指向一个群。这个属性的值必须是一个 group 的名字，这个名字是声明在这个或者其他的应用的 <permission-group>里的。这个属性可以没有设置。

- android:protectionLevel  这个比较复杂点，翻译不好，直接 copy 原文过来。Characterizes the potential risk implied in the permission and indicates the procedure the system should follow when determining whether or not to grant the permission to an application requesting it.有几个值：

  - normal ： 默认的，最低风险的权限，在安装的时候，系统会自动授予权限。
    The default value. A lower-risk permission that gives requesting applications access to isolated application-level features, with minimal risk to other applications, the system, or the user. The system automatically grants this type of permission to a requesting application at installation, without asking for the user's explicit approval (though the user always has the option to review these permissions before installing).

  - dangerous ： 危险的，更高一点风险的权限。系统不会自动授予权限给应用，在使用的时候，会提示用户确定。
    A higher-risk permission that would give a requesting application access to private user data or control over the device that can negatively impact the user. Because this type of permission introduces potential risk, the system may not automatically grant it to the requesting application. For example, any dangerous permissions requested by an application may be displayed to the user and require confirmation before proceeding, or some other approach may be taken to avoid the user automatically allowing the use of such facilities.

  - signature : 签名的。
    当申请该权限的应用的签名证书与该权限所在的应用的证书相同的时候，系统会自动授权。比较绕，就是说两个应用需要有相同的签名证书。一般出现在某些公司有多个应用，多个应用之间会共享一些资源，但是不想被其他第三方应用使用。只要证书相同，系统会自动授权，不需要跟用户确定。A permission that the system grants only if the requesting application is signed with the same certificate as the application that declared the permission. If the certificates match, the system automatically grants the permission without notifying the user or asking for the user's explicit approval.

  - signatureOrSystem ： 签名或者系统的。
    一般不推荐使用。可能用得比较多的是手机厂商和预装应用。A permission that the system grants only to applications that are in the Android system image or that are signed with the same certificate as the application that declared the permission. Please avoid using this option, as the signature protection level should be sufficient for most needs and works regardless of exactly where applications are installed. The "signatureOrSystem" permission is used for certain special situations where multiple vendors have applications built into a system image and need to share specific features explicitly because they are being built together.