strace
-------

strace will record system calls and signals when we run the specified command.

~~~ bash
$ strace <command>
~~~

---
#### A note
strace output is often extensive and hence too long to be presented
here in its entirety. The -c flag is very useful for condensing the output
to a more readable form. Try for yourself to see the full output!

### Useful Options / Examples

#### Example command
The -c flag will present your output in a more readable way.
~~~ bash
$ strace -c <command>
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

#### Example of real output
This example shows strace output when used on a simple C-program.

The program is a simple Hello World-program, helloworld.c:
~~~ c
#include <stdio.h>

int main() {
    printf("Hello World\n");

    return 0;
}
~~~

The output from strace will be:

~~~ bash
$ cc helloworld.c -o helloworld
$ strace - c ./helloworld
Hello World
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         1           read
  0.00    0.000000           0         1           write
  0.00    0.000000           0         2           close
  0.00    0.000000           0         3           fstat
  0.00    0.000000           0         5           mmap
  0.00    0.000000           0         4           mprotect
  0.00    0.000000           0         1           munmap
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         1           ioctl
  0.00    0.000000           0         3         3 access
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           arch_prctl
  0.00    0.000000           0         2           openat
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                    28         3 total
~~~
