top
---
`top` is used to show the list of current processes and usage of the system's resources
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ top
$ q
~~~

'top' opens the interactive command line application
'q' quits the application

---

### Useful Options / Examples
The top half of the application shows the statistics on processes and resource usage, like system time, uptime, number of tasks running, cpu usage, etc.

The bottom half displays a list of the currently running processes, to scroll through the list you can use the up and down arrow keys.

Hit q to close the top application. The options for top are all case sensitive.

Example of the top's interface:

top - 15:06:16 up 0 min,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.9 us,  3.9 sy,  0.0 ni, 90.4 id,  0.0 wa,  0.8 hi,  0.0 si,  0.0 st
MiB Mem :   8087.3 total,   4839.6 free,   3023.7 used,    224.0 buff/cache
MiB Swap:  24576.0 total,  24563.2 free,     12.8 used.   4933.0 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8304    132    104 S   0.0   0.0   0:00.18 init
    3 root      20   0    8304     92     56 S   0.0   0.0   0:00.00 init
    4 root      20   0   16436   3536   3428 S   0.0   0.0   0:00.16 bash
   70 root      20   0   17276   2036   1452 R   0.0   0.0   0:00.05 top

#### Example command
While top is open, you can sort the list of processes as well, here are some common ways (case sensitive):

~~~ bash
$ top 
$ [MPNT]
~~~ 

##### Break it down
With the application open, it will sort the list of processes by the corresponding metric:
'M': sort by memory usage
'P': sort by CPU usage
'N': sort by process ID number
'T': sort by running time

Example of sorting using 'M':
Before:
top - 15:26:57 up 20 min,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):  3.9 us,  5.4 sy,  0.0 ni, 89.5 id,  0.0 wa,  1.1 hi,  0.0 si,  0.0 st
MiB Mem :   8087.3 total,   4949.4 free,   2913.9 used,    224.0 buff/cache
MiB Swap:  24576.0 total,  24558.7 free,     17.3 used.   5042.8 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8304    132    104 S   0.0   0.0   0:00.18 init
    3 root      20   0    8304     92     56 S   0.0   0.0   0:00.00 init
    4 root      20   0   16436   3536   3432 S   0.0   0.0   0:00.16 bash
   71 root      20   0   17276   1968   1388 R   0.0   0.0   0:00.03 top

After:
top - 15:26:57 up 20 min,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):  3.9 us,  5.4 sy,  0.0 ni, 89.5 id,  0.0 wa,  1.1 hi,  0.0 si,  0.0 st
MiB Mem :   8087.3 total,   4949.4 free,   2913.9 used,    224.0 buff/cache
MiB Swap:  24576.0 total,  24558.7 free,     17.3 used.   5042.8 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    4 root      20   0   16436   3536   3432 S   0.0   0.0   0:00.16 bash
   71 root      20   0   17276   2036   1452 R   0.0   0.0   0:00.06 top
    1 root      20   0    8304    132    104 S   0.0   0.0   0:00.18 init
    3 root      20   0    8304     92     56 S   0.0   0.0   0:00.00 init

This will sort the list of process in descending order. To change it to ascending order, 'R' will do the trick.


There are other commands to sort, with the following sorting by CPU usage.

~~~ bash
$ top -o %CPU
~~~


#### Example command
Other options in top which lets users modify the display:

~~~ bash
$ top
$ [tmHk]
~~~

##### Break it down
't' and 'm' will change the layout of the display of the top statistic part, for the CPU usage and memory portions, respectively. Repeatedly hitting 't' or 'm' will cycle through the possible configurations.

After inputting 't' then 'm' the interface looks like this:

top - 15:20:45 up 14 min,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):   1.2/1.9     3[|||                                                                                          ]
MiB Mem : 37.5/8087.3   [|||||||||||||||||||||||||||||||||||                                                          ]
MiB Swap:  0.1/24576.0  [                                                                                             ]

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8304    132    104 S   0.0   0.0   0:00.18 init
    3 root      20   0    8304     92     56 S   0.0   0.0   0:00.00 init
    4 root      20   0   16436   3536   3428 S   0.0   0.0   0:00.16 bash
   70 root      20   0   17276   2040   1456 R   0.0   0.0   0:00.70 top

'H' will change the output to display threads instead of tasks at the top of the screen. The second line now displays
"Threads", versus the "Tasks" shown above.

top - 15:22:25 up 16 min,  0 users,  load average: 0.52, 0.58, 0.59
Threads:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):   6.1/9.6    16[|||||||||||||||                                                                              ]
MiB Mem : 37.5/8087.3   [|||||||||||||||||||||||||||||||||||                                                          ]
MiB Swap:  0.1/24576.0  [                                                                                             ]

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8304    132    104 S   0.0   0.0   0:00.18 init
    3 root      20   0    8304     92     56 S   0.0   0.0   0:00.00 init
    4 root      20   0   16436   3536   3428 S   0.0   0.0   0:00.16 bash
   70 root      20   0   17276   2076   1460 R   0.0   0.0   0:00.76 top

'k' will kill a process. Input 'k', and you'll be prompted to input a PID (first column on the left). Input the PID, and hit enter when prompted again and the process will be killed. Hit Esc to exit the kill prompt. 

top - 15:23:02 up 16 min,  0 users,  load average: 0.52, 0.58, 0.59
Threads:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):   3.0/3.4     6[||||||                                                                                       ]
MiB Mem : 37.6/8087.3   [|||||||||||||||||||||||||||||||||||                                                          ]
MiB Swap:  0.1/24576.0  [                                                                                             ]
PID to signal/kill [default pid = 1] [User inputted PID will show up here]
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8304    132    104 S   0.0   0.0   0:00.18 init
    3 root      20   0    8304     92     56 S   0.0   0.0   0:00.00 init
    4 root      20   0   16436   3536   3428 S   0.0   0.0   0:00.16 bash
   70 root      20   0   17276   2076   1460 R   0.0   0.0   0:00.78 top

