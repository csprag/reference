shutdown
---

`shutdown` schedules a shutdown of the system, by default one minute after the current time.

~~~ bash
$ shutdown [options]
Shutdown scheduled for Mon 2019-10-21 22:33:28 EDT, use 'shutdown -c' to cancel.
~~~

---

### Useful Options / Information 

#### `shutdown -r`

Reboots the system instead of shutting it down.

#### `shutdown -c`

Cancels a previously scheduled shutdown.

#### `shutdown -h now`

~~~ bash
$ shutdown -h now
~~~

##### Break it down

* `-h` powers off the machine
* `now` schedules the shutdown for right now, instead of the default one minute after the current time.

#### `shutdown +10`

Schedules the shutdown for ten minutes from now. 10 can be replaced by the desired shutdown timer.

#### `shutdown 15:35`

Schedules the shutdown for 3:35pm. 15:35 can be replaced by the desired shutdown time.
