# alertdialog的使用
- 2015-03-06 08:38:13
- Android
- android,alertdialog,

<!--markdown-->这个类的学习使用，让我知道了找问题的方法。比如，this的纠正过程。读懂报错的注释。


<!--more-->


    new AlertDialog.Builder(this)
    .setTitle(“help”)
    .setMessage(“helpworld”)
    .setPositiveButton(“确定”, null)
    .show();