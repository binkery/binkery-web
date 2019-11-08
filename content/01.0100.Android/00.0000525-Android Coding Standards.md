# Android Coding Standards
- Android,编码规范


这里总结我自己在编程中的一些习惯，当然，个人习惯最终是要服从于团队规范的。

0. 个人习惯服从于团队规范
1. 成员变量以 m 开头，表示成员变量 member
2. 常量：只要是 static final 的，就必须全大写；只要不是 static final 的，必须不能全大写
3. 一般 View 的成员变量在变量名的最后添加一个 View / Layout / Bar 

  比如 mNameView , mLogoView , mPatientInfoLayout ， mStatusBar。这样 mNameView 和 mName 很容易区分开。

4. 能 private 的不要 public ，尽量控制访问权限
5. Context，Activity 千万千万不要 static
6. 在给方法，成员变量，类命名的时候，尽量不要包含 new 。

  比如你写了一个数据库查询的方法 query() , 一段时间后重构，你又写了一个更好用的方法 newQuery() 。为了区分老的 query ，你加了一个 new 。结果在 N 久之后，又增加了一个更好用的方法，不好意思写成 newNewQuery() ，于是你给起名叫 superQuery() 。但是新加入的成员不知道历史，一看见有新的干嘛不用新的，用完之后还挨一顿臭骂。
