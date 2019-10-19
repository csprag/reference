shuf
---

`shuf` is used to randomly shuffle the lines of an input file. Shuf can also limit the number of random lines returned.  

~~~bash
$ shuf example.txt
~~~

---

### Useful Options / Examples

Output lines in random order from a file

~~~ bash
$ cat example.txt
  1
  2
  3
  4
$ shuf example.txt
  2
  4
  3
  1
~~~

---

#### `shuf -n`

Allows user to choose the number of randomly chosen lines that are ouputed. 

~~~ bash
$ shuf -n1 example.txt
  3
$ shuf -n2 example.txt
  4
  1
~~~

---

#### `shuf -e`

Allows user to pass in inputs directly to shuf instead of reading from a file.

~~~ bash
$ shuf -e 1 2 3 4 5
  3 
  2
  4
  5
  1
~~~

We can combine this with the -n flag to choose a random number

~~~ bash
$ shuf -n1 -e 1 2 3 4 5
  3
~~~

---

### `shuf -i`

This command allows user to output random numbers/lines in a range

~~~ bash
$ shuf -i 1-5
  2
  3
  4
  1
  5
~~~
