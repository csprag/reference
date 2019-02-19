rev
-------

`rev` reverses the order of lines of text and prints it out to the standard console.
It can be run either on a file or on its own. If run on a file, `rev` prints out each line in reverse, without modifying the original file itself. If run on its own, `rev` enters the secondary prompt `PS2` and waits for additional input, printing out each line as they are entered.

~~~ bash
$ rev
hello world
dlrow olleh
$ rev example.txt 
dlrow olleh
~~~

---

### Useful Options / Examples
-V prints out the version of `rev` used

-h prints the help page for `rev`, describing its functionality and these two options

#### Example command
~~~bash
$ rev -V
rev from util-linux 2.31.1
$ rev -V test.txt
rev from util-linux 2.31.1
~~~

##### Break it down
This flag simply displays the version of `rev` used, forgoing the printing of any lines to be reversed.

#### Example command
~~~bash
$ rev -h
Usage: rev [options] [file ...]

Reverse lines characterwise.

Options:
 -h, --help     display this help
 -V, --version  display version

For more details see rev(1).
~~~

##### Break it down
This flag simply displays the help page for `rev`, forgoing the printing of any lines to be reversed.
