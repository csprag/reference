chsh
----

The chsh command allows a user to change the local login shell. The command accepts a filename as an input where a valid shell is stored in the machine. If no shell is found or no valid filename is given, the command will prompt for a valid filename/shell.

The change takes effect the next time the user logs in.

~~~ bash
$ chsh [-s login_shell] [-l] [-h] [-v] [username] 
~~~

---
### Options
 * `-s login_shell`   Sets login_shell as current shell
 * `-l`     Prints list of shells in /etc/shells for Linux machines
 * `-u`     Prints syntax and options on how to use command
 * `-v`     Prints current version installed in the machine
 * `username` Sets name of the current shell user
 
 ### Example
 
~~~bash
chsh -s /bin/zsh Bob 
~~~

Sets user Bob's login shell to zsh located in /bin/zsh

chsh will accept the full pathname of any executable file on the system. However, it will issue a warning if the shell is not listed in the /etc/shells file. It can also be configured to accept only shells listed in this file (unless the user is root). If a shell is not specified, chsh will prompt for one to be specified.

Some related commands include, chfn - change a user's finger information, usermod - change a user's account and passwd - change a user's password.
