sleep
-------

When sleep number[smhd] is called, the script or terminal will wait for that period of time.
If no time unit is specified, sleep will default to seconds

~~~ bash
$ sleep 1s
~~~

---

### Useful Options/Examples
There are four time units that can be used
's' - seconds
'm' - minutes
'h' - hours
'd' - days

When multiple inputs are given, the times are added together
~~~ bash
$ sleep 2m 3s
~~~
Terminal will sleep for 2 minutes and 3 seconds

~~~ bash
$ sleep 3s 3s
~~~
Terminal will sleep for 6 seconds

Floating point input is also allowed
~~~ bash
$ sleep 0.5m
~~~
Terminal will sleep for 30 seconds

#### sleep --help

##### Will print all the options and functions of sleep and then exit 

#### sleep --version

##### Will print the current version of sleep
