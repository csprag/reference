touch
---
`touch` Creates a new empty file and can also change timestamps on existing files. Useful for creating empty files quickly.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ touch main.cpp
~~~

---

### Useful Options / Examples

#### `touch -a filename1 filename2 filename3 ...`

Allows you to create multiple empty files at the same time.

~~~ bash
$ touch main.cpp file1.h file1.cpp
~~~
This command is creating 3 new empty files: `main.cpp`, `file1.h`, and `file1.cpp`.

#### `touch -a filename`

Allows user to change the access time.

~~~ bash
$ touch -a main.cpp
~~~
This changes the access time for `main.cpp` to the current time. 

#### `touch -m filename`

Allows user to change modification time.

~~~ bash
$ touch -m main.cpp
~~~ 
This changes the modification time of `main.cpp` to the current time.

#### `touch -c filename`

This command checks whether a file is created or not. If it has already been created, it will not create another.

~~~ bash
$ touch -c filename
~~~

#### `touch -c-d filename`

This command is used to update access and modification time.

~~~ bash
$ touch -c-d filename
~~~
This changes the modification time of filename

#### `touch -t`
This command is used to create a file using a specified time.

~~~ bash
$ touch -t YYMMDDHHMM filename
~~~

#### `touch -r second_filename first_filename

This command is used to use the timestamp of another file. In this case, the secondfilename is updated with the timestamp of firstfilename.

~~~ bash
$ touch -r secondfilename firstfilename
~~~ 
