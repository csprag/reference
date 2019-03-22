head
-------

`head` is a unix command used to display the beginning of a text file or of data piped into the command. Without specification, `head` will display the first 10 lines of its input to standard output.

~~~ bash
$ echo "Hello World!" >> example.txt
$ head example.txt
Hello World!
~~~

---

### Useful Options / Examples

#### Example command
`head -n [-] num` is used to specify how many lines to print to standard output. If '-' is before *num*, head will print all but the last *num* lines of its input.
(Note: `seq 5` prints 1 to 5 in ascending order with a newline after each number.)

~~~ bash
$ seq 5 > example.txt
$ head -n 2 example.txt
1
2
$ head -n -2 example.txt
1
2
3
~~~

#### Example command
`head -c [-] num` prints the first n bytes. If '-' is before *num*, head prints all but the last *num* bytes. `head` counts a new-line as one byte.

~~~ bash
$ echo "Hello World!" > example.txt
head -c 3 example.txt
Hel
$ head -c -3 example.txt
Hello Worl
~~~ 

#### Example command
`head` can be given multiple input files. If this is done, `head` prints a one-line header for each file.

~~~ bash
$ echo "Hello," > example1.txt; echo "World!" > example2.txt
$ head example1.txt example2.txt
==> example1.txt <==
Hello, 

==> example2.txt <==
World!
~~~

With the -q flag, `head` will **not** print the header for each file:

~~~ bash
$ echo "Hello," > example1.txt; echo "World!" > example2.txt
$ head example1.txt example2.txt -q
Hello,
World!
~~~

#### Example command
`head` can be used for pattern matching. The following command prints the first 7 lines of all .txt files in the current directory:

~~~ bash
$ head -n 7 *.txt
~~~

#### Example command
If no input file is given, `head` will read from standard input. `head` can also take input through piping.
The following command prints the first 10 files in the current directory in alphabetical order:

~~~ bash
$ ls | head
~~~
