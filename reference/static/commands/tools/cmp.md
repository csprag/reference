cmp
-------

cmp compares two files at the byte level and returns nothing if they are idenctical and the location of the first mismatch if they are different. This is mainly useful when comparing binary files like machine code

~~~ bash
$ cmp file1.txt file2.txt
file1.txt file2.txt differ: byte 9
, line 2 #if files are diff
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
#### `cmp -i [bytes-to-be-skipped]`
This compares all the character by the bytes of file1.txt and file2.txt after the 5th byte and 1st byte. The files are the same after the 5th by so there is no output and they are however different after the 1st byte.
~~~ bash
$cmp -i 5 file1.txt file2.txt
# no difference after the 5th byte
$cmp -i 1 file1.txt file2.txt
file1.txt file2.txt differ: char 1, line 1
~~~



#### `cmp -l`
This displays which character is different and what it's respective byte values are. Character 1, 2, and 3 are different (Dog vs Cat) and the numbers in each row represent the byte values of the differing characters
~~~ bash
$ cmp -l file1.txt file2.txt
 1 104 103
 2 157 141
 3 147 164
~~~

