# android的menu实现
- 2015-03-06 07:36:13
- Android
- android,menu,

<!--markdown-->## 用onCreateOptionsMenu方法设置点击菜单后出现的选项；

    public boolean onCreateOptionsMenu(Menu menu) {
    Log.i(tag, “click menu!”);
    menu.add(0, MENU_ID_ABOUT, 0, “about”); //变量值
    menu.add(0, MENU_ID_HELP, 0, “help”);
    return super.onCreateOptionsMenu(menu);
    }

## 写响应事件

    public boolean onOptionsItemSelected(MenuItem item) {
    switch(item.getItemId()){
    case MENU_ID_HELP:
    Log.i(tag, “help menu click”);
    help();
    break;
    case MENU_ID_ABOUT:
    Log.i(tag, “about menu click”);
    about();
    break;
    }
    return super.onOptionsItemSelected(item);
    }