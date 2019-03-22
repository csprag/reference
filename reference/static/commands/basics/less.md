less
-------

Less allows the user to traverse forward or backward in a user stated file. Less can start before reading the entire file, therefore it can start faster than some text editors.
~~~ bash
$ less test.txt

This is the content of test!
test.txt (END)
~~~

---

### Useful Options / Examples

#### Example command q

While in less, pressing q will quit the program and send you back to terminal in the same state you left it in.

~~~ bash
$ less test.txt

This is the content of test!

1

2

3

4

5

test.txt (END)

q
~~~

#### Example command +(positive integer)

This will begin the file at the specified line

~~~ bash
less +2 test.txt

2

3

4

5

(END)
~~~

#### Example command ESC-) or RIGHTARROW ESC-( or LEFTARROW

This will shift right or left respectively. If a number is typed in beore this command, the amount shifted will be that number

~~~ bash
$ less test.txt

This is the content of test! LOOOOOOOOOOOOOOOOOOOOOONG LIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINEEEEEEEEEEEEEEEE

5 RIGHTARROW

is content of test! LOOOOOOOOOOOOOOOOOOOOOONG LIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINEEEEEEEEEEEEEEEE

RIGHTARROW

ntent of test! LOOOOOOOOOOOOOOOOOOOOOONG LIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINEEEEEEEEEEEEEEEE

10 LEFTARROW

This is the content of test! LOOOOOOOOOOOOOOOOOOOOOONG LIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINEEEEEEEEEEEEEEEE
~~~

#### Example command SPACEBAR

This will shift down or up respectively. If a number is typed in beore this command, the amount shifted will be that number

~~~ bash
$ less test.txt

This is content of test!

1

2

3

4

5

5 SPACEBAR

5 

6

7

8

9

10

3 u

2

3

4

5

6

7
~~~

#### Example command man less

Many more commands exist, visit man less to see if any are useful to you

