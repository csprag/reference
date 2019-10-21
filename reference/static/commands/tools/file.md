---
---

file
-------
<!--TODO: Add documentation for this command by submitting a pull request.-->
<!-- one line explanation would go here -->
`file` prints the file type of a file in a human-readable format

<!-- minimal example -->
~~~ bash
$ file test.cpp
test.cpp: c program text, UTF-8 Unicode text

~~~


<!--more-->

### Useful Options / Examples

Useful on Unix since file extensions sometimes are completely unrelated to their actual type.

~~~bash
file starter-files.csvs
starter-files.csv: Zip archive data, at least v2.0 to extract
~~~

#### `file`

~~~bash
$ file [options] filename ...
~~~

Options include:

1. `b` to only show the file type (rather than the file name followed by the file type)
2. `i` to show the file's mime type
3. `z` to view compressed files without decompressing
 

----

#### `file -bi filename`

~~~bash
$ file -z bar.txt.gz
$ bar.txt.gz: ASCII text (gzip compressed data, was "bar.txt", last modified: Wed Sep  7 19:31:23 2016, from Unix)

file -bi file.txt
file.txt: text/plain; charset=us-ascii
~~~

##### Break it down

* The -b option will print only the file type
* The -i option will print the file's mime type rather than a human-readable description of the file type
----


