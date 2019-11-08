# Android 网络编程之 HttpURLConnection
- Android,网络编程,

HttpURLConnection 是 Android 平台上常用的网络编程的工具类，相比 HttpClient，HttpURLConnection 得到了 Android 官方很好的支持和推荐。下面是一些简单的介绍和知识的整理。

这是一个简单的使用 HttpURLConnection 进行 GET 请求的代码。

    URL url = new URL("http://tech.binkery.com");
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setConnectTimeout(6*1000);
    if (conn.getResponseCode() != 200){
        InputStream is = conn.getInputStream();
        // do somethings here
    }
    conn.disconnect();

POST 请求：

    URL url = new URL("http://tech.binkery.com");
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setDoOutput(true); 
    conn.setRequestMethod("POST");
    conn.setConnectTimeout(6*1000);
    OutputStream out = conn.getOutputStream();  
    // like as : out.write(byte[] bytes);
    out.close(); 
    if (conn.getResponseCode() != 200){
        InputStream is = conn.getInputStream();
        // do somethings here
    }
    conn.disconnect();

需要注意的点：

 - HttpURLConnection.setRequestProperty(String key,String value) 用来设置 HTTP 请求的头，也就是 HTTP Request Header .

 - HttpURLConnection.setRequestMethod(String) 用来设置 HTTP 请求的发送方式，不设置默认是 GET ， 一般使用全大写的 "GET" 或 "POST" 。

 - HttpURLConnection.setConnectTimeout(long time) 设置超时是很有必要的，单位是毫秒。

 - HttpURLConnection.getResponseCode() 获取返回的 HTTP 状态码，多一层判断，多一层保护。200 表示正常的，其他类似 404 ， 503 之类的，可以根据业务逻辑去判断做不做处理。

 - 一个空格引发的血案。在通过 HttpURLConnection.setRequestProperty(String key,String value); 给请求设置属性的时候，value 里的空格会被转义成 '\s',所以，你可能需要这样子写：
conn.setRequestProperty("Content-Type", ("application/xml; charset=utf-8").replaceAll("\\s", ""));
http://stackoverflow.com/questions/15030201/issues-with-httpurlconnection-with-post-on-android-2-2?rq=1

 - 在使用 POST 的时候，需要发送的数据都被写入到内存里，然后再发送出去(在close()的时候发送)，如果发送的数据太多，很容易占用太多的内存，造成溢出。所以，在明确知道数据的长度的时候，使用 HttpURLConnection.setFixedLengthStreamingMode(int) 设置流的长度，或者不明确知道数据的长度的时候，使用 HttpURLConnection.setChunkedStreamingMode(int) 设置块的大小，这样就能有效的避免的内存溢出了。
