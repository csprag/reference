git log
---------
<!-- one line explanation would go here -->
`git log` shows you the past commits of that project in the currently checked out branch

<!-- minimal example -->
~~~ bash
$ git log
commit df46e29263becdf1b700cca838a44d864d6bc830 (HEAD -> master, origin/master, origin/HEAD)
Author: Joe Smith <smithjoe@gmail.com>
Date:   Sat Oct 10 10:10:10 2010 -0400

    Initial Commit 

~~~

---

### Useful Options / Examples

#### git log --all
~~~ bash
$ git log --all
~~~
* Adding --all will show all commits from all the branches, regardless of which branch is checked out.

#### git log -<n>
~~~ bash
$ git log -<n>
~~~	
* Displays the last <n> commits. For example, $ git log -2 will show you the 2 most recent commits. 

#### git log --author <name>
~~~ bash
$ git log --author <name>
~~~	
* Limits results to show the commits that were changed by <name>.

