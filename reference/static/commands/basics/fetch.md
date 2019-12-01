fetch
---

`git fetch` downloads commits, files, and refs from a remote repository into your local repo

~~~ bash
$ git fetch <remote>
~~~

---

### Useful Options / Examples

#### `git fetch <remote>` 
~~~ bash
$ git fetch <remote>
~~~

 * Fetch all of the branches from the repository. This also downloads all of the required commits and files from the other repository.

~~~ bash
$ git fetch <remote> <branch>
~~~

 * Same as the above command, but only fetch the specified branch.

~~~ bash
$ git fetch --all
~~~

 * Fetch all remote repositories and all their branches.