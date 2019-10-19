source
------
`source` is a command that reads and executes the content of a file, content that is passed as an argument to the shell script. it uses the $PATH variable to find the path of the file to execute

~~~ bash
$ echo "ls" > hello.txt
$ source hello.txt
the files 
in your 
directory 
show up
~~~

------

### Useful Options / Examples
You can pass arguments to source, to do this make a .sh file named example1.sh with the following code: 

`echo "The user has provided $# argument, execute the loop :"
printf "%s" "$@ time"`

$# gives the number of args, $@ will get the value of all the args.

~~~ bash
$ source example1.sh 1
The user has provided 1 argument, execute the loop :
1 time
~~~

You can also use $1, $2, $3 etc. to get the first second, and third arguments, respectively. 
Make a .sh file named example2.sh with the following code:

`echo "The user has provided $# argument, execute the loop :"
printf "%s" "$1 time"`

~~~ bash
$ source example2.sh 1 2 3
The user has provided 3 argument, execute the loop :
1 time
~~~

One such occasion where running source is useful is in the `.bashrc`
If you would like to alias a word, you do this in the `.bashrc`

To do this, open your `.bashrc` file in vim. 

~~~ bash
$ vim ~/.bashrc
~~~

In vim, type the following command, note that you will need to put in a custom path to your desktop
folder (write in vim pressing i)

~~~ bash
alias desktop='cd /your/path/to/Desktop'
~~~

Quit vim by typing `:wq` and hitting enter.

Now, if you run

~~~ bash
$ source ~/.bashrc
$ desktop
$ /your/path/to/Desktop#

~~~

You will be automatically put into the Desktop directory of your machine!
You succesfully aliased "cd /your/path/to/Desktop" to "desktop" using source!
What happened here is that once you made the changes in the `.bashrc` file, we ran source on the file. What happened was that the `.bashrc` got ran again and the alias that was ran, allowing you to alias that command. To learn more about `.bashrc`  go here https://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work









