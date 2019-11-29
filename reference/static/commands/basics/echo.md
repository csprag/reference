echo
---

`echo` is used to display a message on the screen and write the given message to standard output with a newline at the end.  `echo` is implemented as built-in command in many command shells like bash, ksh, csh.
<!-- one line explanation would go here -->

<!-- minimal example -->

~~~ bash
$ echo "Hello World"
Hello World
$ echo Hello World
Hello World
~~~

---


### Useful Options / Examples

#### Example command
`echo` output can be redirected into a file for easy use. 

~~~ bash
$ echo Hello World > example.txt
$ cat example.txt
Hello World
~~~

#### Example command
`echo -n` is a useful flag if you don't want the trailing newline after the string

~~~ bash
$ echo -n "Hello World." ; echo " There is no new line before me."
Hello World. There is not new line before me.
~~~

#### Example command
`echo` can also be used with pattern matching. The following command line will show all the cpp files under current directory. 

~~~ bash
$ echo *.cpp
~~~

The following command line will show all the files under current directory.

~~~ bash
$ echo *
~~~

#### Example command
'echo' can be used to show the environment value. The following command line will show user's PATH environment variable.

~~~ bash
$ echo $PATH
~~~

#### Example command
`echo x >> y` is used to append x to the end of y.

~~~ bash
$ echo Hello > Hello_World.txt
$ cat Hello_World.txt
Hello
$ echo World >> Hellow_World.txt
$ cat Hello_World.txt
Hello
World
~~~

#### Example command
`echo -e` flag is used to enable the backslash-escaped characters in following table:

~~~ bash
$ echo -e -n "Hello World.\nThis is a new line.\n"
Hello World.
This is a newline.
~~~

#### Example command
Examples with `echo -e` include:

~~~ bash
$ echo -e "EECS \n201 \nis \nfun
EECS
201
is
fun

$ echo - e "\vEECS \v201 \vis \vfun
EECS
    201
       is
         fun
~~~
|       |                                        Backslashescaped characters                                         |
|-------|:----------------------------------------------------------------------------------------------------------:|
|   \\  |                                    a literal backslash character ("\").                                    |
|   \a  |                                                  An alert.                                                 |
|   \b  |                                                 Backspace.                                                 |
|   \c  |                                    Produce no further output after this.                                   |
|   \e  |                        The escape character; equivalent to pressing the escape key.                        |
|   \f  |                                                  Form feed                                                 |
|   \n  |                                                  New line                                                  |
|   \r  |                                               Carriage Return                                              |
|   \t  |                                               Horizontal tab                                               |
|   \v  |                                                Vertical tab                                                |
|  \NNN | The character whose ASCII code is NNN(octal); if NNN is not a valid octal number, it is printed literally. |
| \xnnn | The character whose ASCII code is the hexadecimal value nnn.                                               |
~~~
