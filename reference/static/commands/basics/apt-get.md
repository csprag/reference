# apt-get
-------	-------
apt-get is a package management tool. It provides you the tools to conveniently manage the packages on your system.

 ~~~ bash
$ apt-get install <package_name> 
Reading package lists... Done
Building dependency tree
...
Unpacking <package_name>
...
$
 ~~~


 ---	---


 ### Useful Options / Examples
 ##### Multiple Packages
 apt-get allows you to list multiple package names when they are separated by a space.
  ~~~ bash
$ apt-get install <package1_name> <package2_name> <package3_name>
...
  ~~~

 ##### update
 This command updates your source list. The available packages are found in /etc/apt/sources.list
  ~~~ bash
$ apt-get update
  ~~~
  
  ##### upgrade
 This command updates your copy of packages to the newest version.
  ~~~ bash
$ apt-get upgrade
  ~~~

  ##### check
 This command checks for broken dependencies. It also updates the package cache.
  ~~~ bash
$ apt-get upgrade
  ~~~

 ##### auto-apt
 When using auto-apt, auto-apt will automatically install packages that are being accessed by the program.
   ~~~ bash
$ auto-apt run <program>
...
  ~~~
  
 ##### remove
 remove allows you to remove the specified package
   ~~~ bash
$ auto-apt remove <package>
  ~~~
  
##### apt-cache search
Running this command allows you to search for packages that you can install
  ~~~ bash
$ apt-cache search <search_term>
  ~~~
To see all available packages
 ~~~ bash
$ apt-cache search .
  ~~~
