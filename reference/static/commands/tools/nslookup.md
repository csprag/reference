nslookup
-------
nslookup (short for "name server lookup") is used to query the Domain Name System (DNS) for domain name and IP address information. 
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ nslookup [-option] [name | -] [server]
~~~

---

## Useful Options / Examples

### Non-Interactive Mode
Non-interactive mode is used to print the name and requested information for a host or domain. This mode is entered by default when the name or Internet address of the host to be looked up is given as the first argument. An optional second argument can be used to specify the host name or address of a name server.

#### Finding the IP address of a domain
`$ nslookup [name] [server]` can be used to find the IP address of a domain. For example,

`$ nslookup google.com`

prints the name and address of the answering DNS server, then the name and IP address associated with the query:
~~~ bash
Server:         10.10.10.10
Address:        10.10.10.10.10#53

Non-authoritative answer:
Name:   google.com
Address: 216.58.216.78
~~~
(Non-authoritative answer means that the server queried does not host the domain name associated with the query)


#### Finding the domain name of an IP address
`$ nslookup [address] [server]` can be used to find the domain of an IP address. For example,

`$ nslookup 141.211.243.251 8.8.8.8`

prints the name and address of the answering DNS server, then the domain name  associated with the query:
~~~ bash
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
251.243.211.141.in-addr.arpa    name = www.umich.edu  
~~~


#### Finding the mail servers for a domain
`$ nslookup -query=mx [name]` can be used to find mail servers for a domain. For example,

`$ nslookup -query=mx gmail.com`

prints the name and address of the answering name server, then a list of servers:
~~~ bash
Server:         10.10.10.10
Address:        10.10.10.10.10#53

Non-authoritative answer:
gmail.com	mail exchanger = 5 gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 10 alt1.gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 40 alt4.gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 30 alt3.gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 20 alt2.gmail-smtp-in.l.google.com.
~~~

 
### Interactive Mode
Interactive Mode can be entered in two ways:
1. No arguments are provided (`$ nslookup`)
2. The first argument is a hyphen and the second argument is the host name or Internet address of a name server (`$ nslookup - [name | address]`)

This will present a prompt from which you can issue interactive commands:
~~~ bash
$ nslookup
>
~~~

 
#### Examples
###### Display the default domain name server used for queries with `server`
~~~ bash
> server
Default server: 10.10.10.10
Address: 10.10.10.10#53
Default server: 10.10.5.5       
Address: 10.10.5.5#53
>
~~~

###### Change the domain name server that will be used for queries with `server [name | address]`
~~~ bash
> server 8.8.4.4
Default server: 8.8.4.4
Address: 8.8.4.4#53
>
~~~

###### Display the IP addresses associated with a domain 
~~~ bash
> umich.edu
Server:         10.10.10.10
Address:        10.10.10.10#53

Non-authoritative answer:
Name:   www.umich.edu
Address: 141.211.243.251
>
~~~

###### Display the domain name associated with an IP address
~~~ bash
> 141.211.243.251
Server:         10.10.10.10
Address:        10.10.10.10#53

Non-authoritative answer:
251.243.211.141.in-addr.arpa	name = www.umich.edu
>
~~~

###### Change the query type to find mail servers for a domain with `set type=mx`
~~~ bash
> set type=mx
> umich.edu
Server:         10.10.10.10
Address:        10.10.10.10#53

Non-authoritative answer:
umich.edu mail exchanger = 0 mx1.a.mail.umich.edu.
>
~~~

###### Change the query type back to name-address mapping with `set type=a`
~~~ bash
> set type=a
>
~~~

###### Exit interactive mode
~~~ bash
> exit

$
~~~


