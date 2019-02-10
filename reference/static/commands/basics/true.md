true
-----
`true` is a function that always exits with status 0, the logical truth value.

~~~ bash
$ true
$ echo "The last command exited with status $?."
The last command exited with status 0.
~~~

---
###Useful Options/Examples
The `true` function can take any argument and will still return 0. So the above example could be rewritten as:
~~~
$ true false maybe-true whatever --this_is_an_example
$ echo "The last command exited with status $?."
The last command exited with status 0.

## Null command
`true` is an actual function that needs to be run, so it might take up resources. Null command (`:`) is actually built into the shell and therefore, could be considered more efficient.
In a shell script example.sh we could have:
~~~~
while :
do
	echo hello world
else
	echo goodbye
done
~~~~

And it will run forever.
## Ignoring exit status
`true` can be used to ignore the exit status of a function:
```make ... || true```
This will exit with 0 so the shell will ignore the exit status of the `make` function.

