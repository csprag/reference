commit
-------

git commit records changes to the repository.

~~~ bash
$ edit hello.c
$ git rm goodbye.c
$ git add hello.c
$ git commit
~~~

---

### Useful Options / Examples

#### `commit -m`
~~~ bash
$ git commit -m <msg>
~~~

##### Break it down

* Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs. The -m option is mutually exclusive with -c, -C, and -F.

#### `commit -a`
~~~ bash
$ git commit -a
~~~

##### Break it down

* Use -a or --all to tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.

#### `commit -C`
~~~ bash
$ git commit -C <commit>
$ git commit -reuse-message=<commit>
~~~

##### Break it down

* -C<commit> or -reuse-message=<commit> takes an existing commit object, and reuses the log message and the authorship information (including the timestamp) when creating the commit.


#### `commit -v`
~~~ bash
$ git commit -v
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch commit-contribution
# Changes to be committed:
#       new file:   reference/static/commands/basics/commit.md
#
# Changes not staged for commit:
#       modified:   reference/static/commands/basics/commit.md
#       modified:   reference/static/commands/basics/cp.md
#
# ------------------------ >8 ------------------------
# Do not modify or remove the line above.
# Everything below it will be ignored.
diff --git a/reference/static/commands/basics/commit.md b/reference/static/commands/basics/commit.md
new file mode 100644
index 0000000..e69de29
~~~

##### Break it down

* git commit -v shows unified diff between the HEAD commit and what would be committed at the bottom of the commit message template to help the user describe the commit by reminding what changes the commit has.


