# SpannableString 与 SpannableStringBuilder
- 2016-03-21 09:53:06
- Android
- 

<!--markdown-->SpannableString 和 SpannableStringBuilder 让 TextView 可以展示富文本。SpannableString 和 SpannableStringBuilder 分别对应 String 和 StringBuilder 。

在项目中可能会碰见这种需求：产品给一个文案，一般来说用一个 TextView 就搞定了，但是如果文案中有几个字符需要特殊处理，比如改变颜色，变成粗体。那么好像是很麻烦，其实 TextView 以及能处理这种需求了，只是不能简单的使用 String 而已。

SpannableString 与 SpannableStringBuilder 是处理这种需求的一种方式。

首先，TextView.setText(CharSequence text) ，传的不是 String，而是 String 的父类 CharSequence，CharSequence 是一个接口，String 是它最常见的子类，咱们用习惯了，不要以为 setText 接受的参数是　String　类型。

咱们看看　String，StringBuilder，SpannableString　和　SpannableStringBuilder　的定义

    public final class String implements Serializable, Comparable<String>, CharSequence{}

    public final class StringBuilder extends AbstractStringBuilder implements　Appendable, CharSequence, Serializable{}

    public class SpannableString　extends SpannableStringInternal　implements CharSequence, GetChars, Spannable{}

    public class SpannableStringBuilder implements CharSequence, GetChars, Spannable, Editable,Appendable, GraphicsOperations{}

首先可以肯定的是他们都是 CharSequence 的子类，实现类。SpannableString 和 SpannableStringBuilder 都实现了一个叫 Spannable 的接口。SpannableStringBuilder 和 StringBuilder 类似，都实现了 Appendable 接口，也就是 SpannableStringBuilder 可以像 StringBuilder 一样，使用 append() 方法。

咱们再回到 Spannable 接口，这个接口有一个重要的方法：

    public void setSpan(Object what, int start, int end, int flags);

参数说明：

what ： 是一个样式，下面具体说明

start ： 开始的位置

end ： 结束的位置

flags ： 标志，取值有以下几种


    Spannable.SPAN_EXCLUSIVE_EXCLUSIVE ：前后都不包括 = ()
    Spannable.SPAN_EXCLUSIVE_INCLUSIVE ：前面不包括，后面包括 = (]
    Spannable.SPAN_INCLUSIVE_EXCLUSIVE ：前面包括，后面不包括 = [)
    Spannable.SPAN_INCLUSIVE_INCLUSIVE ：前后都包括 = []

什么意思呢？比如说现在有个字符串，ABBC，现在要求两个 B 的颜色要红色，what 传的是一个改变字体颜色的对象，start 就是 1，end 是 2，flags 的不同体现在当 在 A 和 B 直接或者 B 和 C 直接要插入一个 D，那么这个 D 的颜色是否需要和 B 的颜色一样，就取决为 flags 传的是哪个参数了。

为什么还能插入 D ？有这种需求吗？别忘了，EditText 的父类是 TextView。你完全可以做一个即见即得的文本编辑器，只是可能没人喜欢在手持设备上那么用而已。

然后咱们再来看看那个 what 都可以传什么样的对象。

在 android.text.style 包下面，有 N 多个 XxxxSpan 类，所有这些类都是可用的。
比如说 

 * BackgroundColorSpan 背景颜色
 * ForegroundColorSpan 字体颜色
 * UnderlineSpan 下划线
 * ...

他们都是继承于 android.text.style.CharacterStyle，CharacterStyle 是一个抽象类，有个抽象方法 updateDrawState(TextPaint tp)，你完全可以自定义一个样式，人家已经把画笔给你了。