# python 字符串格式化
- python,string,
- 2019.02.27

python 有强大的字符串处理能力和语法，其实主要还是语法。


## format 支持字典

以前在做字符串 format 的时候，我经常这样子使用：

    name = ''
    age = ''
    '{name} is {age}'.format(name=name,age=age)

对于比较短的字符串还好，但是我一般都用它来生成 html 页面。字符串的长度是很长的，结果就是 format 的参数异常的多。我觉得肯定有解决的办法的，我尝试了用字典的方式，结果证明是可行的。

    user['name'] = ''
    user['age'] = ''
    '{user[name]} is {user[age]}'.format(user=user)

这样 format 参数就简洁了很多。
