kill
---

The *kill* command can be used to terminate a process without having to reboot the computer. Each running program is assigned a unique process identification number (PID) which is used by this command to reference the process.

~~~ bash
$ kill 1098
~~~

---

Rather than kill a process itself, this command sends a signal to a process. When no signal is provided as an argument, signal 15 (SIGTERM) is sent as a default. If this fails, signal 9 (SIGKILL) will then be used, which will guarantee termination (after waiting for the return of a system call if necessary). 

### Syntax

~~~ bash
$ kill [signal or option] PID(s)
~~~

### Process IDs

A PID is the only required argument to run this command, however multiple PIDs can be provided to be used in a single command.

To find the PID of a given process, use the ps command. ps aux returns all the running processes on a system, it can be used in conjunction with grep to find processes linked to a program name. 

~~~ bash
$ ps aux | grep -i "program name"
~~~

For example

~~~ bash
$ ps aux | grep -i "chrome"
User     6671   0.0  0.0  2444056    804 s000  S+   11:35AM   0:00.00 grep chrome
~~~

The ps options are:
* a = show processes for all users
* u = display the process's owner
* x = show all processes (not just those attached to the terminal)


### Signals

To view the full list of signals that can be used with the kill command, use the -l option. 
~~~ bash
$ kill -l
~~~

Some common signals apart from 9 and 15 are:

| Signal Name  &nbsp;   | Value           | Effect                                    |
|-----------------|-----------------|-------------------------------------------|
| SIGHUP          | 1               | Hangup                                    |
| SIGINT          | 2               | Interrupt from the keyboard               |
| SIGQUIT         | 3               | Quit process and dump core                |
| SIGKILL         | 9               | Kill process immediately, can't be caught |
| SIGSTOP         | 17, 19, 23 &nbsp; | Stop the process                          |

<br />
Here is an example of killing a process with a process value specified.
~~~ bash
$ kill -9 <process_id>
~~~

You may also use the *-s* flag or simply *-<FLAG_NAME>* to pass in symbolic names of each signal rather than the signal value itself.

For example

~~~ bash
$ kill -s HUP <process_id>
~~~



### killall

*killall* can also be used to kill a process by name rather than by PID.

The following command will terminate the process name chrome. It does not guarantee that all running chrome processes will terminate, so it may need to be used multiple times. 

~~~ bash
$ killall -9 chrome
~~~

