ssh
-------

`ssh` allows the shell to open a secure connection to a remote machine. Once connected, it can retrieve files from and execute commands on the remote machine. 

~~~ bash
$ ssh uniqname@login.engin.umich.edu
~~~

---
### History

SSH replaced Telnet and rlogin as the main mechanism for logging into remote directories. Previously, data was passed as plain text between the host and remote machines. This led to many security breaches and the need for a more secure protocol: SSH. SSH allows users to securely log from one machine into another, even over an insecure network. 

### Basic Usage

Look at the above command: 
~~~bash
$ ssh uniqname@login.engin.umich.edu
~~~
Only one argument is passed into ssh. This argument actually includes two pieces of data: a username and a remote machine. In this case the username is "uniqname", while the remote machine is located at "login.engin.umich.edu". 

SSH can execute a command immediatly after connecting to the remote machine. This occurs if the user specifies a second argument as is done below: 
~~~bash
$ ssh uniqname@login.engin.umich.edu ls
~~~
The above line will first establish a connection to the server "login.engin.umich.edu" using the username "uniqname", then it will execute the command "ls" on the remote directory, and finally it will return to the host directory. The key difference here is that ssh does not return to the host directory if no command is specified. 

---
### Useful Flags
---
#### -l

The -l flag allows the user to specify the target username separately from the location of the remote directory. The initial example: 
~~~bash
$ ssh uniqname@login.engin.umich.edu
~~~
can be rewritten: 
~~~bash
$ ssh -l uniqname login.engin.umich.edu
~~~

#### -x

The -x flag enables "X11 Forwarding". If you launch a GUI application in a remote directory, that GUI is not displayed on your host computer by default. It will run on the remote directory and you will not be able to view it because the SSH was opened purely as a text-based connection. With -x included, the GUI will be drawn on your screen, even though the executable itself is run on the remote machine. 
~~~bash
$ ssh -x uniqname@login.engin.umich.edu
~~~

