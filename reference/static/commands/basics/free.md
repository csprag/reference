free
-------

`$ free [OPTIONS]`

free shows a summary of the memory usage in the system, for RAM and swap memory. It shows
total, used, free, shared, buff/cache, and available memory. With no options it displays
values in KB but can be configured to use different units.

~~~ bash
$ free
              total        used        free      shared  buff/cache   available
Mem:       16506956     7115500     9162104       17720      229352     9257724
Swap:      29312892           0    29312892
~~~

---

### Useful Options

-b, --bytes : displays the memory in bytes. <br />
-k, --kilo : displays the amount of memory in kilobytes (default). <br />
-m, --mega : displays the amount of memory in megabytes. <br />
-g, --giga : displays the amount of memory in gigabytes. <br />
&nbsp;&nbsp;&nbsp;&nbsp; --tera : displays the amount of memory in terabytes. <br />
-h, --human : shows all output columns scaled to shortest three digit unit and display the units: B(bytes), K(kilos), M(megas), G(gigas), and T(teras). <br />
&nbsp;&nbsp;&nbsp;&nbsp; --si : shows the output in powers of 1000 instead of 1024. <br /><br />
-c N, --count N : displays the output N number of times and this option actually works with -s option. <br />
-s N, --seconds N : allows you to display the output continuously after an N seconds delay. <br />
-t,   --total : adds an additional line in the output showing the column totals. <br />
&nbsp;&nbsp;&nbsp;&nbsp; --help : displays a help message and exits. <br />
-V,   --version : It displays version info and exits.


### Examples
`free -h` is used to see memory allocation in a human readable format
~~~bash
$ free
              total        used        free      shared  buff/cache   available
Mem:            15G        7.0G        8.6G         17M        223M        8.6G
Swap:           27G          0B         27G
~~~
---
`free --si` is used to see memory allocation in powers of 1000
~~~bash
$ free
              total        used        free      shared  buff/cache   available
Mem:       16506956     7618744     8658860       17720      229352     8754480
Swap:      29312892           0    29312892
$ free --si
              total        used        free      shared  buff/cache   available
Mem:       16506956     7617176     8660428       17720      229352     8756048
Swap:      29312892           0    29312892
~~~
---
`-c N` and `-s N` can be combined to show multiple outputs each after a delay of N seconds
~~~bash
$ free -c 3 -s 3

//3 second delay 
              total        used        free      shared  buff/cache   available
Mem:       16506956     7535312     8742292       17720      229352     8837912
Swap:      29312892           0    29312892

//3 second delay
              total        used        free      shared  buff/cache   available
Mem:       16506956     7535168     8742436       17720      229352     8838056
Swap:      29312892           0    29312892

//3 second delay
              total        used        free      shared  buff/cache   available
Mem:       16506956     7533668     8743936       17720      229352     8839556
Swap:      29312892           0    29312892
~~~
---
`info free` ot `man free` provide documentation on how to use `free` from the linux manual
