# ListView拖动时背景黑色的问题
- 2015-03-06 09:37:46
- Android
- android,listview,背景,

<!--markdown-->Android系统默认的ListView样式在滚动的时候，背景会出现黑色。


<!--more-->


修改方式如下：

A、通过布局属性来设定(ListView的属性中直接定义)

    android:cacheColorHint=”#00000000″

B、在代码中直接设定

    listView.setCacheColorHint(Color.TRANSPARENT);