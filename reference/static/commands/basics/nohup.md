nohup
-------

`nohup` allows you to keep a process running even after you log out.

~~~ bash
$ nohup wget [link] & 
[1] 56166
appending output to nohup.out
~~~

---

### Useful Options / Examples

#### `nohup sh your-script.sh &` 
`nohup` is useful when you want to run long commands using ssh, log out of the ssh session, and keep the command running.

~~~ bash
$ ssh login.engin.umich.edu
$ nohup ./myLongScript [options for myLongScript] &
$ exit
~~~
##### Break it down
 * myLongScript will continue to run even after exiting the ssh session, shutting down, etc.
 * by default, stdout and stderr output will be redirected to nohup.out in the working directory.

#### `nohup sh your-script.sh > /custom/path &`
~~~ bash
$ nohup ls > ls.out &
[1] 56413
[1]+ Done		nohup ls > ls.out
$ cat ls.out
File1
File2
Directory1
~~~
##### Break it down
 * adding a custom path allows you to redirect output to somewhere other than nohup.out
