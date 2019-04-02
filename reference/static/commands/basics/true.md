true
-----
`true` is a function that always exits with status 0, the logical truth value.

~~~ bash
$ true
$ echo "The last command exited with status $?."
The last command exited with status 0.
~~~

---
### Usage with variables
The correct usage with variables is kind of unintuitive: the safest way to use the value `true` in a variable in conditionals is by comparing it to `true` itself:
~~~ bash
var=true
#Intuitive way of writing if statement:
if [ $var ]; then
	echo "I might execute this"
else
	echo "I could also execute this"
fi
#Correct way of writing if statement:
if [ $var = true ]; then
	echo "I will execute this"
else
	echo "Never this"
fi
~~~
And the reason is that if `var` is not explicitly set to `true` (like `var=$1`), it might contain something other than `true`, `false`, `1` or `0` which will be executed but probably shouldn't.
### Useful Options/Examples
The `true` function can take any argument and will still return 0. So the above example could be rewritten as: <br>
~~~ bash
$ true false maybe-true --this_is_an_example=0
$ echo "The last command exited with status $?."
The last command exited with status 0.
~~~
This means that `true` can be used to ignore the exit status of a function: <br>
~~~ bash
$ make arg1 || true
~~~
Will evaluate to true regardless of the status of `make` because of `true`, so the shell will continue.
`true` can also be used inside scripts to return booleans:
~~~ bash
if [ $1 = "foo" ]; then
  echo "bar!"
  return true
else
  return false
fi
~~~
### Null command
`true` is an actual function that needs to be run, so it might take up resources. Null command (`:`) is built into the shell and therefore, could be considered more efficient.
In a shell script example.sh we could have
~~~~ bash
while :
do
	echo 'hello world'
else
	echo 'goodbye'
done
~~~~
Which is equivalent to
~~~ bash
while true
do
  echo 'hello world'
else
  echo 'goodbye'
done
~~~
And both would run until interrupted.  
Another possibly neat use for `:` is in the case where the program should **do nothing**:
~~~ bash
while condition_is_true; do
  : #Do nothing
done
~~~
This loop will run forever and will not execute any statements.
