git init
---
`git init` is a command that creates an empty Git repository.

~~~ bash
cd /desiredPath
git init
git add .
git commit
~~~

---
### Additional Information

This command creates a `.git` directory with subdirectories for `objects`, `refs/heads`,
`refs/tags`, and template files. An initial `HEAD` files that references the HEAD of the 
master branch is also created.

Some flags that can be used:
* `-q` or `--quiet` - Only print error and warning messages. All other output will be surpressed.
* `--bare` - Creates a bare repository.
* `--template=<templateDirectory>` - Specifies the directory from which templates will be used.
 
