whereis
-------

`whereis` helps you locate where a program is on your computer. It can find binaries, manuals, and source code. 

~~~ bash
$ whereis python
/usr/bin/python
~~~

---
The `whereis` command checks standard binary directories for the specified program(s), then prints out the paths to those programs.

### Useful Options
* `-b` search only for binaries
    * use if you just want to know the location of the program
* `-m` search only for manuals
    * use if you want to find the manuals
* `-s` search only for sources
    * use if you want just the source code
* `-u` looks for unusual files
    * an 'unusual file' is a file that doesn't have only one entry of each type specificed in your command
* `-B`, `-M`, and `-S` let you change or limit the places where whereis looks for binaries, manuals, and sources (respectively)
    * useful to narrow down the search
* `-f` signals the end of the last directory list and the start of file names. 
    * you must use this any time you use `-B`, `-M`, or `-S`
* `l` prints out a list of all the paths that `whereis` searches

####  `whereis [options] [-BMS] [PATH] -f filename`
~~~bash
$ whereis ctags
ctags: /usr/bin/ctags.emacs25 /usr/bin/ctags /usr/share/man/man1/ctags.1.gz
~~~

#### Break it down
1. first, `whereis` finds the binary, manual files, and/or source files for the given filenames based on the included flags
2. the names are stripped of leading path-name components and any trailing extensions of the form ".ext"
3. then it attempts to find your program in a list of standard Linux places, the places specified in `$PATH`, and the places specified in `$MANPATH`

#### `whereis -b filename`
~~~bash
$ whereis -b python
python: /usr/bin/python3.6 /usr/bin/python3.6m /usr/lib/python2.7 /usr/lib/python3.7 /usr/lib/python3.6 /etc/python2.7 /etc/python3.6 /usr/local/lib/python3.6 /usr/include/python3.6m /usr/share/python

~~~

#### Break it down
Use this command if you just want to find the location of the program (the binary file) and nothing else. 

#### `whereis -m filename`
~~~bash
$ whereis -m firefox
firefox: /usr/share/man/man1/firefox.1.gz

~~~
#### Break it down
`-m` returns the manual files with firefox in the filename. You would use `-u`  along with  `-m`  if for example you have more than one manual on your system or if the program you're looking for appears in more than one place.

#### `whereis -B [PATH] -f filename`
~~~bash
$ whereis -B /usr/bin -f cp
cp: /usr/share/man/man1/cp.1.gz
~~~

#### Break it down
If you kind of have a vague idea where your program is, you can use `-B` to search a specific list of directories. In this example, `whereis` would only search for binary files in /usr/bin

##### Similar commands
`find`, `locate`, `which`

##### A Good Reference
https://linux.die.net/man/1/whereis
