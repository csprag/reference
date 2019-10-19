tee
-------
`tee`, when paired with `|`, allows a user to:
Take the output at the time of the `tee` command, put it in a file, and continue moving down the pipeline.
In other words, the command is used to *split* the output of a program so that it can be both saved in a file and displayed.

<!-- minimal example -->
~~~ bash
$ ls -l | tee file.txt | less
~~~

---

A More In Depth Example

Say we have a directory containing two text files, file1.txt and file2.txt

~~~bash
$ ls | tee file_list.txt | less
~~~

The output of the `ls` command is now displayed in the `less` editor, and 
the file "file_list.txt" now contains the text:

file1.txt  
file2.txt  

Tee takes the output of the command before it, places it in a file or files, and then continues down the pipeline

### Useful Options / Examples

~~~bash
$ ls | tee -a file_list.txt | less
~~~

The `-a` flag appends the output to the file, rather than overwriting it. 
Following the previous example above, the new contents of file_list.txt is now:

file1.txt  
file2.txt  
file1.txt  
file2.txt  

### Useful Options / Examples

~~~bash
$ ls | tee list1.txt list2.txt | less
~~~

We now have two files that contain a list of files

**list1.txt**  
file1.txt   
file2.txt  

**list2.txt**  
file1.txt   
file2.txt  
