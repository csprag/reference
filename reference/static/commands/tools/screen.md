screen
-------
`screen` allows users to create a screen session that will not terminate even after the terminal window is closed. That said, it allows users to perfrom a long-running task on a remote server, and the process will continue running even if users disconnect from the server, so that you don't lose your work when your connection suddenly drops. 
~~~ bash
$ screen
$ screen -ls
There are screens on:
        50180.pts-16.gelato     (10/12/2019 02:25:25 AM)        (Detached)
        50067.pts-16.gelato     (10/12/2019 02:22:47 AM)        (Detached)
        377316.pts-21.gelato    (10/02/2019 01:22:59 AM)        (Detached)
        26961.pts-14.gelato     (09/21/2019 02:50:37 PM)        (Detached)
4 Sockets in /var/run/screen/S-xxxxx.
$ screen -r 377316
$ screen -X -S 377316 quit
~~~

---

### Useful Options / Examples

#### `screen`
~~~ bash
$ screen
~~~

To start a screen session, simply type `screen`. Once it is done, it creates a single window with a shell in it. Each screen session has an ID that we can track with. Users can create more than one screen session; just type `screen` again to start another one. 

#### `Ctrl+a d`
~~~ bash
Ctrl+a d
[detached from 377316.pts-21.gelato]
~~~

This allows you to detach from the screen session. Afterwards, you will come back to your normal terminal console. In this example, we have detached from session 377316.pts-21.


 #### `screen -ls`
~~~ bash
$ screen -ls
There are screens on:
        50180.pts-16.gelato     (10/12/2019 02:25:25 AM)        (Detached)
        50067.pts-16.gelato     (10/12/2019 02:22:47 AM)        (Detached)
        377316.pts-21.gelato    (10/02/2019 01:22:59 AM)        (Attached)
        26961.pts-14.gelato     (09/21/2019 02:50:37 PM)        (Detached)
4 Sockets in /var/run/screen/S-xxxxx.
~~~
Use this command to find the session ID list of current running screen sessions. In this example, we have created four screen sessions in total and we are currently inside screen 377316.pts-21.

 #### `screen -r [session # you want to resume]`
~~~ bash
$ screen -r 377316
~~~

This allows you to resume a screen session. Before you can resume a screen session, you must detach from this screen. In this example, we have restored screen 377316.pts-21.

 #### `screen -X -S [session # you want to kill] quit`
~~~ bash
$ screen -X -S 377316 quit
~~~

This allows you to kill the complete session. If you are inside the screen and you want to kill it, you can simply type `exit` alternatively. 
