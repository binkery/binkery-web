# 开发工具之 SQLiteBorwser
- android,ubuntu,sqlite,
- 2014-12-16 09:48:20


SQLite 是一个很轻量级的数据库，Android 也是采用这样的数据库。SQLiteBorwser 是一款在 ubuntu 上运行的优秀的 SQLite 数据库文件查看修改的工具。可以打开从 Android 项目里拽出来的数据文件，也可以创建数据库并保存成文件，导入到 Android 项目里使用。是辅助开发的一个利器。


安装：

    sudo apt-get install sqlitebrowser



- 打开已有数据库文件或者新建数据并保存为数据库文件。

- create / modify / delete table 可以对表结构进行修改，完全可视化，简单明了，老少皆宜。

- create / delete index 创建/删除索引

- Database Structure 可以查看数据库的表结构，表的名字，各字段的名字和数据类型都可以很直观的看到。

- Browse Data 可以查看每张表下面的数据，每页默认最多显示1000行，可以很方便的查看表内的具体数据。

- Execute SQL 可以执行编写的 sql 语言，并且把执行后的结果显示出来。