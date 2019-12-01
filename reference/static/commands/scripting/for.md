for
-------
for performs a set of commands multiple times as specified by a changing amount of values.


`for VARNAME in [VALUES]; do COMMANDS; end`

-------

for performs a set of commands multiple times. It will perform the commands specified by COMMANDS multiple times. Each time the environment variable specified by VARNAME is assigned a new value from VALUES. If VALUES is empty, COMMANDS will not be executed at all.

~~~ bash
$ for variable in 0 1 2 3; do echo $variable; end
0
1
2
3
~~~

---

### Useful Options / Examples

#### char / string input

~~~ bash
$ for v in a b c d; do echo $v; end
a
b
c
d
~~~

##### Break it down

* The variable within the for loop can be any type, and is not just limited to ints, but almost anything you can think of.

#### file looping

~~~bash
$ for FILE in $HOME/.bash*; do echo $FILE; done
/root/.bash_history
/root/.bash_logout
/root/.bash_profile
/root/.bashrc
~~~

##### Break it down

*The variable for the for loop can even be files, and the for loop is able to read all the files and perform commands for each one. 

#### using `seq`

~~~bash
$ for i in $(seq 5) ; do echo $i; done
1
2
3
4
5
~~~

##### Break it down

*The `seq` function generates a sequence that can used for the for loop input.



