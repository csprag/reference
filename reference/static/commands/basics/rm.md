rm
-----

`rm` is a built-in command used to remove files from the user's computer

~~~ bash
rm <file>
~~~

This command will search the **working directory** for the specified file(s) and *permanently*
remove any matching files. To see the working directory, use the command `pwd`.

---

Errors
-----

You can't remove something that isn't there. If a file you named doesn't exist, `rm` will tell you.

~~~ bash
rm absent.file
rm: absent.file: No such file or directory
~~~

In this case, `absent.file` was not found in the working directory.

Multiple Files
-----

We can remove multiple files with just one command. Simply list as many files as you'd like
to remove.

~~~ bash
rm <first> <second> <third>
~~~

This command will remove files `<first>`, `<second>`, and `<third>` from the working directory.

Directories
-----

By using the `-R` or `-r` options (they do the same thing), we can remove directories
*recursively*.

~~~ bash
rm -R <directory>
~~~

This command will remove the entire directory rooted at `<directory>`, including any files
or directories it contains.

#### Bypass Prompts

Sometimes you will be prompted to confirm that you want to remove a file. To skip the prompt
and confirm anyway, use the `-f` option.

~~~ bash
rm -f <file>
~~~

This will remove `<file>` without a prompt, regardless of the file's permissions.

~~~ bash
rm -Rf <directory>
~~~

This will remove the entire directory rooted at `<directory>`, including any files or directories
it contains, without any prompts.
