who
-------

`who` prints out all usernames currently logged in

~~~ bash
$ who -a
       system boot  2019-02-16 07:00
       run-level 5  2019-02-16 07:07
user  + pts/0       2019-02-16 12:00 (:0.0)
user2 - pts/1       2019-02-16 11:23 (127.0.0.1)
$ who -q
user user2
# users=2
~~~

---

### Description
Who is used to print out all of the users logged in, with the time and date logged in, along
as the IP address used to connect and the pseudo terminal connected with. If connected remotely, 
the remote IP is displayed, or if locally, the IP of (:0.0) is displayed. Each user logged in has
their own pseudo terminal, with indexing starting at 0, displayed as pts/0. The + or - symbol means
that the user is accepting messages from other users, by mesg pr wall command.

### Syntax
~~~bash
who [options] [file] [am i]
~~~

options can be added to change the output format of the info displayed.

file is a location to search for current users. Defaults to /var/run/utmp if not specified.

am i displays only information about current user, and no one else.

### Useful Options / Examples
~~~bash
who 
    -a, --all
    -m
    -q, --count
    -u
~~~

-a is used to print all infomation that the who command can provide.
All users, systems, message states, times, dates, and IP info is displayed.

-m is an alias for who am i, which only displays info about self.

-q provides a list of all usernames logged in, as well as a count of total users logged in.

-u provides a full list similar to -a, but is limited to only physical users and not system processes.

#### Example command
~~~bash
$ who -a
          system boot  2019-02-14 07:00
          run-level 5  2019-02-14 07:07
user1  +  pts/0        2019-02-16 23:36   .   (11.1.1.1)
user2  +  pts/1        2019-02-16 18:31 01:26 (222.2.22.2)
user3  +  pts/2        2019-02-16 19:51 04:21 (3.33.333.33)
user4  -  pts/3        2019-02-16 21:36   .   (44.44.44.4)
~~~
##### Break it down
By running who without any options, it displays (only) users currently logged in.
The first field returned is the user's username.
The second field is an indicator whether that user can receive messages from the terminal.
The third field returned is a "pseudo terminal slave", which is a numerical number
sequencially assigned to users to differentiate them.
The fourth field is the date that the user logged in.
The fifth field is the time that the user logged in.
The sixth field is the time since the user has been active (idle time).
The seventh field is the IP address of the user.