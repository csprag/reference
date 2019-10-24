alias
-------

alias saves time by creating a shortcut to an existing command or chain of commands.

~~~ bash
alias shortcut='echo hello'
~~~
Typing shortcut is now the same as running echo hello.

---

### Useful Options / Examples
Running alias in the command window creates a temporary alias.
This alias no longer exists in a new session.
To create a permanant alias, edit your .bashrc file.
Add the same command as you would type in the command window to the end of the file.
You can now always run that command in your bash terminal.

To remove a temporary alias, run the command unalias [SHORTCUT_NAME]
Using -a in place of the shortcut name will remove all aliases.
#### Example command
unalias shortcut
##### Break it down
shortcut no longer works as a command.
#### Example command
unalias -a
##### Break it down
all temporary aliases are erased.
