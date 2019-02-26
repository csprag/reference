hostname
-------

The name that one has assigned to their computer is called a host name. A host name is how one's computer is recognized on a local network, and hostname is a command which allows the user to view this name as well as something called the domain name (which is the address that uniquely identifies the machine). This post and the flags used in it are geared toward Linux users. The following lines are an example of using hostname in a machine called daniel-VirtualBox

~~~ daniel@daniel-VirtualBox:/$
hostname
daniel-VirtualBox
~~~

---

### Useful Options / Examples

#### sudo hostname

##### If you're using Linux, this command allows you to change or set the hostname of your system

~~~ daniel@daniel-VirtualBox:/$
sudo hostname changedname
[sudo] password for daniel:
daniel@daniel-VirtualBox:/$ hostname
changedname
~~~

#### -i flag

##### Displays network address

~~~ daniel@daniel-VirtualBox:/$
hostname -i
34.234.89.0
~~~

#### -d flag

##### Displays name of the DNS domain

~~~ daniel@daniel-VirtualBox:/$
hostname -d
hsd1.mi.comcast.net
~~~
