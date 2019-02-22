Status
-------

git status displays the state of the working directory and shows you which changes have been made, which haven't and which files aren't being tracked by git

~~~ bash
git status [<options>..] [--] [<pathspec>...]
~~~

---

### Useful Options / Examples

#### -s or --short
~~~ bash
git status -s
git status --short
~~~

##### 
This flag gives the output in the short-format. This output the status of each path in a format of : XY PATH1 -> PATH2.
Path1 is the head the the ->path2 only shown when path1 is different than the worktree (a file is renamed).
The XY is a two - letter status code.
If there is a merge conflict, X and Y show the modification states of each side; otherwise X shows the status of the index and Y shows the status of the work tree. Otherwise these are the different symbols and their meanings:
`??` = untracked path
`''` = unmodified
`M` = modified
`A` = added
`D` = deleted
`R` = renamed
`C` = copied
`U` = updated but unmerged
Ignored files are not listed until --ignored is specificed and then they show up with the symbol `!!`.

#### -u[<mode>] or --untracked-files[=<mode>]
~~~ bash
git status -u
git status --untracked-files=no
~~~

##### 
Can show or not show untracked files
The parameter is optional and will default to all (showing all untracked files), but you can specify by adding:
`no` = show no untracked files
`normal` = shows untracked files and directories
`all `- Also shows individual files in untracked directories.
The default can be changed using the status.showUntrackedFiles configuration variable documented in git-config[1].

#### --ignored
~~~ bash
git status --ignored
~~~

##### 
Shows ignored files as well. These files are usually set with .gitignore previously.

####  --ignore-submodules[=<when>]
~~~ bash
git status --ignore-submodules=untracked
git status --ignore-submodules=dirty
~~~

##### 
This command ignored changes to submodules when looking for changes. The flag for <when> can be:
`none` = consider submodule modified when it has untracked or modified files or if its HEAD differs from the commit record
`untracked ` = submbodules are not considered dirty when they only contain untracked content (also scanned for modified content)
`dirty` = ignores all changes to work tree of submodules, only shows changes to the commits stored in the subproject
`all` = hides all changes to submodules
