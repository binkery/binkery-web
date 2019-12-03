# 页面内容不足以铺满屏幕高度时，footer 居底显示
- CSS,HTML,前端
- 2018.08.06

在有些网页内容比较少的时候,经常会出现不满一屏的情况。为了让页面看上去更加好看一些，就需要让网页自动铺满，让底部显示在屏幕的最下方。

在项目中常常会遇到这样的问题：页面主要内容不足以铺满一个屏幕的高度，footer 下面就会有白块剩余。

现在要实现的效果就是，在主要内容不足以铺满整个屏幕的情况下，footer 居于屏幕低部显示，使得整个页面占满屏幕。而当主要内容高度大于整个屏幕高度的时候，footer 跟随主要内容进行显示。

## html 代码部分

    <div class="page">
        主要页面
    </div>
    <footer>底部</footer>

## CSS 代码部分

    html,body{
        height: 100%;
        margin: 0;
        padding: 0;
    }
    .page{
        box-sizing: border-box;/*为元素指定的任何内边距和边框都将在已设定的宽度和高度内进行绘制*/
        min-height: 100%;
        padding-bottom: 300px;
    }
    footer{
        height: 300px;
        margin-top: -300px;
        opacity: 0.5;
    }


主要内容放在 page 内部，page 最小高度为100%（注意这里html，body高度也要设为100%）。page 有个 padding-bottom 大小为 footer 的高度（按需要调整），最重要的一点 page 的 box-sizing:border-box，为元素指定的任何内边距和边框都将在已设定的宽度和高度内进行绘制，也就是说 page 的 padding-bottom 也会设定在 min-height：100% 内。而 footer 的 margin-top 为负的自身高度，把自己拉到 page 的 padding-bottom 空白块上，从而达到需求效果。

优点：简洁明了，没有冗余的 div 盒子；

缺点：box-sizing:border-box 的兼容问题，ie7 以下包括 ie7 不支持。ie 就是一个奇葩的存在。
