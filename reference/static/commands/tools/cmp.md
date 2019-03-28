cmp
-------

cmp compares two files at the byte level and returns nothing if they are idenctical and the location of the first mismatch if they are different. This is mainly useful when comparing binary files like machine code

~~~ bash
$ cmp file1.txt file2.txt
file1.txt file2.txt differ:
byte 9, line 2 #if files are diff
--or--
  #if files are the same
~~~

---

### Useful Options / Examples
For the following examples I'll keep it simple with 
~~~ bash
$ echo "Dogs are cute" >> file1.txt
$ echo "Cats are cute" >> file2.txt
~~~
Note it's useful to remember that all ascii characters are one byte. In other words, every character in the files count as one byte. It's also worth noting that cmp uses character and byte interchangably.

#### `cmp -b`
This compares all the characters by the bytes of file1.txt and file2.txt and gives a more verbose explanation to the first mismatch in the files. More specifically, it will tell you not only the location of the first mismatch but the byte (ascii) values as well.
~~~ bash
$ cmp -b file1.txt file2.txt 
file1.txt file2.txt differ: byte 1, line 1 is 104 D 103 C
~~~

#### `cmp -i [bytes-to-be-skipped]`
This compares all the character by the bytes of file1.txt and file2.txt after the 3rd byte and 1st byte respectively. The files are the same after the 3rd byte so there is no output, but they are however still different after the 1st byte. Notice that the first byte after the first skipped bytes starts off at one.
~~~ bash
$ cmp -i 3 file1.txt file2.txt
# no difference after the 3rd byte
$ cmp -i 1 file1.txt file2.txt
file1.txt file2.txt differ: char 1, line 1
~~~

#### `cmp -l`
This displays which character is different and what it's respective byte values are. Character 1, 2, and 3 are different (Dog vs Cat) and the numbers in each row represent the differences in byte (ascii) values accross all bytes in the files.
~~~ bash
$ cmp -l file1.txt file2.txt
 1 104 103
 2 157 141
 3 147 164
~~~

