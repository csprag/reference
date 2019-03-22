ping
-------

Ping (Packet Internet Groper) is a network administration utility used to check the connectivity status between a source and a destination computer/device over an IP network. It also helps you assess the time it takes to send and receive a response from the network. You can check if a host is alive or not through the following ping command: (ctrl+c to exit)
~~~ bash
$ ping "host-name/IP"
PING "host-name/IP" ("host-name/IP") 56(84) bytes of data.
64 bytes from "host-name/IP": icmp_seq=1 ttl=54 time=16.0 ms
64 bytes from "host-name/IP": icmp_seq=2 ttl=54 time=15.3 ms
^C
--- "host-name/IP" ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 15.356/15.682/16.009/0.349 ms
~~~

---

### Useful Options / Examples

#### `ping -c NumberOfPackets host-name/IP`

~~~ bash
$ ping -c 5 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=54 time=17.0 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=54 time=16.8 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=54 time=17.9 ms
64 bytes from 1.1.1.1: icmp_seq=4 ttl=54 time=14.6 ms
64 bytes from 1.1.1.1: icmp_seq=5 ttl=54 time=15.5 ms

--- 1.1.1.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4018ms
rtt min/avg/max/mdev = 14.643/16.384/17.903/1.157 ms
~~~

##### Break it down

* You can set ping to send a specific number of packets (thus avoiding having to ctrl+c exit) by using this command.

#### `ping -w TimeInSeconds host-name/IP`

~~~ bash
$ ping -w 4 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=54 time=15.6 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=54 time=19.5 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=54 time=15.5 ms
64 bytes from 1.1.1.1: icmp_seq=4 ttl=54 time=16.2 ms

--- 1.1.1.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 15.577/16.774/19.557/1.629 ms
~~~

##### Break it down

* Another way to avoid exiting manually is to set a time limit for ping after which it will exit no matter how many ping packets were sent/received.
