Shutdown
-------

The shutdown command can be be used on a Mac. It can also be used with or without delay. It is useful on your mac as well as if you spend any time remotely logged into Macs via the command line,  because it can be used to restart remote servers. 

~~~ bash
sudo shutdown -h now
~~~

---

### Useful Options / Examples

#### Example command
sudo shutdown -r now
##### Break it down
This restarts your mac immediately.

#### Example command
sudo shutdown -r +60

##### Break it down
This restarts your mac with a time delay. The 60 argument is the time delay in minutes.

