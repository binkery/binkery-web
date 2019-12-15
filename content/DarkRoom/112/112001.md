# Android WebView 不支持 H5 input type="file" 解决方法
- Android,WebView,HTML5,input,file
- 2018.03.06

默认的 Andorid WebView 是不支持 input type="file" 这种标签的用法的，但是我们在平时开发中却又是经常碰见这样的需求的。

在应用内嵌 HTML5 页面是很常见，一般情况下，HTML5 页面比较适合做一些业务说明，介绍或者展示等简单的功能，比较复杂的话，可能需要做一些表单的提交。

表单提交的话，input type=file 算是比较麻烦的。出于安全的问题，webview 默认并不会主动弹出文件选择器，不过 Android 还是为我们预留出一些 api 来，我们可以进行一定的扩展和自由发挥。

但是这样的 api 又有版本的变化，适配变得比较麻烦了。下面简单贴出大概的代码。

## 弹出文件选择器

下面的代码展示如何接收 file type=file 控件的点击事件。这里唤起的是系统默认的文件选择器，你也完全可以启动自己项目里实现的文件选择器，或者图片选择器之类的。这里的重点是需要重写 WebChromeClient 的几个方法。

    webview.setWebChromeClient(new WebChromeClient(){

        // For 3.0+ Devices (Start)
        // onActivityResult attached before constructor
        protected void openFileChooser(ValueCallback uploadMsg, String acceptType){
            Intent i = new Intent(Intent.ACTION_GET_CONTENT);
            i.addCategory(Intent.CATEGORY_OPENABLE);
            i.setType("image/*");
            startActivityForResult(Intent.createChooser(i, "File Browser"), FILECHOOSER_RESULTCODE);
        }


        // For Lollipop 5.0+ Devices
        @TargetApi(Build.VERSION_CODES.LOLLIPOP)
        public boolean onShowFileChooser(WebView mWebView, ValueCallback<Uri[]> filePathCallback, WebChromeClient.FileChooserParams fileChooserParams){
            Intent intent = fileChooserParams.createIntent();
            try{
                startActivityForResult(intent, REQUEST_SELECT_FILE);
            } catch (ActivityNotFoundException e){
                return false;
            }
            return true;
        }

        //For Android 4.1 only
        protected void openFileChooser(ValueCallback<Uri> uploadMsg, String acceptType, String capture){
            Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
            intent.addCategory(Intent.CATEGORY_OPENABLE);
            intent.setType("image/*");
            startActivityForResult(Intent.createChooser(intent, "File Browser"), FILECHOOSER_RESULTCODE);
        }

        protected void openFileChooser(ValueCallback<Uri> uploadMsg){
            Intent i = new Intent(Intent.ACTION_GET_CONTENT);
            i.addCategory(Intent.CATEGORY_OPENABLE);
            i.setType("image/*");
            startActivityForResult(Intent.createChooser(i, "File Chooser"), FILECHOOSER_RESULTCODE);
        }

    });

## 接收选择结果

这里是唤起系统文件选择器后，用来接收 result intent。不同的版本略有不同。如果你唤起的是你自己应用的 Activity，处理也是相似的。不过最终，你都是需要通过一个 ValueCallback<Uri> 把用户选择的文件的 Uri 回调给 webview，HTML 才会收到这个文件的路径。

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent intent){

        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP){
            if (requestCode == REQUEST_SELECT_FILE){
                uploadMessage.onReceiveValue(WebChromeClient.FileChooserParams.parseResult(resultCode, intent));
            }
        }else if (requestCode == FILECHOOSER_RESULTCODE){
            // Use MainActivity.RESULT_OK if you're implementing WebView inside Fragment
            // Use RESULT_OK only if you're implementing WebView inside an Activity
            Uri result = intent == null || resultCode != MainActivity.RESULT_OK ? null : intent.getData();
            mUploadMessage.onReceiveValue(result);
        }else{

        }
    }

## 个人建议

这个方式实现，可以让 HTML 具有更高的适配性，可以在其他的浏览器中使用，实现了一次编写，到处部署，到处运行的效果。但是这个方式在混合编程确实还是有一些适配的问题，需要花些经历去解决。

现在也有很成熟的 webview 桥接技术，推荐开发团队可以考虑试用一下。
