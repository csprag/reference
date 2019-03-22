sed
-------

sed is a Stream EDitor that takes each line from a file, stdin, or pipe and performs insert, substitute, 
and delete. The most common usage of sed is find and replace through the 
substitution command. When used with regular expression, sed is a powerful tool that allows you 
to match and edit patterns in text files without the need to open them in a text editor.

~~~ bash
$ sed OPTIONS [SCRIPT] [INPUTFILE]
~~~

---

### Useful Options
We will perform operations on example file *idol.txt* to demonstate some of the most common usage of sed.

~~~ bash
I love myself, I love my fans
Love my dance and my what
There are hundreds of me’s inside of me
I’m facing a new me again today
It’s all me anyway
So instead of worrying, I’m just gonna run
Runnin’ man, runnin’ man, runnin’ man
~~~

By default, sed does not modify the file that it operates on; it only output the result to the standard
output. To overwrite the file with the modified text, use the **-i** option
~~~ bash
$ sed -i 's/me/apple/' idol.txt
~~~

You can also redirect the output to another file:
~~~ bash
$ sed 's/me/apple/' idol.txt > newFile
~~~

You can also use sed to find out how many lines are in a file:
~~~ bash
$ sed -n '$=' idol.txt
7
~~~
The *-n* option is negation. This allows sed to only print out the line number of the last line, which
is equivalent to the total number of lines in the file.

### Find and Replace

A basic substitution command is made up of four parts. The *s* stands for substitution, *me* is the 
search pattern to be replaced, *apple* is the replacement string, and the three forward slashes are delimiters 
that separate the components of the command. **Delimiters can be any symbol that is not in the search pattern 
in order to reduce confusion.**
~~~ bash
$ sed 's/me/apple/' idol.txt > new.txt
I love myself, I love my fans
Love my dance and my what
There are hundreds of apple’s inside of me
I’m facing a new apple again today
It’s all apple anyway
So instead of worrying, I’m just gonna run
Runnin’ man, runnin’ man, runnin’ man
~~~

This also works (colon as the delimiter):
~~~ bash
$ sed 's:me:apple:' idol.txt > new.txt
I love myself, I love my fans
Love my dance and my what
There are hundreds of apple’s inside of me
I’m facing a new apple again today
It’s all apple anyway
So instead of worrying, I’m just gonna run
Runnin’ man, runnin’ man, runnin’ man
~~~

This command replaces the first instance of "me" in each line with "apple". The output is saved 
in a file called *new.txt*. *s/me/apple/* does not need to be in quotes, but it's good practice. 
Notice in the third line that the second occurrence of "me" is not affected by the command. 
This is because sed is **line oriented by default**. To substitute all occurrences, add the **g** option 
at the end of the command: *'s/me/apple/g'*. **If a word contains a matching pattern (e.g. dome),
sed still replaces the pattern (e.g. doapple).**

sed is case sensitive by default, to enable **case insensitivity**, add **i** to the command:
~~~ bash
$ sed 's/i/apple/gi' idol.txt
apple love myself, apple love my fans
Love my dance and my what
There are hundreds of me’s applensapplede of me
apple’m facappleng a new me agaapplen today
applet’s all me anyway
So applenstead of worryappleng, apple’m just gonna run
Runnapplen’ man, runnapplen’ man, runnapplen’ man
~~~

**Deleting strings** that match search pattern is the same as replacing the word with nothing:
~~~ bash
$ sed 's/me//g' idol.txt
I love myself, I love my fans
Love my dance and my what
There are hundreds of ’s inside of 
I’m facing a new  again today
It’s all  anyway
So instead of worrying, I’m just gonna run
Runnin’ man, runnin’ man, runnin’ man
~~~

To **replace whole line(s)**, a different syntax is used. This example replaces line 2 to 4 with "Line":
~~~ bash
$ sed '2,4 c\Line' idol.txt
I love myself, I love my fans
Line
It’s all me anyway
So instead of worrying, I’m just gonna run
Runnin’ man, runnin’ man, runnin’ man
~~~

This example replaces line 2 with "Line", then repeats the same action the next 4th line:
~~~ bash
$ sed '2~4 c\Line' idol.txt
I love myself, I love my fans
Line
There are hundreds of me’s inside of me
I’m facing a new me again today
It’s all me anyway
Line
Runnin’ man, runnin’ man, runnin’ man
~~~

### Deleting Lines

There are many ways to delete line(s) from a file. You can specify which lines you want to delete 
by giving the line number, a range of line numbers, or using regular expression to delete lines that
match a specific pattern. 

To delete the 5th line:
~~~ bash
$ sed '5d' idol.txt
~~~

To delete the last line:
~~~ bash
$ sed '$d' idol.txt
~~~

To delete line 2 to line 6:
~~~ bash
$ sed '2,6d' idol.txt
~~~

To delete to pattern matching line:
~~~ bash
$ sed '/pattern/d' idol.txt
~~~

### Insertion / Append

sed can also insert lines after specified lines and space your file systematically.

To insert a blank line after each line:
~~~ bash
$ sed G idol.txt
~~~

To insert 2 blank lines after each line:
~~~ bash
$ sed 'G;G' idol.txt
~~~
Commands can be combined with *;* to be executed in a single sed command. *'G;G'* is essentially 
executing *sed G idol.txt* twice.

To append a line after certain line(s) or after every pattern matching line:
~~~ bash
$ sed '2 a\Line which you want to append' idol.txt
$ sed '/pattern/ a\Line which you want to append' idol.txt
~~~

To insert a line before certain line(s) or before every pattern matching line:
~~~ bash
$ sed '2,5 i\Line which you want to append' idol.txt
$ sed '/pattern/ i\Line which you want to append' idol.txt
~~~
