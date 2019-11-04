# JavaMail for Android
- 2015-03-06 13:48:20
- Android
- android,javamail,pop,imap,

<!--markdown-->JavaMail 是由oracle（也就是sun）公司提供的一个在 Java 平台上支持 POP，IMAP 等邮件传输协议的 Java 类库。


<!--more-->


使用起来很简单，但是有很多坑，我就走了不少冤枉路，浪费了很多时间。

1. 总共需要三个jar包，分别是 mail.jar , additionnal.jar , activation.jar , 如果只使用 mail.jar ，在登录链接上没有任何问题，在获取邮件内容的时候，也就是 getContent() 的时候，总会抛出一个异常。

2. mail.jar 不能使用 oracle 提供的，而要在 google code 上获取，不然在 getContent() 的时候，返回的是一个 InputStream 的子类，而不是 MimeMultipart 或者 MimeBodyPart .

一切的一切都只能怪 google 被墙，要是一开始就能正常访问 google code 网站的话，我也不会去别的地方下载mail.jar 了，当然，也不会有上面的一些收获了。当然，最后要感谢 stackoverflow ，上面的第二个问题困扰了我很长时间，一开始返回的是 InputStream，我就通过 IO 流把数据读出来，但是读出来的是一些二进制数据，我不知道该怎么解决了，最后在 stackoverflow 上有个悲剧的哥们提问说为什么返回的是 InputStream 而不是 Part，然后有人告诉他，哥们，你用错包了吧。

至于第一个问题，其实是我咎由自取，有点小小洁癖，看着一下子要导入三个 jar 包，有点小小不爽，心存侥幸心理，以外没有那两个包也是ok的，结果反而让自己多走了不少弯路。

下面的JavaMail for Android 的 google code 地址，希望你能正常访问。三个包都在上面。
https://code.google.com/p/javamail-android/​