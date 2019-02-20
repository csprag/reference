cd
-------

Stands for "change directory". Allows you to navigate to a different shell working directory.

~~~ bash
$ pwd
$ /Users/Desktop/csprag
$ ls
$ week01
$ cd week01
$ pwd
$ /Users/Desktop/csprag/week01
~~~

---

### Useful Options / Examples

#### cd -

##### Switches back to the previous directory in which you were working. If you were not previously working in a directory, then "cd -"  will give you an error saying "cd: no OLDPWD was set". In this case if you want to go up and you have parent directories, you need to navigate to them using "cd .." or "cd ../"

#### cd .. or cd ../

##### Changes your current directory to the parent directory (which effectively moves up one directory)

##### cd ~

##### Moves to users home directory from any directory

##### cd

##### Moves directly to root directory

##### cd + directory with whitespace

##### To navigate to a directory with whitespace in its name, you can use a "\" before the space so that cd knows which directory to navigate to. If you do not use "\", then cd will only read the name until the first space.
