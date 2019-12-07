git push
-------

`git push` is a command to upload local repository content to a remote repository. It's the counterpart to `git fetch`.

~~~ bash
$ git push origin master
~~~

###Basic Usage
`$ git push <remote> <branch>`
---

### Useful Options / Examples

##### `git push <REMOTENAME> <LOCALBRANCHNAME>:<REMOTEBRANCHNAME>`

 To rename a branch, add one more argument to git push separated by a `:`. This pushes the `LOCALBRANCHNAME` to the `REMOTENAME`, but it is renamed to `REMOTEBRANCHNAME`

##### `git push <REMOTENAME> <TAGNAME>`
 To push a single tag, use the `git push` command and add your `TAGNAME` to it.

##### `git push <REMOTENAME> --tags`
 To push all your tags, add `--tags` to the `git push` command


##### `git push <REMOTENAME> :<BRANCHNAME>`
 To delete a branch use the above syntax. Note, this is similar to the syntax for renaming a branch (there is a space before the colon).

##### `git push <remote> --force`
Forces the push, even if it results in a non-fast-forward merge. Do not use the `--force` flag unless you're absolutely sure you know what you're doing.

##### `git push <remote> --all`
Use this command to push all of your branches to the specified remote.

##### `git push <remote> --delete`
Use this command to delete all listed references from the remote repository. This can also be done by prefixing all references with a colon.


