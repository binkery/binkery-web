# Android Doc Content Providers 中文
- 2015-03-06 08:47:52
- Android
- android,contentprovider,翻译,中文,官方文档,

<!--markdown-->Content providers store and retrieve（检索） data and make it accessible（可进入的） to all applications. They're the only way to share data across（穿过） applications; there's no common（普通） storage area that all Android packages can access.


<!--more-->


binkery:在不同的APP直接分享，但不是存储在共同的存储区域，而是存储在特定的空间里。

Android ships with a number of content providers for common data types (audio, video, images, personal contact information, and so on). You can see some of them listed in the android.provider package. You can query these providers for the data they contain (although, for some, you must acquire the proper（适当的） permission to read the data).

binkery:Android系统本身提供了多个provider。

If you want to make your own data public, you have two options: You can create your own content provider (a ContentProvider subclass) or you can add the data to an existing provider — if there's one that controls the same type of data and you have permission to write to it.

binkery:有两种方式把你自己的数据分享给别的App，一个创建自己的provider。另一种方法是把数据写到一个已存在的provider里，当然需要有写的权限。

This document is an introduction to using content providers. After a brief（简要的） discussion of the fundamentals（基础）, it explores how to query a content provider, how to modify data controlled（控制） by a provider, and how to create a content provider of your own.

Content provider basics

Querying a content provider 查询

Modifying data in a provider 修改provider

Creating a content provider 创建provider

Content URI summary