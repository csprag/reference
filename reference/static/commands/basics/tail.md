tail
-------
`tail` is used to print the last few n (n = 10 by default) lines of a certain file.

~~~ bash
$ tail /path/to/file  
outputs the last 10 lines of the file at that path  

~~~

---

### Useful Flags
`-n` limits output to n lines   
`-q` surpresses the header of the file, good for combining files  

## Example: Limiting output to 5 lines
$ tail -n 5 /usr/share/dict/american-english  
épée's  
épées  
étude  
étude's  
études  
## Example: Multiple Files
##### We can also use `tail` with multiple files at once 
   
$ tail -n 5 /usr/share/dict/american-english /usr/share/dict/cracklib-small  
==> /usr/share/dict/american-english <==  
épée's  
épées  
étude  
étude's  
études  
  
==> /usr/share/dict/cracklib-small <==  
zurich  
zw6syj  
zxcvbn  
zxcvbnm  
zygote  
## Example: Multiple Files with no headers
##### We use the `-q` flag to get rid of the header when using `tail` on multiple files. This can be useful to combine the last n lines of two files together.  
  
$ tail -qn 5 /usr/share/dict/american-english /usr/share/dict/cracklib-small  
épée's  
épées  
étude  
étude's  
études  
zurich  
zw6syj  
zxcvbn  
zxcvbnm  
zygote  
## Example: Piping with `tail`
##### We can pipe `tail` to and from other commands. In this example, I am doing `ls` within my home directory to see the 5 oldest files or folders in my home directory.  
   
$ ls -t | tail -n 5  
Music  
Pictures  
Public  
Templates  
Videos  
