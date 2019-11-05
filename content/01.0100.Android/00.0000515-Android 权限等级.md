# Android 权限等级
- 2016-03-22 07:19:02
- Android
- 

<!--markdown-->
Android 定义了四种权限等级（protection level)，分别是 normal,dangerous,signature 和 signtureOrSystem

## normal

最低的权限等级，有比较低的风险。当一个应用在申请这样的权限的时候，系统会很大方的替用户授权。如果你自己定义了这样等级的权限，需要考虑到这样的风险。

## dangerous

有比较高风险的权限。表示可能会获取用户的私人的敏感数据。对于这样的权限，系统就不会擅自帮用户做主了，在安装的时候会明显的提示用户，得到用户的授权。

## signature

如果 A 应用定义了一个权限，等级为 signature，如果 B 应用申请了这个权限，只有当 B 应用和 A 应用使用相同的证书签名的情况下，系统会自动的授权给 B 应用权限。这个不需要通知用户，也不需要用户干预。这意味着，A 应用和 B 应用应该是同一个开发者或者公司。所以包含好你的证书很关键的。

## signatureOrSystem

这样一个等级的权限，只有你的 APP 存在于 Android 系统的镜像里（Android System Image）或者使用相同证书签名的应用。官网建议使用 signature 而不适用 signatureOrSystem .这个等级的权限一般用在系统的内置应用。
