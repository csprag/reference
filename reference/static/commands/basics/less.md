less
-------

`less` is a command used to help the user navigate through a large output from within a terminal window.

~~~ bash
$ less long_file.txt
$ cat long_file.txt | less
~~~

---

### Useful Options / Examples

#### `less [file]`
~~~ bash
$ less [options] long_file1.txt
~~~
This command displays the contents of the file you specify as an argument, which in this case is `long_file1.txt`. 

#### `[command] | less`
~~~ bash
$ sdiff long_file1.txt long_file2.txt | less [options]
~~~
You can pipe the output of another command into `less` in order to navigate the output of that command more easily. This is helpful when a command prints a lot of output, as you can now navigate through your output using purely your keyboard, which can be helpful if you're using a terminal that does not have good support for scrolling. In addition, `less` also makes it easy to instantly jump to certain parts of your output.

#### `less -N`
~~~ bash
$ less -N [file]
$ [command] | less -N
~~~
The `-N` flag opens your output in `less` with visible line numbers next to each line.

#### `less -X`
~~~ bash
$ less -X [file]
$ [command] | less -X
~~~
The `-X` flag can be used to ensure that the content currently displayed on your screen is not cleared when you exit `less`.

### Navigating Around in `less`:
- Quit - `q`
- Move one line down - `Down`, `j`, `e`, or `Enter`
- Move one line up - `Up`, `k`, or `y`
- Move one page down - `PgDn` or `Space`
- Move one page up - `PgUp` or `b`
- Jump to first line - `Home` or `g`
- Jump to last line - `End` or `G`
- Jump to 5<sup>th</sup> line of output - `5g`
- Jump to 25% through the output - `25p` or `25%`
- Search for text - `/search [text]`, followed by `Enter`
- Edit the currently opened file using your default editor - `v`
- Show help screen - `h`