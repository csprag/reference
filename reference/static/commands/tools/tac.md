tac
-------

`tac` is a command that is used to _concatenate_ and print files in reverse, writing each file to standard output, the last line first. `tac` is essentially the reverse version of the `cat` command.    

~~~ bash
$ echo -e "example \nThis is an:" > beginning.txt
$ cat beginning.txt
example
This is an:
$ tac beginning.txt
This is an:
example
~~~

---

### Useful Options / Examples

#### Example command
One usage of the `tac` command is represented by the `-s`, `--separator` flag which seperates the contents of the file based on a string or a keyword from the file instead of newline.

~~~ bash
$ echo "engr101,engr151,eecs203,eecs280,eecs281,eecs201" > example.txt
$ cat example.txt
engr101,engr151,eecs203,eecs280,eecs281,eecs201
$ tac example.txt #Normally, tac reads files from last LINE to first
engr101,engr151,eecs203,eecs280,eecs281,eecs201
$ tac example.txt -s , #Now, the default seaparator is the string ","
eecs201
eecs281,eecs280,eecs203,engr151,engr101,$ #List is now outputted in reverse order
~~~

#### Example command

As can be seen from above, the string "eecs201" was not separated based on the comma since there was no comma after it originally. `tac` can change this as it has the option to put the separator before instead of after using the `b`, `--before` flag. 

~~~ bash
$ echo "engr101,engr151,eecs203,eecs280,eecs281,eecs201" > example.txt
$ cat example.txt
engr101,engr151,eecs203,eecs280,eecs281,eecs201
tac example.txt -b -s ,
,eecs201
,eecs281,eecs280,eecs203,engr151engr101$ #Now the comma comes before each string
$ echo ",engr101,engr151,eecs203,eecs280,ees281,eecs201," > secondExample.txt
$ cat secondExample.txt
,engr101,engr151,eecs203,eecs280,eecs281,eecs201,
$ tac secondExample.txt -s ,

eecs201,eecs281,eecs280,eecs203,engr151,engr101,,$ #There are two commas at the end
$ tac secondExample.txt -b -s ,
,
,eecs201,eecs281,eecs280,eecs203,engr151,engr101$ #No commas at the end
~~~


