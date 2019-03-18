hash
---
<!-- one line explanation would go here -->
`hash` is a command which keeps track of the location of, and number of times each command is used.
<!-- minimal example -->
~~~ bash
$ hash
hits	command
   1 	/usr/bin/vim
   2 	/bin/cat
   1 	/usr/bin/man
   9 	/bin/ls
~~~

---
### More Detailed Explanation
`hash` is a basic Unix command which shows the full pathname of each command used in this session, along with the number of times that command has been used. The `hash` command utilizes a hash table data structure to store this information for quick retrieval. The full path name, and the number of uses, of each command is always stored in the hash that is shown when `$ hash` is run. This is done in the background even if `$ hash` is never explicitly run. Calling `$ hash` merely prints out the hash table that is being silently populated in the background.

### Why does it exist?
The `hash` command is first and foremost an optimization for Unix shell users. By storing the full path to each command in a hash table (which has very fast access speed), the path of each command (such as `ls` , ` vim` , `man` , `cat` , etc.) does not have to be determined from `$PATH` each time it is called. This noticably reduces the time required for the shell to execute commands. This is very helpful for users who are utilizing many commands which are dispersed throughout their directories. Not having `hash` would take those users noticably longer to execute the command they need.   

### Useful Options / Examples
The `hash` command has a short list of flags and arguments. (Note that the following summary of the `hash` command's flags and arguments can be found in the help pages for hash. To find this yourself, open a Unix terminal and enter the following command: `$ hash --help` ).

#### Arguments
- COMMAND
	- COMMAND is the command you are interested in adding, removing, or printing its stored path

##### Flags
- -d COMMAND
	- Removes the entry corresponding to COMMAND from the hash table				 
- -l 
	- Outputs hash table entries in a way suitable for input to other commands
- -p PATHNAME COMMAND 
	- For the hash table entry COMMAND, changes its stored path to PATHNAME	
- -r
	- Removes all hash table entries
- -t COMMAND
	- Prints the path stored in the hash table for COMMAND

Note that like other basic Unix commands, anytime COMMAND is listed, mulitple COMMANDS can be used (with spaces separating each one) and the flags will be applied to all COMMANDS.

### Example commands


#### No flags or arguments
~~~ bash
$ hash 
hits	command
   2	/bin/cat
   2	/usr/bin/vim
   3	/bin/ls
~~~

##### Break it down
Using `hash` with no arguments or flags simply prints what is in the hash table at that moment. The hits corresponds to the amount of times that command has been called, and the command corresponds to the full path of the command (with the command name being what comes after the last `/`.
NOTE: The fact that these entries printed in ascending order based on the number of hits is merely coincidence. A hash table has no natural order and the printing of the table is not garunteed to be in any specific order.


#### Using `hash` with the `-d` flag
~~~ bash
$ hash -d cat
$ hash
hits	command
   2	/usr/bin/vim
   3	/bin/ls
~~~

##### Break it down
Here the `-d` flag was used along with the command `cat`. This resulted in `cat` having its entry removed from the hash table.


#### Using `hash` with the `-l` flag
~~~ bash
$ hash -l
bullitin hash -p /bin/cat cat
bullitin hash -p /usr/bin/vim vim
bulltiin hash -p /bin/ls ls
~~~

##### Break it down
Here the `-l` flag was used. Just as was described above, this flag changes the way the hash table entries are printed. This output is stated to be "easier to use as input" (presumably to other commands) according to the help page. However, this flag seems to have limited application. Just printing the path corresponding to specific commands can be done with the `-t` flag.


#### Using `hash` with the `-t` flag
~~~ bash
$ hash -t vim
/usr/bin/vim
~~~

##### Break it down
Here the `-t` flag was used to have hash print the path for `vim` as it is stored in the hash table. Note that this path is not garunteed to be accurate, since the user can change the path of a tabl entry with the `-p` flag.


#### Using `hash` with the `-p` flag
~~~ bash
$ hash -p /reality/can/be/whatever/i/want/vim
$ hash -t vim
/reality/can/be/whatever/i/want
~~~

##### Break it down
Here the `-p` flag was used to change the stored path for `vim` in the hash table. Notice that the path name for `vim` was changed to be something completely arbitrary and nonexistent in the user's directory. Again, notice that `/vim` was not even required to be the last entry in the file path. Nonetheless, the command: `$ hash -t vim` still printed the correct entry's path name. This is because the keys for the underlying hash tables are the commands themselves. 


#### Using `hash` with the `-r` flag
~~~ bash
$ hash -r
$ hash
hash: hash table empty
~~~ 

##### Break it down
Here it can be seen that using the `-r` flag clears all the entries of the hash table. Note that this does not erase the commands from the `$PATH` variable, but just erases the copies stored in the hash table.


#### Using `hash` with multiple arguments
~~~ bash
$ hash
hits	command
   1	/bin/cat
   1	/usr/bin/vim
   2	/usr/bin/man
   5	/bin/ls
$ hash -d cat vim
$ hash
hits	command
   2	/usr/bin/man
   5	/bin/ls
~~~

##### Break it down
This is just an example of how mutliple arguments can be passed to the `-d` flag. This will also work with the `-t` and `-p` commands (note that using mutliple arguments with the `-p` flag will set all of the listed commands to have the same specified path in the hash table.


#### Resources
For further research, the following resources will likely be helpful.
- Running the command: `$ hash --help` on a Unix terminal
- https://en.wikipedia.org/wiki/Hash_(Unix)
- https://unix.stackexchange.com/questions/86012/what-is-the-purpose-of-the-hash-command


