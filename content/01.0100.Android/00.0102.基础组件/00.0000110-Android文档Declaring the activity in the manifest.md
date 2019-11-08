# Android文档Declaring the activity in the manifest
- Android,activity,翻译,中文,英文,官方文档,

## Declaring the activity in the manifest

### 在manifest里声明activity

You must declare your activity in the manifest file in order for it to be accessible（容易进入的） to the system. To decalare your activity, open your manifest file and add an \<activity\> element as a child of the \<application\> element.

每一个activity都必须在项目的manifest里声明。这样的作用是Android出于系统的效率考虑的。 

    <manifest ... > 
    <application ... >
    <activity android:name=".ExampleActivity" /> 
    ... 
    </application ... > 
    ... 
    </manifest >

Activity元素里，有很多可用的标签。

There are several other attributes（属性） that you can include in this element, to define properties（属性） such as the label for the activity, an icon for the activity, or a theme（主题） to style（样式） the activity's UI. See the \<activity\> element reference（参考） for more information about available（可用的） attributes（属性）.

### Using intent filters 使用intent过滤器

intent-filter的作用。

An \<activity\> element can also specify（列举） various（不同的） intent filters—using the \<intent-filter\> element—in order to declare how other application components（部件） may activate（激活） it.
binkery:当你使用Android SDK创建一个应用的时候，自动生成的activity的子类已经包含了一个intent-filter。

When you create a new application using the Android SDK tools, the stub activity that's created for you automatically（自动的） includes an intent filter that declares the activity responds to the "main" action and should be placed in the "launcher" category（分类）. The intent filter looks like this:

    <activity android:name=".ExampleActivity" android:icon="@drawable/app_icon">
    <intent-filter>
    <action android:name="android.intent.action.MAIN" />
    <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    </activity>

Binkery:这两行intent-filter的简单解释

The \<action\> element specifies（指定） that this is the "main" entry（入口） point to the application. The \<category\> element specifies that this activity should be listed in the system's application launcher (to allow users to launch this activity).
Binkery:如果你的应用是独立的话，你也许不需要intent-filter。你可以使用显示的方式来启动你的activity。

If you intend（打算） for your application to be self-contained（独立的） and not allow other applications to activate its activities, then you don't need any other intent filters. Only one activity should have the "main" action and "launcher" category, as in the previous（之前的） example. Activities that you don't want to make available（可用的） to other applications should have no intent filters and you can start them yourself using explicit（明确的） intents (as discussed（讨论） in the following section).
Binkery:如果你的应用打算和其他的应用进行交互的话，可以通过增加intent-filter来实现。

However, if you want your activity to respond to implicit（隐式的） intents that are delivered（传递） from other applications (and your own), then you must define additional（附件的） intent filters for your activity. For each type of intent to which you want to respond, you must include an <intent-filter> that includes an <action> element and, optionally（可选的）, a <category> element and/or a <data> element. These elements specify（指定） the type of intent to which your activity can respond.

For more information about how your activities can respond to intents, see the Intents and Intent Filters document.
