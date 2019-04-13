type
-------

`type` displays information about any specified command. It can display command type, location 

~~~ bash
$ type cp
cp is /bin/cp
~~~

---

### Useful Options / Examples

#### Example Command

 To specify what type of tool a command is simply add the -t flag after `type` and the outcome will either be file, alias, keyword, function, builtin or `'.
~~~ bash
$ type -t ls
file
~~~
#### Example command
In order to determine if a command is a disk file, keyword, alias or function use the -a flag after `type`. This will also display any other places where the command is used if applicable.
~~~ bash
$ type -a pwd
pwd is a shell builtin
pwd is /bin/pwd
~~~
#### Example Command
The -p option can be used after `type` to find the name of the disk file executed by the shell when implementing a given command. Nothing will be returned if the command is not a disk file.
~~~ bash
$ type -p git
/usr/local/bin/git
~~~

