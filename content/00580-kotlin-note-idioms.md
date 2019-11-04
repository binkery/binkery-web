# Kotlin 自学笔记 - Idioms 代码风格
- 2019.05.01
- Kotlin
- Kotlin
- Kotlin自学笔记,Kotlin代码风格,Kotlin学习笔记

## 创建 DTOs（POJOs/POCOs）

    data class Customer(val name:String,val email:String)
    
  在 Kotlin 中，创建各种实体还是很简单的，上面的代码创建了一个 Customer 类，并且拥有下面的方法。
  
  - getters 方法，如果定义的是 var 的话，还有对应的 setters 方法
  - equals() 
  - hashCode()
  - toString()
  - copy()
  - componenet1(),component2(),... 这个暂时不知道是什么意思
  
  ## 方法参数的默认值 default values for function parameters
  
  这个是 Java 没有的功能，Java 中是通过重载来实现这个功能的。
  
      fun foo(a :Int = 0 , b:String = "") {}
      
 ## 过滤列表 Filtering a list
 
    val positives = list.filter {x-> x>0 }
    val positives = list.filter {it > 0 }

## 字符串插入 string interpolation

这个功能会，在字符串的处理上，让 Kotlin 的代码变得更加的高效简洁。

    println("Name is $name")

## 类型检测 instance checks

    when(x){
        is Foo -> ...
        is Bar -> ...
        else -> ...
    }
    
## 遍历 Map/List traversing a map/list of pairs

    for((k,v) in map){
        println("$v -> $v")
    }
    
 **k** 和 **v** 可以是任何类型。
 
 ## 数组跨度 Using Ranges
 
 两个点 .. 是 kotlin 的一个特殊代码风格，会让代码更加简洁
 
    for(i in 1..100){ ... }
    for(i in 1 until 100 ){ ... }
    for(x in 2..10 step 2){  .... }
    for(x in 20 downTo 1){ ... }
    if(x in 1..10){ ... }
  
 ## 只读的列表，只读的 Map Read-only list / Read-only map

    val list = listOf("a","b","c")
    val map = mapOf("a" to 1, "b" to 2,"c" to 3) 
 
 只读表示这个容器一旦生成，就不被允许修改。
 
 ## map 的访问
 
    println(map["key"]) // 访问
    map["key"] = value  // 修改
    
## 懒特性 lazy property

    val p: String by lazy{
        // compute the string
    }
    
## 扩展方法

可以扩展一个现有类的方法。

    fun String.spaceToCamelCase(){ ... }
    "Convert this to camelcase".spaceToCamelCase()

## 创建单例

    object Resource{
        val name = "Name"
    }
    
## 非空判断

    val files = File("test").listFiles()
    println(files?.size)
    println(files?.size ?: "empty")
    
## Executing a statement if null

    val values = ...
    val emial = values["email"] ?: throw IllegalStateException("...")

## 获取一个可能为空的集合的第一个元素

    val emails = ...
    val mainEmail = emails.firstOrNull() ?: ""
    
## Execute if not null

    val value = ...
    value?.let{
        ... // 执行这个代码块，如果不为空的话
    }

## map nullable value if not null

    val value = ...
    val mapped = value?.let{
        transformValue(it)
    } ?: defaultValueIsNull

## return on when statement

    fun transform(color:String): Int{
        return when(color){
            "red" -> 0
            "green" -> 1
            "blue" -> 2
            else -> throw IllegalArgumentException("...")
        }
    }


## try catch 表达式 异常捕获 

    fun test(){
        val result = try{
            count()
        }catch(e: ArithmeticException){
            throw IllegalStateException(e)
        }
        // working with result
    ]

## if 表达式

    fun foo(param:Int){
        val result = if(param == 1){
            "one"
        }else if(param == 2){
            "two"
        }  else{
            "there"
        }
    }

在 Kotlin 中，可以认为表达式都是有返回值的，而且表达式的返回值都是这个表达式的最后的值。

## Builder-style usage of methods that return Unit

    fun arrayOfMinusOnes(size:Int):IntArray{
        return IntArray(size).apply{ fill(-1)}
    }
    
## single-expression functions

方法体的简写样式，下面这两种方法是一样的。

    fun theAnswer() = 42
    fun theAnswer():Int {
        return 42
    }
    
这样可以节省很多代码量，配合其他表达式，比如 when ：

    fun transform(color:String):Int = when(color){
        "Red" -> 0
        ...
    }

## 调用一个实例对象的多个方法 calling multiple methods on an object instance (with)

    class Turtle{
        fun penDown()
        fun penUp()
        fun turn(degress:Double)
        fun forward(pixels:Double)
    }

    val turtle = Turtle()
    with(turtle){
        // 这里的几个方法都是 turtle 对象的方法
        penDown()
        for(i in 1..4){
            forward(100.0)
            turn(90.0)
        }
        penUp()
    }

## Java 7 try with resources

    val stream = Files.newInputStream(Paths.get("/some/file.txt"))
    stream.buffered().reader().use{ reader ->
        println(reader.readerText())
    }


Convenient form for a generic function that requires the generic type information


    //  public final class Gson {
    //     ...
    //     public <T> T fromJson(JsonElement json, Class<T> classOfT) throws JsonSyntaxException {
    //     ...

    inline fun <reified T: Any> Gson.fromJson(json: JsonElement): T = this.fromJson(json, T::class.java)


##　使用可能为空的布尔值 Consuming a nullable Boolean

    val b:Boolean? = ...
    if(b == true){
        ..
    }else{
        // 'b' is false or null
    }
    
## 交换两个变量

    var a = 1
    var b = 2
    a = b.also{ b = a}
