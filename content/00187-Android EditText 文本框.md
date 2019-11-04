# Android EditText 文本框
- 2015-03-06 09:55:18
- Android
- android,输入法,edittext,文本框,

<!--markdown-->使用Android EditText 的时候碰见两个问题。


<!--more-->


1. 输入法挡住了输入框

解决办法：在AndroidManifest.xml中的anctivity中添加属性  

    android:windowSoftInputMode="adjustPan"

2. 输入法中找不到回车换行。

解决办法：在EditText 中添加 

    android:inputType="textMultiLine"

网上找了一下，发现很多网友吐曹输入法怎么怎么垃圾，各种输入法躺着也中枪啊。o(∩∩)o...哈哈。