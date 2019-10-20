sdiff
---

`sdiff` is a command that compares two files and writes the results to standard output in a side-by-side format. It displays a < (less than sign) in the field of spaces if the line only exists in the file specified by the File1 parameter, a > (greater than sign) if the line only exists in the file specified by the File2 parameter, and a | (vertical bar) for lines that are different.

~~~ bash
$ sdiff file1.txt file2.txt
Sam                               Sam
Elise                             Elise
Thomas                          | Wendy
Richard                         <
~~~

---

### Useful Options / Examples

#### `sdiff -l`

This displays only the left side when lines are identical.

~~~ bash
$ sdiff -l file1.txt file2.txt
Sam                             (
Elise                           (
Thomas                          | Wendy
Richard                         <
~~~


#### `sdiff -s`

does not display the identical identical lines.

~~~ bash
$ sdiff -s file1.txt file2.txt
Thomas                          | Wendy
Richard                         <
~~~


#### `sdiff -o OutFile`

Creates a third file, specified by the OutFile variable, by a controlled line-by-line merging of the two files specified by the File1 and the File2 parameters.

~~~ bash
$ sdiff -o output.txt file1.txt file2.txt
Sam
Elise
Thomas
Richard
Wendy
~~~