whereis
-------

`whereis` locates the binary, source, and manual page files for a command.

~~~ bash
$ whereis ls
ls: /bin/ls /usr/share/man/man1/ls.1.gz
~~~

---

### Useful Options / Examples

General form:

`whereis [-bms] [-BMS directory -f] command`

`whereis` can be used with the flags `-b`, `-m`, or `-s`.

The `-b` flag returns only the location of the command's binary file.

~~~ bash
$ whereis -b ls
ls: /bin/ls
~~~

The `-m` flag returns only the location of the command's manual file.
~~~ bash
$ whereis -m mv
mv: /usr/share/man/man1/mv.1.gz
~~~

The `-s` flag returns only the location of the command's source file.

The flags `-B`, `-M`, and `-S` are used with a directory to tell the `whereis` command where to look for the binary, manual, and source files, respectively. When using these flags, you must specify at least one directory AND include `-f` to signal the end of the list of directories and the beginning of the commands to search for.

~~~bash
$ whereis -B /usr/bin/ -f cp
cp: /usr/share/man/man1/cp.1.gz
~~~

The command sequence above tells the computer to look for binary files for the command `cp` only in the directory /usr/bin/ and look for other file types in default paths.

#### How whereis works

`whereis` only looks in a certain set of hard-coded paths for the binary, source, and command files. This is why it is sometimes necessary to tell the whereis command what other directories to search in. To see the default directories that whereis looks in, use the `-l` flag.

~~~bash
$ whereis ls -l
ls: /bin/ls /usr/share/man/man1/ls.1.gz
bin: /usr/bin
bin: /usr/sbin
bin: /lib/x86_64-linux-gnu
bin: /usr/lib/x86_64-linux-gnu
bin: /usr/lib
bin: /bin
bin: /sbin
bin: /etc
~~~
---
More folders are included as well.

In the directory list, you can include only a few paths that are already searched to limit the command's search, or you can include paths that are not already searched.

Some commands are built in to the shell and do not have files in directories on the computer.

~~~bash
$ whereis cd
cd:
~~~
