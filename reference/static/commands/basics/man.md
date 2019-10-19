man
-------

`man` is used to view the manual page of another program, utility, or function. Once called, an interface opens with program details. To exit this interface, press **q**.

The general format is

~~~ bash
$ man [options] [command/utility]
~~~

---

A simple example is:

~~~ bash
$ man cat
~~~

This will open up the manual page for the command `cat`, listing the full, robust documentation for `cat`. This is helpful to check what command flags are or to get a quick rundown of a new command a user is unfamiliar with. 

### Useful Options / Examples

#### `man -f, --whatis`
Look up all reference pages for the specified keyword and print their shortest description. This is a great flag to use if the user doesn't want to dive into an entire manual page and just wants a quick overview of a new command

For example, if we wanted to see a brief overview of commands ls, echo, and grep, we could run:

~~~ bash
$ man -f ls
ls (1)               - list directory contents
LS (6)               - display animations aimed to correct users who accidentally enter LS instead of ls .
$ man -f echo
echo (1)             - display a line of text
$ man -f grep
grep (1)             - print lines matching a pattern
~~~

#### `man -k, --apropos` 
Search the short descriptions and manual page names for the specified keyword as a regular  expression. Print out any matches. Equivalent to apropos printf.

For example, if we wanted to list all manual page names and descriptions for the command `mkdir`:

~~~ bash
$ man -k mkdir
mkdir (1)            - make directories
mkdir (2)            - create a directory
mkdirat (2)          - create a directory
~~~

