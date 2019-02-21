head
-------

'env' is used to obtain the current environment or run another program in a custom environment without having to
modify the current environment.

~~~ bash
$ env
HOSTNAME=861d736c60b8
TERM=xterm-256color
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/bin:/sbin:.:/usr/share/smlnj/bin
PWD=/home/cg/root
SHLVL=1
HOME=/
_=/usr/bin/env
~~~

---

### Useful Options / Examples
When inputted without arguments, 'env' prints a list of all the environments.
#### Example command
The -i argument starts with an empty environment

$ env -i /bin/sh
$ env
PWD=/home/ubuntu
#### Example command
LOGPATH can be used to set a specifc environment variable

$ env LOGPATH=/var/log
HOSTNAME=861d736c60b8
TERM=xterm-256color
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/bin:/sbin:.:/usr/share/smlnj/bin
PWD=/home/cg/root
SHLVL=1
HOME=/
_=/usr/bin/env
LOGPATH=/var/log
##### Example command
The -u flag removes a variable from the environment

$ env -u LOGPATH
HOSTNAME=861d736c60b8
TERM=xterm-256color
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/bin:/sbin:.:/usr/share/smlnj/bin
PWD=/home/cg/root
SHLVL=1
HOME=/
_=/usr/bin/env
##### Example command
'env' can also be used inside of a script in the hashbang line to modify the interpreter

test.py:
#!/usr/bin/env python2
print "Hello World."

$ python test.py
Hello World.
