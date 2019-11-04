# Git 查看两次 commit 之间的变更
- 2015-03-06 09:35:42
- 操作系统与开发环境
- Git,命令行
- git diff,git 命令行,git diff commit,
- 在 git 中，如果我们要比较两次 commit 之间的所有变更，我们可以通过 git diff commit-id-1 commit-id-2 来查看 。

通过 *git diff --help* 查询 git 帮助文档可看到

    git diff [--options] <commit> <commit> [--] [<path>...]

这个是 diff 两个 commit 之间的变更, <commit> 是 commit 的 ID 号，可以通过 *git log* 查看。获取到两个 commit 的 ID 号后，就可以查看两个 commit 变更的内容了。

    git diff commit-id-1 commit-id-2 

或者可以输出到文件里：

    git diff commit-id-1 commit-id-2 >> diff.txt

