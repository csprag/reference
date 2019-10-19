ifconfig
-------

ifconfig (interface configuration) is used to view and configure network interfaces on your system.

~~~ bash
$ ifconfig
ifconfig eth0
~~~

---

### Useful Options / Examples

#### 'ifconfig'

~~~ bash
ifconfig
~~~
This command gives information on all network interfaces currently in operation. Outputs information similar to 
~~~ bash
eth0      Link encap:Ethernet  HWaddr 09:00:12:90:e3:e5  
          inet addr:192.168.1.29 Bcast:192.168.1.255  Mask:255.255.255.
          inet6 addr: fe80::a00:27ff:fe70:e3f5/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:54071 errors:1 dropped:0 overruns:0 frame:0
          TX packets:48515 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:22009423 (20.9 MiB)  TX bytes:25690847 (24.5 MiB)
          Interrupt:10 Base address:0xd020</span>
~~~
Here eth0 refers to the first ethernet interface. Other ethernet interfaces would be named eth1,eth2 etc. Other common interfaces include lo the loopback interface the system uses to communicate with itself, wlan for wireless network interfaces and usb for networks over usb.
  The -a option displays all network interfaces, not just those in use. A specific network interface can also be specified such as
~~~ bash
ifconfig eth0
~~~

#### 'ifconfig <interface> up' or 'ifconfig <interface> down'
~~~ bash
ifconfig eth0 up
ifconfig eth0 down
~~~
These commands simply let you enable or disable a specific network interface, in this case the first ethernet network.

#### Assigning an IP, netmask and broadcast to a network
~~~ bash
sudo ifconfig eth0 192.168.7.2
sudo ifconfig eth0 netmask 255.255.255.0
sudo ifconfig eth0 broadcast 172.16.25.98
sudo ifconfig eth0 192.168.7.2 netmask 255.255.255.0 broadcast 172.16.25.98
~~~
A static ip can be assigned simply by specifying a network and providing a number as seen in the first command. A netmask can be assigned by specifiying the network, typing netmask to specify that you want to assign the netmask and providing the netmask address. Broadcast can be set the same way except by specifiying broadcast instead of netmask. These commands can all be combined into one single command as in the last command.

#### Creating an alias for a network
~~~bash
ifconfig eth0:0 172.16.25.127
~~~
This command lets you create an alias for your network interface. The alias created here is referred to as eth0:0 and the ip provided must be the same as the ip of the original network. Other aliases can be created similarly such as eth0:1. In this case 172.16.25.127 is the ip of both eth0 and eth0:0.This command is useful if you need multiple ips on a single network This alias can be removed by disabling network interface
~~~bash
ifconfig eth0:0 down
~~~

#### Changing the MAC address.
~~~ bash
ifconfig eth0 hw ether AA::BB::CC::DD::EE::FF
~~~
This command lets you change the mac adress of a specific network adress. Similarly to changing the netmask and broadcast, first you specify the network your changing (eth0), followed by hw ether to indicate you are changing the mac adress, and providing the MAC address you want to change to(AA::BB::CC::DD::EE::FF).

#### Creating an alias for a network
~~~bash
ifconfig eth0:0 172.16.25.127
~~~
This command lets you create an alias for your network interface. The alias created here is referred to as eth0:0 and the ip provided must be the same as the ip of the original network. Other aliases can be created similarly such as eth0:1. In this case 172.16.25.127 is the ip of both eth0 and eth0:0.This command is useful if you need multiple ips on a single network This alias can be removed by disabling network interface
~~~bash
ifconfig eth0:0 down
~~~
#### Changing maximum transmission unit
~~~ bash
ifconfig eth0 mtu 1000
~~~
This command allows you to set the maximum transmission unit. Larger mtus allow for more efficient transfer of data as more data can be transmitted in less packets but this delays the time between packets.

### Side note on deprecation
ifconfig is currently deprecated in favor of the ip command. In the future consider using the ip command for easier use and better tools.
