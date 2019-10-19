git stash
-------

"stash" any changes in your working directory away and roll back your repository to the `HEAD` commit

~~~ bash
$ git stash
~~~

---

### Useful Options / Examples
Use git stash when you want to keep a record of your changes to your repository/branch, but want to go back to having a clean working directory. The most common situation I've come across for using `git stash` is when you have merge conflics when pulling code.

#### stashin'
* `git stash` is synonomoys to `git stash pull` and will stash all changes to the repository since it was last 'clean' meaning the last time there were no changes to commit.
* `git stash [-u|--include-untracked]` will also stash any untracked files you have changed or added since the `HEAD` commit
* `git stash [-a|--all]` will stash untracked files and any changes to ignored files

#### What to do once you've stashed
* `git stash list` shows you a list of all the things you have stashed. They are named using 0 indexing like `stash@{0}` ect. It will also show the branch you were on when the stash was made and then a description of the commit the stash was called on.
* `git stash show [<stash name>]` will show you the difference between the stash specified and the commit `git stash` reverted to when that stash was created. The output is formatted as a `diff` which you can find more information on [here](https://cspragmatics.com/ref/tools/diff).
* `git stash pop [<stash name>]` removes a stash from the `list` and make the changes stored in the stash to the current working directory. Be careful though because doing this can restult in conflicts which you have to resolve by hand.
* `git stash clear` and `git stash drop [<stash name>]` get rid of your stashes. `clear` will get rid of all the stashes in the list. `drop` gets rid of the specified stash.  

##### Example
* Trying to pull when there is merge conflicts

~~~ bash
$ git pull
  ---------------------
file myfile is not up to date, cannot merge.
$ git stash
$ git pull
$ git stash pop
~~~