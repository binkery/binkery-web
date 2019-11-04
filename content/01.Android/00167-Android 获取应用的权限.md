# Android 获取应用的权限
- 2015-03-06 09:35:01
- Android
- android,权限,permission,packagemanager,

<!--markdown-->Android通过应用的包名，可以获取该应用需要的权限。不过在具体的开发中发现了一个问题。


<!--more-->


代码如下：

    PackageManager mPackageMgr = getPackageManager();
    PackageInfo pack = mPackageMgr.getPackageInfo(packageName,PackageManager.GET_PERMISSIONS);
    PermissionInfo[] permissions = pack.permissions; //这里为null
    String[] permissionStrings = pack.requestedPermissions; //这里是正确的内容

第一种方法直接返回PermissionInfo对象数组，但是一直为空。看来是被废了。

第二种方法正确的返回了我所要的数据，不过返回的是一个String ， 需要再把它变成一个PermissionInfo 对象。