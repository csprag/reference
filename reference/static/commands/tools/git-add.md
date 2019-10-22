git add
-------
`git add` is command that adds changes in the working directory to the staging area. It tells Git which files you want to include and update in the next commit.

##Common Options
~~~bash
$ git add <file-name>
$ git add <directory>
$ git add .
~~~

### Examples

##### `git add <file-name>`
This will add the specific file you want to the git staging area.

##### `git add <directory>`
This will stage all changes in <directory> for the next commit.

##### `git add .`
This will add all the files, folders, sub-folders to the staging area.

##### `git add *`
This will add all the files in the current directory, and stages them for a commit, except the ones that begin with a dot. 
