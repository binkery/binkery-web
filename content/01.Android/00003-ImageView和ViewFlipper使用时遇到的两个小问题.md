# ImageView 和 ViewFlipper 使用时遇到的两个宽高问题
- 2015-03-06 03:29:10
- Android
- Android,ImageView,ViewFilpper,宽高问题,Android 开发


前段时间遇到个问题，当 ImageView 宽度设为 fill_parent ，高度设为 wrap_content 时，我希望图片能根据宽度等比缩放，然后 ImageView 的高度再根据图片本身的高度得出，但是结果却不是我想的那样。ImageView 的上下方都会出现一段空白。试了各种 scaletype 都无法实现这个设计。后来从网上去找，发现原来解决这个问题的答案非常简单，那就是设置 ImageView 的属性adjustViewBounds 为 true，即在 ImageView 的 xml 中加入 android:adjustViewBounds="true"。


之后又遇到了一个新的问题，由于 ViewFlipper 的一个子 view 是这个 ImageView ， ViewFilpper 在切换时，高度总是为子 View 中高度最大的值作为其高度值。后经搜索，发现需要设置 android:measureAllChildren="false" 即可。

两个问题在我的一个项目中的遇到了，小纠结了一小会。试着通过改变布局的权重来解决问题，但是最后都没有解决。通过上面的方法，一下子搞定了问题。
