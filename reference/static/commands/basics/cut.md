cut
-------

The `cut` command allows for the manipulation of input text by extracting specific fields or bytes from each line.

~~~ bash
$ echo "foo bar baz" > file
$ cut -d " " -f 1,3 file
foo baz
$ cut --complement -d " " -f 1,3 file
bar
~~~

---

### Useful Options / Examples

The general usage of `cut` is the following:
~~~ bash
$ cut [OPTIONS] [FILENAMES]
~~~

The  `OPTIONS` specify how you might want to cut each line of the input. You can break down lines into bytes (`-b` flag), characters (`-c` flag), or fields (`-f` flag) with a delimiter. Then you specify which chunks you want displayed either by position (NUM), or with a range (START_NUM-END_NUM).

#### Cut line into bytes

You can use the `-b` flag to select specific bytes of each line.
~~~ bash
$ echo "This is my first line \nThis is my second line" > file
$ cut -b 9-17 file
my first   # the 17th byte is a space
my second

~~~

~~~ bash
$ cut -b 1,3,5,12 file   # indexing is 1-based
Ti f   # the 5th byte is a space
Ti s
~~~

~~~ bash
$ cut -b 5- file   # cut everything from the fifth byte until the end of the line
 is my first line
 is my second line
~~~

#### Cut line into characters

You can use the `-c` flag to select specific characters of each line.
~~~ bash
$ echo "This is a\ttab\nThis is a space" > file
$ cut -c 9,10,11 file   # spaces and tabs are each single characters
a	t
a s
~~~

~~~ bash
$ cut -b -10 file   # get all characters up to the 10th
This is a
This is a
~~~

#### Cut line into fields

You can use the `-f` flag to select specific fields of each line. The default delimiters are tabs. You can change that using teh `-d "<DELIM>"` option.
~~~ bash
$ echo "This is a\tline with tabs\nThis line does not have tabs" > file
$ cut -f 1 file   # get the first field delimited by tabs
This is a
This line does not have tabs
~~~

Changing the delimiter:
~~~ bash
$ cut -d " " -f 1,2,3 file   # change the delimiter to space
This is a	line
This line does
~~~

We can suppress lines that do not have the given delimiter:
~~~ bash
$ cut -d '%' -f 1 file  # will display whole line since the delimiter is not present
This is a	line with tabs
This line does not have tabs
$ echo "Another%line" >> file
$ cut -d '%' -s -f 1 file  # will suppress first two lines
Another
~~~

#### Get complement of selection

You can invert your selection using the `--complement` flag:
~~~ bash
$ echo "This is a line.\nThis is another line." > file
$ cut --complement -d ' ' -f 1 file  # get all fields except for 1
is a line.
is another line.
~~~

#### Pipe other commands into cut

The power of cut is most evident in combination with other commands. It allows you to directly manipulate the output of other commands in order to extract useful information from them.

~~~ bash
$ echo "name,age,gpa,major" > student_records.csv
# insert student information into csv
$ cat student_records.csv | head | cut -d ',' -f 1,3,4 | sort   # get first 10 students' name, gpa, and major in lexicographic order
~~~