# Android 网络编程之 HttpClient
- 2016-03-22 07:22:25
- Android
- android,http,网络编程,

<!--markdown-->HttpClient 是由 APACHE 提供的一套 API ，Google 把它们都加入到了 Android 的 SDK 里了。这一套 API 做了很丰富的封装，在使用的过程中你就可以发现，这套 API 安装 Java 面向对象的思想，对 HTTP 请求中的各个环节都做了封装，比如 GET 请求有 HttpGet ，POST 请求是 HttpPost 。这样是很符合 Java 面向对象的特点，而且扩展性也很好。但是这套被 Google 加入 Android 豪华午餐的 API 并没有受到很好的支持，Android 也推荐使用 HttpURLConnection 而不是这套 API。

<!--more-->

下面简单介绍一下 HttpClient 的用法。


 ### GET 请求代码

    String baseUrl = "http://tech.binkery.com/login.php?user=user&password=password"; 
    HttpGet httpGet = new HttpGet(baseUrl + "?" + param); 
    HttpClient httpClient = new DefaultHttpClient();  
    try {  
        HttpResponse response = httpClient.execute(httpGet);
    } catch (ClientProtocolException e) {  
        e.printStackTrace();  
    } catch (IOException e) {  
        e.printStackTrace();  
    }  


 ### POST 请求代码

    List<BasicNameValuePair> params = new LinkedList<BasicNameValuePair>(); 
    params.add(new BasicNameValuePair("user", "user"));  
    params.add(new BasicNameValuePair("password", "password"));  
    String baseUrl = "http://tech.binkery.com/login.php"; 
    HttpClient httpClient = new DefaultHttpClient(); 
    try {  
        HttpPost httpPost = new HttpPost(baseUrl);  
        httpPost.setEntity(new UrlEncodedFormEntity(params, "utf-8")); 
        HttpResponse response = httpClient.execute(httpPost);
    } catch (UnsupportedEncodingException e) {  
        e.printStackTrace();  
    } catch (ClientProtocolException e) {  
        e.printStackTrace();  
    } catch (IOException e) {  
        e.printStackTrace();  
    }  



 ### 一些需要注意的知识点

 - GET 请求，参数可以直接拼接到 URL 的后面，但是如果参数的内容由用户输入的话，你可不能保证那个熊孩子会给你输入些啥玩意，空格啊，中文啊，火星文啊。所以如果需要更加健壮的代码，那就需要多费点功夫了。大概是这个样子：

    List<BasicNameValuePair> params = new LinkedList<BasicNameValuePair>();  
    params.add(new BasicNameValuePair("user", "user"));  
    params.add(new BasicNameValuePair("password", "password"));  
    String param = URLEncodedUtils.format(params, "UTF-8");  

 - POST 请求，通过 HttpPost.setEntity 来 POST 数据。你可以选择任何的 HttpEntity 的子类，也可以自己扩展，当然提供的已经够用了。
 - HttpGet 和 HttpPost 都是 HttpUriRequest 的子类。
 - HttpClient.execute() 就是执行请求。返回一个 HttpResponse .
 - HttpResponse 的主要方法
   - StatusLine getStatusLine() // response.getStatusLine().getStatusCode() == 200
   - Header[] getAllHeaders()
   - HttpEntity getEntity()
 - 一般使用 NameValuePair 的子类 BaseNameValuePair(String name , String value) 来存放每个键值对参数。并且把所有键值对放在一个容器里 -- List<NameValuePair> ，然后通过new UrlDecodedFormEntity(List<NameValuePair>) 创建一个 HttpEntity 的实例，并通过 HttpPost.setEntity(HttpEntity) 来设置 POST 的数据。
 - 通过 HttpResponse.getEntity() 可以获取到一个 HttpEntity 的对象，我们可以使用 EntityUtils 这个工具类来获取我们想要的数据。主要的方法有：
    - public static byte[] toByteArray(HttpEntity entity)
    - public static String toString(HttpEntity entity)
    - public static String toString(HttpEntity entity , String encoding)
