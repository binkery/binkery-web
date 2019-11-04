# Android socket 连接客户端代码分享
- 2015-03-06 03:47:28
- Android
- android,socket,代码,

<!--markdown-->Socket 客户端代码分三部分。

* 第一部分是Android客户端的代码，主要是跟android界面和通讯录读取相关的一些代码。代码不多，也就没有分到多个类里面去写了。
* 第二部分是socket的代码，IO操作在一个单独的线程，另外使用了Timer这个类来处理超时的情况。
* 第三部分就是XML了，这个很简单，不多说了。下面就开始贴代码了。主要关键点都打日志了，所以没怎么写注释。


<!--more-->


## 第一部分：Android代码

    package com.binkery;
    
    import android.app.Activity;
    import android.database.Cursor;
    import android.os.Bundle;
    import android.os.Handler;
    import android.os.Message;
    import android.provider.ContactsContract;
    import android.view.View;
    import android.widget.Button;
    import android.widget.TextView;
    
    public class SocketClientActivity extends Activity {
    
    private TextView log;
    private SocketHandler handler;
    private SocketConnect sc;
    private Button uploadBtn;
    
    /** Called when the activity is first created. /
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        log = (TextView) findViewById(R.id.log);
        uploadBtn = (Button) findViewById(R.id.upload);
        handler = new SocketHandler();
    }

    public void clickUpload(View view) {
        uploadBtn.setClickable(false);
        log.append("开始上传！\n");
        new Thread() {
            public void run() {
                String str = getContentFromDB();
                socketConnect(1, str);
           }
        }.start();
    }

    public void clickClearLog(View view) {
        log.setText("日志");
    }

    private void appendLog(String log) {
        handler.sendMessage(handler.obtainMessage(LOG_APPEND, log));
    }
    
    /* 读取通讯录
    *  @return
    */
    private String getContentFromDB() {
    try {
        appendLog("开始读取通讯录！\n");
        int personCount = 0;
        StringBuffer sb = new StringBuffer();
        Cursor cursor = getContentResolver().query(
        ContactsContract.Contacts.CONTENT_URI, null, null, null,null);
        while (cursor.moveToNext()) {
            personCount++;
            String contactId = cursor.getString(cursor.getColumnIndex(ContactsContract.Contacts._ID));
            int hasPhone = cursor.getInt(cursor.getColumnIndex(ContactsContract.Contacts.HAS_PHONE_NUMBER));
            String name = cursor.getString(cursor.getColumnIndex(ContactsContract.Contacts.DISPLAY_NAME));
            sb.append("{name:"").append(name).append(""");
            if (hasPhone == 1) {
                Cursor phones = getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI,
    null, ContactsContract.CommonDataKinds.Phone.CONTACT_ID + " = " + contactId, null, null);
    sb.append(",phones:[");
        while (phones.moveToNext()) {
            String phoneNumber = phones.getString(phones.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER));
            sb.append(phoneNumber).append(",");
    }
        sb.deleteCharAt(sb.length() - 1);
        sb.append("]}");
        phones.close();
    } else if (hasPhone == 0) {
        sb.append("}");
    }
    }
        cursor.close();
        appendLog("共读取" + personCount + "个联系人数据。\n");
        return sb.toString();
    } catch (Exception e) {
        appendLog("联系人数据读取失败！");
        e.printStackTrace();
        return null;
    }
    }
    
    
    
    private void socketConnect(int type, String str) {
    
    sc = new SocketConnect() {
    @Override
    public void onResponse(byte[] array) {
    try {
    String str = new String(array, "utf-8");
    appendLog(str);
    } catch (Exception e) {
    e.printStackTrace();
    }
    }

    @Override
    public void onLog(String str) {
    appendLog(str);
    }

    @Override
    public void onColse() {
    uploadBtn.setClickable(true);
    }

    };
    
    sc.sendRequest(type, str);
    
    }

    private static final int LOG_APPEND = 1;

    class SocketHandler extends Handler {
        public void handleMessage(Message msg) {
            switch (msg.what) {
            case LOG_APPEND:
            log.append((String) msg.obj);
            break;
            }
        }
    }
    }

## 第二部分：Socket代码
这一部分其实是 Java 代码，主要实现了 Socket 的连接的建立和数据的传输。

    package com.binkery;
    
    import java.io.ByteArrayOutputStream;
    import java.io.DataInputStream;
    import java.io.DataOutputStream;
    import java.net.Socket;
    import java.util.Timer;
    import java.util.TimerTask;
    
    public abstract class SocketConnect {
    
    private static final String IP = "10.78.140.143";
    // private static final String IP = "10.122.22.118";
    private static final int PORT = 9527;
    
    private Socket socket;
    private DataOutputStream dos;
    private DataInputStream dis;
    private ByteArrayOutputStream baos;
    private int curDataLen;
    private Timer timer;
    
    public SocketConnect() {
    try {
    onLog("开始建立连接\n");
    socket = new Socket(IP, PORT);
    dos = new DataOutputStream(socket.getOutputStream());
    dis = new DataInputStream(socket.getInputStream());
    timer = new Timer();
    onLog("建立连接完成\n");
    } catch (Exception e) {
    e.printStackTrace();
    }
    }
    
    public void sendRequest(final int type, final String str) {
    onLog("计时器开始工作\n");
    timer.schedule(new SocketTimeTast(), 3000, 3000);
    
    new Thread() {
    
    public void run() {
    try {
    onLog("开始写数据！\n");
    dos.writeInt(type);
    dos.writeUTF(str);
    
    baos = new ByteArrayOutputStream();
    onLog("开始读数据！\n");
    while (true) {
    int rsp = dis.read();
    if (rsp == -1) {
    break;
    }
    baos.write(rsp);
    }
    onLog("接收数据完成\n");
    onResponse(baos.toByteArray());
    close();
    } catch (Exception e) {
    e.printStackTrace();
    }
    }
    }.start();
    
    }
    
    public void close() {
    onLog("回收资源。\n");
    try {
    dos.close();
    dos = null;
    dis.close();
    dis = null;
    socket.close();
    socket = null;
    timer.cancel();
    timer = null;
    } catch (Exception e) {
    onLog("回收资源出错。\n");
    e.printStackTrace();
    }
    onColse();
    }
    
    public abstract void onResponse(byte[] array);
    public abstract void onLog(String str);
    public abstract void onColse();
    
    class SocketTimeTast extends TimerTask{
    
    @Override
    public void run() {
    onLog("计时到。\n");
    if(socket.isClosed()){
    return;
    }
    onLog("连接未关闭。\n");
    if(baos.size() > curDataLen){
    onLog("有数据接收，字节数：" + baos.size() + "\n");
    curDataLen = baos.size();
    return;
    }
    onLog("应该关闭。\n");
    close();
    }
    
    }
    
    }

## 第三部分：XML代码
XML 代码很简单，就那么几个控件。

    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:orientation="vertical">
        <Button
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:text="上传"
            android:id="@+id/upload"
            android:onClick="clickUpload"  />

    <ScrollView
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:layout_weight="1">

    <TextView
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="日志："
        android:id="@+id/log"   />
    </ScrollView>
    
    <Button
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="清除日志"
        android:id="@+id/clearlog"
        android:onClick="clickClearLog"  />
    </LinearLayout>