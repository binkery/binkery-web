# Java 基础之 Integer
- Java,基础,Integer

int 是 Java 中的八大基本数据类型之一，对应的封装类是 java.lang.Integer。

Java 的自动装箱和自动拆箱功能，让 int 和 Integer 可以互换。

尽量使用 Integer.valueOf(int) 方法来获取一个 Integer 对象，而不使用 new Integer(int) 来构造 Integer 对象。

Java 有两种数据类型，一种是基本数据类型，一种是引用类型。int 就是 Java 的一种基本数据类型，Integer 是 int 的封装类，位于 java.lang 包下。

Integer 作为 int 的封装类，肯定是封装了一些跟 int 运算处理有关的方法。那么在使用的过程中，就会有这样的问题，int 是比较常用的基本数据类型，在程序中，你可能需要很多的 int 类型的参数或者变量。Java 又是一个面向对象的语言，所以会尽可能的希望你使用 Integer 而不是 int ,特别是 Integer 提供了一些现成的方法，再加上自从 Java 5.0 后，Java 加入了基本数据类型的自动装箱功能 autoboxing , 就是在必要的时候，自动把一个 int 变成一个 Integer 对象。这样子就会导致运行时中，存在很多的 Integer 对象，引用类型肯定是比基本数据类型占用内存的。为了减少不必要的内存消耗，和内存开辟的次数，Integer 里做了一个缓存，缓存了从 -128 到 127 之间的 Integer 对象，总共是256个对象。

代码其实很简单，下面是从源代码复制过来的。

    //如果在 -128 到 127 之间的话，返回缓存内的对象，否则实例化一个对象。
    public static Integer valueOf(int i) {
        return  i >= 128 || i < -128 ? new Integer(i) : SMALL_VALUES[i + 128];
    }

    private static final Integer[] SMALL_VALUES = new Integer[256];

    // 类加载的时候就初始化这 256 个对象。
    static {
        for (int i = -128; i < 128; i++) {
            SMALL_VALUES[i + 128] = new Integer(i);
        }
    }

    // equals 比较的还是数值本身，不是对象。
    public boolean equals(Object o) {
        return (o instanceof Integer) && (((Integer) o).value == value);
    }

这个小细节可能本身没有太多的作用，平时也少会需要关注到它，但是这个却给我们一些启发，或者一些思考，加深对 Java 的一些理解。
 - Integer 对象肯定比 int 更占内存
 - 即使一个对象的内存开销不是很大，但是频繁的实例化对象，开辟内存，也给系统造成一定的资源浪费
 - 实例化 Integer 尽量使用 Integer.valueOf(int) ，而不用 new Integer(int)
 - 既然 Integer 里有了这么一个缓存，那我们在定义常量，变量的时候，就可以放心地使用，并且从设计上，也可以考虑尽量使用缓存范围内的数值。比如在定义常量的时候，有人喜欢 0,1,2,3,4... 这么定义，有人喜欢 0,1,2,4,8,16 ... 这么定义。当然最后还得看项目的具体需求，别捡了芝麻掉了西瓜，毕竟这点小小的东西作用不是那么特别重要。
 - 在你设计自定义的类型的时候，必要的时候可以参考一些这个思路，做一个简单的缓存，而不一定每次都通过实例化。
 - Integer 的缓存使用了一个定长的数组，看起来好像很不灵活，不过估计 Java 认为，如果再复杂一些的话，消耗就大于收益了。
