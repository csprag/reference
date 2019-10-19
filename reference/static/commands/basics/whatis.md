whatis
-------

`whatis` provides very brief descriptions of command line programs

~~~ bash
$ whatis cat
fc-cat(1) - read font information cache files
...
cat(1)    - concatenate and print files
~~~

---

`whatis` is equivalent to `man -f` and looks up a given command, system call, library function, or special file name, as specified by the Command parameter.

### Useful Options / Examples

#### Example command

`whatis [command][command]` can be used to simultaneously search for information about multiple topics. 

~~~bash
$ whatis head tail
ghead(1), head(1)        - output the first part of files
...
gtail(1), tail(1)        - output the last part of files
tail(1)                  - display the last part of a file
~~~

The above example would provide information about both `head` and `tail.` 

#### Example command

If I want to find similar commands, I can use the wildcard `whatis -w`.

~~~bash
$ whatis -w 'ls*'
ls (1) - list directory contents
lsattr (1) - list file attributes on a Linux second extended file system
...
~~~

The above example provides information on all commands starting with `ls` combination.
