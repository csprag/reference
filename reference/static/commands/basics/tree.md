tree
-------

tree is a very useful command when visualizing your current directory along with all of its subdirectories. It does a depth-first search on the current directory and every single subdirectory inside of it. You can customize it to give you different outputs.

~~~bash
$ pwd
/
$ tree -L 1
.
├── bin
├── boot
├── dev
├── etc
├── home
├── init
├── lib
├── lib64
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── snap
├── srv
├── sys
├── tmp
├── usr
└── var

20 directories, 1 file
~~~

---

### Useful Options / Examples
If you were to type just "tree" the command woudl print all files within your current directory, regardless if they were in other directories. This makes the command useless, especially if you are printing from a directory such as "Documents". 

tree has a lot of useful flags which can make it more reasonable to use:
 	- -d: prints only the subdirectories within the current directory
 	- -L + number: prints everything in the current directory, but only up to the specified depth level given by "number"
 	- -s: prints the filename along with its size in bytes
 	- -o filename: prints all output from the command into "filename"

You can also sort the order of the directories with the following flags:
	- -t: sort the output based on when the file was last modified instead of alphabetically
	- -U: don't sort at all: list files as the appear in the directory

 There are a lot of useful other options which can be seen in its manual or by typing 

~~~bash
$ man tree
~~~

