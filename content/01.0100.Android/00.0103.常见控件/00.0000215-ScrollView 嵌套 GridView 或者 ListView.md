# ScrollView 嵌套 GridView 或者 ListView
- Android,listview,gridview,scrollview,

在一些应用中会有这样的需求。在ScrollView里需要嵌套使用GridView或者ListView.

ListView 的话，其实ListView 有 header 可以使用，能满足一部分的需求。但是如果是GridView的话，只能嵌套。

怎么使用网上有很多，主要就是要自定义一个GridView，重写onMeasuer方法。这个能满足需求。但是会有一些问题。

可能网上的例子要满足的需求比较简单，所以没有那么多的问题。但是如果你的GridView里每个item都有很多的内容，不是简单的几个文字，并且你的GridView会有很多很多的items ，并且每个item都比较复杂。那么问题就出现了。

首先，ScrollView 会一直计算它需要占用多少的空间，所以需要算GridView的空间，我这里说的主要是高度，因为需要滚动。GridView计算高度会调用onMeasure这个方法，这个方法会调用GridView绑定的Adapter的bindView方法，结果是bindView方法被一次一次的调用。根据我打印的日志，那叫一个疯狂。

另外，因为上面所说的，GridView的高度被计算出来了，并且给他留了空间了，那么他的每个item都会被现实出来，所以，并不是只在屏幕上看到的item才会被调用bingView。从日志中，你可以看出，bindView会从index 0 到 最后一个，执行一遍。其实意思是说，GridView和他的Adapter没有起到任何作用。这个是我猜测的，但估计应该是这样的。所以这个使用，使用一个GridView和LinearLayout或者其他的Container没什么差别。

所以我认为，使用ScrollView嵌套GridView本身就是一个bug。毕竟android官网也不建议这样使用。

期望以后找到其他的solution。
