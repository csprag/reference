git clean
-------
This command cleans the working tree by recursively removing files that are not under version control, starting from the current directory.

~~~ bash
$ git clean -xdi
Would remove the following items:
  .pytest_cache/               insta485.egg-info/           insta485/__pycache__/        insta485/views/__pycache__/  var/
*** Commands ***
    1: clean                2: filter by pattern    3: select by numbers    4: ask each             5: quit                 6: help
What now>
~~~

---

### Useful Options / Examples
Sometimes, it may be useful to clear your working git directory of any dependencies and cache files for any number of different reasons. For example, often times when testing a project, you need to test on a completely clean and new build to simulate a user's first interaction with your project; `git clean` makes it easy to reset your development environment, without losing the important files that you've worked on for your project (i.e., files that you generated manually). More specifically, it makes it easy to remove files that are untracked by git and files that are included in your .gitignore file, which are commonly files that are computer generated, and therefore, do not need to be committed to the repo since they can be easily generated.

How `git clean` works, is it removes untracked files from the working tree. There are multiple command line options that are supported when running the `git clean` command, but the most commonly used (and most useful are listed below)
- -d: Remove untracked directories in addition to untracked files.
- -i or --interactive: Show what would be done and clean files interactively. When the command enters the interactive mode, it shows the files and directories to be cleaned, and goes into its interactive command loop.
- -x: This allows removing all untracked files, including build products.

#### Example command
Here's an example scenario: Say I'm working on a project for an EECS class that has a bunch of Python dependency files. While working on the project, I realize that I need to change the name of my home directory because Python (for whatever reason) struggles to understand that directory names may contain spaces (' '). I do this, and now I'm getting a directory not found error. This is because I have cached files stored inside my virtual environment directories. Here's how I can easily get rid of these cache files and get my project working again:

~~~bash
# Run 'git status' and commit any changes that need to be saved
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean

# Run 'git clean -xdi' to see what will be removed (this won't delete anything yet)
$ git clean -xdi
Would remove the following items:
  .pytest_cache/               insta485.egg-info/           insta485/__pycache__/        insta485/views/__pycache__/  var/
*** Commands ***
    1: clean                2: filter by pattern    3: select by numbers    4: ask each             5: quit                 6: help
What now> 4 # this option means it will iteratively ask what content I want deleted
Remove .pytest_cache/ [y/N]? y
Remove insta485.egg-info/ [y/N]? y
Remove insta485/__pycache__/ [y/N]? y
Remove insta485/views/__pycache__/ [y/N]? y
Remove var/ [y/N]? N
Removing .pytest_cache/
Removing insta485.egg-info/
Removing insta485/__pycache__/
Removing insta485/views/__pycache__/

$ # End of command sequence
~~~

##### Break it down
After this, your cache is cleared an you should be able to successfully run your project again (this is of course assuming it was working properly before the directory name change).

This is an example demonstration of a safe and easy way to remove your untracked files to develop with a fresh, clean working environment. It will come particularly in handy when working with a deep software stack that requires many dependencies and therefore has many interacting parts that all need to work together in order to build a successful project.

Feel free to try it out on your own or read the [official git documentation](https://git-scm.com/docs/git-clean) here for more details.

