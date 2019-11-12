# Git push and delete remote branches
- git,branch,
- 2014-08-01 12:57:14


This is an action that many Git users need to do frequently, but many (including the author) have forgotten how to do so or simply don’t know how. Here’s the definitive guide if you’ve forgotten.

So let’s say you have&nbsp;checked out a new branch, committed some awesome changes, but now you need to share this branch though with another developer. You can push the branch up to a remote very simply:
<blockquote><code>git push origin newfeature</code></blockquote>
Where&nbsp;<code>origin</code>&nbsp;is your remote name and&nbsp;<code>newfeature</code>&nbsp;is the name of the branch you want to push up. This is by far the easiest way, but there’s another way if you want a different option.&nbsp;Geoff Lanehas created a&nbsp;great tutorial&nbsp;which goes over how to push a ref to a remote repository, fetch any updates, and then start tracking the branch.

Deleting is also a pretty simple task (despite it feeling a bit kludgy):
<blockquote><code>git push origin :newfeature</code></blockquote>
That will delete the&nbsp;<code>newfeature</code>&nbsp;branch on the&nbsp;<code>origin</code>&nbsp;remote, but you’ll still need to delete the branch locally with&nbsp;<code>git branch -d newfeature</code>.

There’s a script called&nbsp;git-publish-branch&nbsp;created by&nbsp;William Morgan&nbsp;that can easily automate this process if you find yourself performing these actions frequently. It also makes deleting remote branches feel a bit more natural. Know of better or easier ways to do the above tasks? Let us know in the comments or&nbsp;submit your own tip!