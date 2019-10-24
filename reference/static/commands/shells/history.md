history
-------

`history` lists Command Line history.

~~~ bash
$ history 2
500  ssh -i 485awskey.pem ubuntu@ec2-52-15-191-29.us-east-2.compute.amazonaws.com
501  ls
~~~

---

#### Syntax
~~~bash
history [n]

history -c

history -d offset

history -anrw [filename]

history -p arg [arg ...]

history -s arg [arg ...]

~~~
#### Options

~~~ bash
   -c        Clear the history list by deleting all the entries.

   -d        offset Delete the history entry at position offset.

   -a        Append the `new' history lines (history lines entered since the beginning of the current
             bash session) to the history file.

   -n        Read  the history lines not already read from the history file into the current history
             list.  These are lines appended to the history file since the beginning of the current
             bash session.

   -r        Read the contents of the history file and use them as the current history.

   -w        Write the current history to the history file, overwriting the history file's contents.

   -p        Perform history substitution on the following args and display the result on the standard
             output.  Does not store the results in the history list.  Each arg must be quoted
             to disable normal history expansion.

   -s        Store the args in the history list as a single entry.  The last command in the history
             list is removed before the args are added.

~~~

#### Break it down
With no options, display the command history list with line numbers. Lines listed with a * have been modified.

An argument of n lists only the last n lines.
