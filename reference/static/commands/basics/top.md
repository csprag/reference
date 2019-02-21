top
---
`top` is used to show the list of current processes and usage of the system's resources
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ top
interactive command line application
$ q
quits application
~~~

---

### Useful Options / Examples
The top half of the application shows the statistics on processes and resource usage, like system time, uptime, number of tasks running, cpu usage, etc.

The bottom half displays a list of the currently running processes, to scroll through the list you can use the up and down arrow keys.

Hit q to close the top application. The options for top are all case sensitive.

#### Example command
While top is open, you can sort the list of processes as well, here are some common ways (case sensitive):

$ top 
$ [MPNT] 

##### Break it down
With the application open, it will sort the list of processes by the corresponding metric:
'M': sort by memory usage
'P': sort by CPU usage
'N': sort by process ID number
'T': sort by running time

This will sort the list of process in descending order. To change it to ascending order, 'R' will do the trick.

$ top -o %CPU
This is another command to sort, this example will sort by CPU usage.

#### Example command
Other options in top:

$ top
$ [tmHk]

##### Break it down
't' and 'm' will change the layout of the display of the top statistic part, for the CPU usage and memory portions, respectively. Repeatedly hitting 't' or 'm' will cycle through the possible configurations.

'H' will change the output to display threads instead of tasks at the top of the screen. 

'k' will kill a process. Input 'k', and you'll be prompted to input a PID (first column on the left). Input the PID, and hit enter when prompted again and the process will be killed.

