uptime
-------

Gives time for which the system has been up (or running).

~~~ bash
$ uptime
$ 11:56  up 13 days, 11:54, 3 users, load averages: 2.06 2.18 2.06
~~~

---

### Useful Options / Examples

#### Example command
~~~ bash
$ uptime
$ 11:56  up 13 days, 11:54, 3 users, load averages: 2.06 2.18 2.06
~~~

11:56 is the current time
13 days, 11:54 is total time for which the system has been up
3 users is how many users are currently logged on
2.06 is load average over the last minute
2.18 is load average over the last 5 minutes
2.06 is load average over the last 15 minutes

To learn more about load averages [click here](https://www.howtogeek.com/194642/understanding-the-load-average-on-linux-and-other-unix-like-systems/)

#### Example command
~~~ bash
$ uptime -p
$ up 29 weeks, 4 days, 11 hours, 1 minute
~~~

Outputs uptime in pretty format

### Example command
~~~ bash
$ uptime -s
$ 2018-11-10 20:14:15
~~~

Get time and date of when the system started

### Example command
~~~ bash
$ uptime -V
$ uptime from procps-ng 3.3.10
~~~

Gives version information

### Example command

~~~ bash
$ uptime -h
~~~

Gives information on all options in case you forget them.
