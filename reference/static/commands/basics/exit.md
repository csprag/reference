exit
-------

exit command allows user to exit a shell

~~~ bash
$ exit
~~~

---

### Examples

#### `exit N`
~~~ bash
$ exit 0
logout
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Process completed]
~~~

* exit N, where N is an integer, will exit the shell with a status of N, with 0 being a normal exit, and any non-zero value being an unsuccessful shell termination