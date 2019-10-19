pushd
----
<!-- one line explanation would go here -->
The pushd command stores a directory path in the directory stack while the popd command removes the top directory path from the same stack. In addition, both these commands make the directory being working on as your new working directory.
<!-- minimal example -->
~~~ bash
yzr:~ yzr/Downloads$ pushd /home/yzr/Desktop
~~~
When this command is run, the current directory - ~/yzr/Download - is saved on the directory stack and the directory - home/yzr/Desktop - becomes your new working directory.

### Useful Options / Examples

#### `pushd -n PathOfDirectory`

~~~bash
yzr:~ yzr$ pushd ~/Dropbox/accounts/
~~~

##### Break it down
* To suppress the default change to directory, use the -n option.
* In the above example, ~/Dropbox/accounts/ is added to the stack but current directory will not change into it

#### `pushd [+N|-N]`

~~~bash
yzr:~ yzr$ pushd +2
yzr:~ yzr$ pushd -1
~~~

##### Break it down
* When counting from top to bottom (or left to right), you want to use argument [+N] where N is the index.
* When counting from top to bottom (or left to right), you want to use argument [-N] where N is the index.
* In the above example, when there are 4 directories on the stack, +2 and -1 would refer to the same directory.
