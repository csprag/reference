at
-------

'at' allows the user to execute a command at a specified time

Using 'at' will open a prompt for bash commands to be executed at the specified time. This can be escaped using 'ctrl-d'.

~~~ bash
$ at now + 1 minute
at> echo "E"
at> <EOT>
job 1 at Sun Fed 17 19:09:00 2019
~~~

---

### Useful Options / Examples

#### 'at -m time < filename'

Allows the user to run a set of commands in a file at a specified time.

~~~ bash
$ at -m noon < jobs.txt
commands will be executed using /bin/sh
job 1 at Mon Feb 18 12:00:00 2019
~~~

This will execute the commands in jobs.txt at noon.

#### 'at -r number'

Allows the user to delete a job that has been added

~~~ bash
$ at -r 4
~~~

This will delete job 4 from the queue.
'atrm' functions the same.

#### 'at -l'

Allows the user to view the current queue of jobs.

~~~ bash
$ at -l
1		Mon Feb 18 01:00:00
2		Wed Feb 20 20:40:33
~~~

#### Time expressions

'noon', 'midnight', 'tomorrow', 'next monday', etc. all work as expected. Other time expressions can be found in the 'at' documentation. 



