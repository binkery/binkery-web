# Improving Stability by Reducing Usage of non-SDK Interfaces
- Android
- 2018.03.02

Android 为了提高稳定性，增加了对非 SDK api 使用的限制。这是一遍来自官方的说明文档。

In Android, we're always looking for ways to improve the user and developer experience by making those experiences as stable as possible. In this spirit, we've been working to ensure that apps don't use non-SDK interfaces, since doing so risks crashes for users and emergency rollouts for developers. In Android N, we restricted the set of symbols that C/C++ code could use. This change ensured that apps using C++ rely on stable NDK interfaces rather than incur the incremental crashes caused by reliance on unstable, non-NDK interfaces. Starting in the next release of Android, we will further increase stability by expanding these restrictions to cover the Java language interfaces of the SDK.

在 Android N 版本中，Google 已经在 NDK 做了一些限制，限制 c/c++ 调用非 API 的接口。在下一个版本中，这个范围会扩大到 Java 层中。

## What behavior will I see?

Starting in the next release of Android, some non-SDK methods and fields will be restricted so that you cannot access them -- either directly, via reflection, or JNI. If you try, you can see errors such as NoSuchFieldException or NoSuchMethodException.

在下一个 release 版本中，非 SDK 的方法和字段将会被显示访问，包括直接调用，反射，JNI 等方式。相应的，会抛出 NoSuchFieldException 和 NoSuchMethodException 异常。

Initially, this restriction will impact interfaces with low or no usage. It is an explicit goal of our planning and design to respect our developer community and create the absolute minimum of change while addressing app stability issues flagged by our users and device manufacturers. In cases where a migration to SDK methods will be possible but is likely to be technically challenging, we'll allow continued usage until your app is updated to target the latest API level. We plan to broaden these restrictions in future platform versions, giving developers time to migrate with long advance warning, and also giving us time to gather feedback about any needed SDK interfaces. We have always said that using non-SDK interfaces is always risky -- they might change in any release as we refactor code to add features or fix bugs. So if your app currently relies on non-SDK interfaces, you should begin planning a migration to SDK alternatives.

和之前的一些重要的更新一样，只有当你的 target sdk version 升级到对应的版本，才会开启这样的限制，在此之前，你的应用同样可以正常的运行在新的 Android 系统中。但是这样的限制会是以后长期的一个制度，这一天早晚都会到来的，只是时间问题。现在你还有不少时间来适应这个变化。

Because the Java language has different features from C++, this restriction will take a slightly different form than the previous symbol restriction. You should not access classes that are not part of our SDK, but you also need to be sure that you are only using the officially documented parts of each class. In particular, this means that you should not plan to access methods or fields that are not listed in the SDK when you interact with a class via semantics such as reflection.

## What if there isn't a SDK alternative?

We know that some apps may be using non-SDK interfaces in ways that do not have an SDK alternative. We value your feedback about where and how we need to expand and improve the public APIs for you. If you feel that you'll need the SDK API expanded before you can stop using non-SDK ones, please tell us via our bug tracker. We will be monitoring this list closely and using this valuable feedback to prioritize. It is critical for us to get this feedback in a timely manner so that we can continue to both tune the blacklist to minimize developer impact and also begin developing any needed alternatives for future platforms.

## What's coming next?

In the next Android developer preview, you'll be able to run your existing apps and see warnings when you use a non-SDK interface that will be subject to blacklist or greylist in the final release. It's always a best practice to make sure your app runs on the developer preview, but you should pay specific attention to the interface compatibility warnings if you are concerned that you may be impacted.

在下一个开发者预览版中，你可以运行你的应用，并且提供黑名单和灰名单的机制，以便你发现警告。

In conjunction with the next developer preview and the new bug tracker category, we'll be monitoring usage of non-SDK interfaces. In cases where official SDK alternatives already exist, we'll publish official guidance on how to migrate away from commonly used non-SDK interfaces.

在最后官方版本发布的时候，Android 会提供官方的引导文档，教你如何过度。
