chsh
----

The chsh command allows a user to change the local login shell. The command accepts a filename as an input where a valid shell is stored in the machine. If no shell is found or no valid filename is given, the command will prompt for a valid filename/shell.

### Syntax 
~~~bash
chsh [-s login_shell] [-l] [-h] [-v] [username] 
~~~

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
