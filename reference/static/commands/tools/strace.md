strace
-------

strace will record system calls and signals when we run the specified command.

~~~ bash
$ strace <command>
~~~

---
#### A note
strace output is often extensive and hence too long to be presented
here in its entirety. Try for yourself to see the full output!

### Useful Options / Examples

#### Example command
The -c flag will present your output in a more readable way.
~~~ bash
$ strace - c <command>
<command output>
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.80    0.000080           0        14           <system call 1>
  0.05    0.000005           0         7         1 <system call 2>
  0.15    0.000015           0        26           <system call 3>
------ ----------- ----------- --------- --------- ----------------
100.00    0.000100                    47        1  total
~~~

#### Example command
The -o flag will print the output of strace to the specified file instead of to
standard output.

~~~ bash
$ strace - o output.txt <command>
<command output>
$ cat output.txt
<system call 1>(<argument>)                                = <signal 1>
<system call 2>(<argument>)                                = <signal 2>
<system call 3>(<argument>)                                = <signal 3>
+++ exited with <exit signal> +++
~~~
