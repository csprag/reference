awk
-------

`awk` is a utility for pattern scanning and processing. It searches files to see if they contain lines that match and perform the associated action. 

~~~ bash
$ awk '{print}' example.txt
===OUTPUT===
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
~~~

---

### Useful Options / Examples

#### Example command
Print the lines of a file that matches the pattern given by the user

~~~ bash
$ awk '/manager/ {print}' example.txt
ajay manager account 45000
varun manager sales 50000
amit manager account 47000
~~~

#### Example command
Split lines delimited by whitespace. You can set demlimiter with -F flag

~~~ bash
$ awk '{print $1,$4}' example.txt
 ==OUTPUT===
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
~~~

#### Built in Variables
Awk has many built in variables, including field variables like $1, $2, $3, etc.

FS: FS contains the field separator character.
RS: RS stores current separator character.

NR: NR command keeps a current count of the number of input records.
This example uses the NR variable to display line numbers.
~~~ bash
$ awk '{print NR, $0}' example.txt
1 ===OUTPUT===
2 ajay manager account 45000
3 sunil clerk account 25000
4 varun manager sales 50000
5 amit manager account 47000
6 tarun peon sales 15000
7 deepak clerk sales 23000
8 sunil peon sales 13000
9 satvik director purchase 80000
~~~

NF: NF command keeps a count of the number of fields in the current input record.
This example uses NF to display the first and last field.
~~~ bash
$ awk '{print $1, $NF}' example.txt
 ===OUTPUT===
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
~~~

#### Advanced Example
Finding the longest line in the file
~~~ bash
$ awk '{ if (length($0) > max) max = length($0) } END { print max }' example.txt
31
~~~
