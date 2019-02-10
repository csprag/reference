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
-i [bytes-to-be-skipped]: to skip an initial amount of bytes
-l option : prints byte position and byte's value for all differing bytes

#### Example command
~~~ bash
$cmp -i 10 file1.txt file2.txt
~~~

##### Break it down
This compares all the bytes of file1.txt and file2.txt after the 10th byte

#### Example command
~~~ bash
cmp -l file1.txt file2.txt
~~~

##### Break it down
This prints all the bytes that are different between file1.txt and file2.txt
