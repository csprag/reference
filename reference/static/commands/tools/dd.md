dd
-------

dd is a tool used primarily for converting/copying files.
dd is a command unlike most unix commands in that the syntax uses option=value syntax. 

~~~ bash
$ dd if = <source file name> of=<target file name> [options]
~~~

---

### Practical examples:

#### Backup an entire hard drive
~~~bash
$ dd if = /dev/hda of = /dev/hdb
~~~

This example is an example of how to back up a hard drive to another hard drive also connected to the system. The source hard drive is /dev/sda and the target is located at /dev/hdb.

#### Backup a parition to an image file
~~~bash
$ dd if = /dev/hda of = ~/partition.img
~~~

This example is quite similar to the first. Use the device name of a partition as the input file and specify the target path as shown.

####  Create image of a hard drive 
~~~bash
$ dd if = /dev/hda of = ~/hdadisk.img
~~~

This example would be used to backup the state of a hard drive into a new image file.

#### Restore using a hard drive image
~~~bash
$ dd if = hdadisk.img of = /dev/hdb
~~~
This example would be used to load any of the images saved in previous examples into the hard drive. 

### Options:
if=FILE - read file<br/>
of=FILE - output file<br/>
ibs=BYTES - Read BYTES at a time<br/>
obs=BYTES - Write BYTES at a time<br/>
skip=BLOCKS - Skip BLOCKS blocks in the input file before copying<br/>
seek=BLOCKS - Skip BLOCKS blocks in the output file before copying<br/>
count=BLOCKS - Copy BLOCKS blocks from the input file before copying.<br/>
