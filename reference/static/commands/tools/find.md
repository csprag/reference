find
---
'find' is a command line tool that allows the user to search for files or directories with a given search criteria, anywhere on your machine.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ find . -name "*poster*"
  ./Downloads/silly_poster copy.pdf
$ find . -size -2M
  ./Documents/README.md
  ./Downloads/test.txt
~~~

---

### Useful Options / Examples
Find is really useful for making very specific searches (file names, sizes, modification dates, etc.), for anywhere on your machine, from anywhere on your machine! Some of the useful arguments you can use to toggle your search include: 
-name [search for a file based on name, case-sensitive]
-iname [search for a file based on name, non case-sensitive]
-size [search for a file based on size]
-amin [search for a file based on how many minutes ago you modified it]
-time [search for a file based on how many days ago you modified it]
#### find ~/ -size -5M
This commands returns all the files on your computer that are less than 5MB in size. 

~~~ bash
$ find ~/ size -5M
  ./Documents/setup.cpp
  ./Desktop/starter.hpp
~~~


#### find ~/ -size +1M and -time -1
This command returns all the files on your computer that are greater than 5MB in size and last modified in the last 1 day.

~~~bash
$ find ~/ size +1M and -time -1
  ./Downloads/Chrome.dmg
  ./Documents/lecture_recordings
~~~
