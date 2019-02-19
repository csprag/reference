
mkdtemp
---

`mkdtemp()` creates a unique temporary directory.

~~~ bash
$ mkdtemp(char *template)

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

1. `mkdtemp` generates a uniquely named temporary directory from 'template'
2. the last six characters of 'template' are replaced with a string that makes the directory name unique
3. returns a pointer to the modified template string

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
`echo -e` flag is used to enable the backslash-escaped characters in following table:

~~~ bash
$ echo -e -n "Hello World.\nThis is a new line.\n"
Hello World.
This is a newline.
~~~

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
