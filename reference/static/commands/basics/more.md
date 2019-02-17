more
-------

`more` controls the way text from a file is presented onto the screen

~~~ bash
$ more [flags] filename
~~~

---

One benefit of `more` vs a command such as `cat` is that unlike `cat`, using `more` ensures that you always see the beginning of the file first, even when the file is very long

Given a file named `alphabet` containing a letter of the alphabet per line, `more alphabet` will display as much of the file as possible on one screen and pause. Pressing `enter` displays the next line until the entire file is on the screen

~~~ bash
$ more alphabet
a
b
c
d
e
f
g
h
--More--(30%)
~~~

### Useful Options / Examples 

#### Example command

`more`'s `-number` flag will output only the given _number_ of lines at first, and then continue to display one line at a time by pressing `enter`

~~~ bash
$ more -2 alphabet
a
b
--More--(7%)
~~~

#### Example command

`more`'s `+number` flag displays the file starting at line number _number_

~~~ bash
$ more +5 alphabet
e
f
g
h
i
j
k
--More--(42%)
~~~

#### Example command

`more`'s `+/string` flag searches for _string_ in the file before displaying the contents of the file

If _string_ is found, it will display it along with nearby lines

~~~ bash
$ more +/z alphabet

...skipping
x
y
z
~~~

If the file does not contain the given string

~~~ bash
$ more +/2 alphabet
Pattern not found
~~~

Pressing `enter` will begin to display the contents of the file from the beginning

~~~ bash
$ more +/2 alphabet
a
--More--(3%)
~~~ 

#### Example command

`more`'s `-p` flag clears the screen before displaying the contents of the file

Given a terminal that initially looks like this

~~~ bash
t
u
v
w
x
y
z
$
~~~ 

Running `more -p -2 alphabet` 

~~~ bash
a
b
--More--(7%)
~~~

Even though the `-2` flag tells `more` to only display two lines of the file at first, the `-p` flag forces it to clear the terminal. It even gets rid of the line with the command `more -p -2 alphabet` to ensure that the only thing you see is the file specified

#### Example command

`more`'s `-s` flag detects multiple blank lines and only outputs one of them, allowing you to see more of the actual content of the file

In this example, the file named `alphabet` has two blank lines between each letter

~~~ bash
$ more alphabet
a


b


c
--More--(9%)
~~~

~~~ bash
$ more -s alphabet
a

b

c

d
--More--(13%)
~~~
