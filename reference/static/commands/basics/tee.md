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
