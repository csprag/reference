df
-------

df is a UNIX and Linux command for reporting file system disk space usage.

~~~ bash
$ df
Filesystem    512-blocks      Used Available Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   976490576 220250560 748549912    23% 2716011 9223372036852059796    0%   /
devfs                373       373         0   100%     646                   0  100%   /dev
/dev/disk1s4   976490576   6291496 748549912     1%       3 9223372036854775804    0%   /private/var/vm
map -hosts             0         0         0   100%       0                   0  100%   /net
map auto_home          0         0         0   100%       0                   0  100%   /home
~~~

---

Filesystem - the filesystem on the machine<br/>
Used - the amount of space used in 512-byte blocks (on Mac)<br/>
Available - the amount of available space in 512-byte blocks<br/>
Use% - the percentage that the filesystem is in use<br/>
Mounted on - where the filesystem is mounted<br/>

### Useful Options / Examples

The -h flag prints it in a more human readable format

#### Example command

~~~ bash
$ df -h
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   466Gi  105Gi  357Gi    23% 2716179 9223372036852059628    0%   /
devfs          187Ki  187Ki    0Bi   100%     646                   0  100%   /dev
/dev/disk1s4   466Gi  3.0Gi  357Gi     1%       3 9223372036854775804    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
~~~

##### Break it down
This prints sizes in powers of 1024 and will append G for gigabytes, M for megabytes and B for bytes.

#### Example command
The -Ht flag shows the space available, filesystem and mount point for a folder

~~~ bash
$ df -Ht Desktop/eecs201
Filesystem     Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   500G   113G   383G    23% 2716179 9223372036852059628    0%   /
~~~

##### Break it down
The output of this shows where the filesystem type, and where it is mounted. This can be useful if you are administering a server or machine and are unsure where a folder is mounted.
