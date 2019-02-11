bg
-------

bg starts a suspended job in the background or moves a job to the background

~~~ bash
$ bg gedit
[1]+ gedit &
~~~

---

### Useful Options / Examples
`bg` is often used to start a background process after `CTRL + Z` is used to suspend the job. In this case, launching gedit results in an unresponsive command line. Pressing `CTRL + Z` suspends the jobs and the `bg` command allows the job to run again in the background.
~~~bash
$ gedit
^Z
[1]+  Stopped                 gedit
$ bg gedit
[1]+ gedit &
~~~
---
The `&` operator can be added to the end of a command to start the process in the background.
~~~bash
$ vim &
$ jobs
[1]+  Stopped                 vim
~~~
---
`jobs` shows a current list of processes. The number in the brackets represents the job number. Next to that, a `+` or `-` sign can appear. The `+` indicates that the job was the last one to be suspended from the foreground. The `-` indicates any other suspended job.
~~~bash
$ jobs
[1]+  Stopped                 gedit
[2]-  Stopped                 gnome-calculator
~~~
Once the job number for a process is known, the `%` operator combined with the job number can be used to start that specific task. In this case, gnome calculator is job one and using `bg %1` starts that job in the background. The `&` that follows indicates that the job is running in the background.
~~~bash
$ jobs
[1]-  Stopped                 gnome-calculator
[2]+  Stopped                 gedit
$ bg %1
[1]- gnome-calculator &
~~~
---
If no job is specified after `bg` the jobs that was last suspended will start running in the background. This is indicated by the job with the `+` symbol.
~~~bash
$ jobs
[1]-  Stopped                 gnome-calculator
[2]+  Stopped                 gedit
$ bg
[2]+ gedit &
~~~
---
`help bg` provides documentation on how to use `bg`
~~~bash
$ help bg
bg: bg [job_spec ...]
    Move jobs to the background.

    Place the jobs identified by each JOB_SPEC in the background, as if they
    had been started with `&'.  If JOB_SPEC is not present, the shell's notion
    of the current job is used.

    Exit Status:
    Returns success unless job control is not enabled or an error occurs.
~~~
---
