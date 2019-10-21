cd
-------

`cd` is a command that changes your working directory

~~~ bash
$ pwd
/home/User
$ ls
eecs281 eecs201 eecs376 notaDirectory.txt
$ cd eecs201
$ pwd 
/home/User/eecs201
~~~

---

### Useful Options / Examples

To navigate to the parent directory, use two periods
~~~bash
$ cd ..
~~~

To navigate to the previous working directory, use a hyphen
~~~bash
$ cd -
~~~

#### Example command
`cd` can take an absolute path as an argument 

~~~bash
$ pwd 
/home/User
$ cd /home/User/eecs201/advanced-homework6
$ pwd 
/home/User/eecs201/advanced-homework6
~~~

#### Example command
Using 'cd ~' in any directory will navigate to the home directory

~~~bash
$ pwd
/home/User/eecs281/project3
$ cd ~
$ pwd 
/home/User
~~~

