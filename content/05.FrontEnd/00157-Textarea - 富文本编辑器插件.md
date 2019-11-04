# Textarea - 富文本编辑器插件
- 2015-03-06 09:40:39
- 前端技术
- textarea,文本编辑器,插件,ueditor,tiny,editor,

<!--markdown-->这个东西很复杂，想想就很复杂，想想就自己不想写。哈哈，javascript可不是我的强项，会很累的，会死人的。所以还是直接抄一个算了。


<!--more-->


网上搜了一下，有很多开源的代码可以使用，各有特色，各有优缺点。所以就选择一个自己喜欢的吧。

看了一下百度的，Ueditor，据说很强大，官网：http://ueditor.baidu.com/website/ ，貌似真的很强大，不过看着头疼，太复杂了，不是我想要的。几分钟内搞不定的，我就选择了放弃。一说明它很复杂，二说明功能太多，三说明代码太多，四说明有代码洁癖的我是不会喜欢的。

另外一个是TinyEditor，http://www.scriptiny.com/ 据说很小很简单，下载完了看了一下，确实是，应该是我喜欢的，而且也在几分钟内搞定了安装了，简单才是硬道理。

刚才安装完测试的时候发现了一个问题，就是再次编辑的时候，更改的内容并没有提交上去。查了一下，原来还需要加几行javascript代码。

    <textarea name="content" id="tinyeditor"></textarea>
    <script>
      var editor = new TINY.editor.edit('editor', {...}
    </script>

上面的代码Tiny官网上的DEMO上有，下面的没有，不过官网有个说明，就是没给代码。就是在提交的时候调用一下post()这个方法。

    <input type="submit" value="保存" onclick="post_commit()" />
    <script>
    function post_commit(){
    editor.post();
    }
    </script>

The first parameter taken by TINY.editor.edit is the variable name used for the object instance. Keep in mind that before posting you will need to call the instance.post() function to ensure that the latest changes in the WYSIWYG translate into the text area. This script has been tested in all major browsers and is available free of charge for both personal or commercial projects under the creative commons license.

问题挺多的。在文本编辑框里，直接显示出了HTML控件，把我郁闷的，找不到问题啊，不在行啊。

最后这样搞定的，在输出的时候转一下。

    <textarea name="content" id="tinyeditor"><?php echo htmlspecialchars($post['content']);?></textarea>