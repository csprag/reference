look
-------

`look` is a program for printing all lines in a file that begin with a specified string. If no file is specified, it will instead search through `/usr/share/dict/words`.

~~~ bash
$ look [string] [file]
~~~

---

Below is a sample of output you would get with `look`:

~~~ bash
$ look "import" test.py             // list lines in the python file starting with import
import numpy
import flask
~~~


### Useful Options / Examples

#### -f, -&#45;ignore-case

Using the `-f` or `--ignore-case` option will ignore the case of alphabetic characters in the string. 

#### -t, -&#45;terminate

The `-t` or `--terminate` option specifies a string termination character. This means that only the characters in the string up to and including the first occurrence of the termination character are compared.

~~~ bash
$ look -t l hello    //List all words starting with hello, up to the first occurrence of char l
helen
held
hello
~~~

#### -d, -&#45;alphanum

Using `-d` or `--alphanum` will only compare alphanumeric characters.

#### -b, -&#45;binary

If the file is sorted, `-b` or `--binary` will use a binary search on the file.



### Tips

#### Check Spelling

Since this command uses `/usr/share/dict/words` if no file is specified, it can be used to check the spelling of a word. For example, say you don't remember how to spell rendezvous:

~~~ bash
$ look ren    // list all words starting with ren
rend
render
...
rendezvous
~~~

#### Finding Headers

This command can also be used to easily find what headers are being used by a .cpp file.

~~~ bash
$ look "#include" test.cpp   // list header includes
# include <iostream>
# include <string>
# include <cmath>
~~~
