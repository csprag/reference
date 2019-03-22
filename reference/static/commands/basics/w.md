w
-------

`w` shows who is logged on and what they are doing, by displaying information about the users currently on the machine, and their processes.

The syntax is:

~~~ bash
$ w [options] user ...
~~~

---

A simple example would be:

~~~ bash
$ w
 18:01:11 up  5:54,  1 user,  load average: 1.24, 0.92, 0.58
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
agedeon  :0       :0               17:50   ?xdm?   7:28   0.12s /sbin/upstart --user
~~~

---
### Output Description

The header for the `w` command shows the following (in this order): the current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes.

The following entries are displayed for each user: the login name, the tty name, the remote host, login time, idle time, JCPU, PCPU, and the command line of their current process.

The JCPU time is the time used by all processes attached to the tty. It does not include past background jobs, but does include currently running background jobs.

The PCPU time is the time used by the current process, named in the "what" field.


---

### Useful Options / Examples

#### `w -h`

The `-h` flag prevents the header from being printed.

~~~ bash
$ w -h
agedeon  :0       :0               17:50   ?xdm?   9:27   0.12s /sbin/upstart --user
~~~

#### `w -s`

The `-s` flag uses the short format, meaning the login time, JCPU, and PCPU is omitted.

~~~ bash
$ w -s
 18:28:26 up  6:15,  1 user,  load average: 0.45, 0.33, 0.37
USER     TTY      FROM              IDLE WHAT
agedeon  :0       :0               ?xdm?  /sbin/upstart --user
~~~

#### `w -f`

The `-f` flag toggles printing the "FROM" field.

~~~ bash
$ w -f
 18:34:41 up  6:21,  1 user,  load average: 0.04, 0.12, 0.25
USER     TTY        LOGIN@   IDLE   JCPU   PCPU WHAT
agedeon  :0        17:50   ?xdm?  10:25   0.12s /sbin/upstart --user
~~~

#### `w -V`

The `-V` flag displays version information.

~~~ bash
$ w -V
w from procps-ng 3.3.12
~~~

#### `w [user]`

The `[user]` parameter shows information for the specified user only.

~~~ bash
$ w agedeon
 18:45:48 up  6:33,  1 user,  load average: 0.04, 0.13, 0.17
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
agedeon  :0       :0               17:50   ?xdm?  11:30   0.12s /sbin/upstart --user
~~~