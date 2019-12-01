fold
---

`fold` is a UNIX command that folds long lines for finite widths. It wraps each line in an input file to fit a specified width and prints it to the standard output. By default it wraps lines at a maximum width of 80 columns, but it also supports specifying the column width and wrapping by numbers of bytes.

~~~ bash
$ # Syntax / Example
$ fold [OPTION]... [FILE]...
$ fold linux.txt
$ cat linux.txt
Linux is a family of open source Unix-like operating systems based on the Linux kernel, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.
$ fold linux.txt
Linux is a family of open source Unix-like operating systems based on the Linux
kernel, an operating system kernel first released on September 17, 1991, by Linu
s Torvalds. Linux is typically packaged in a Linux distribution.

~~~

---

### Useful Options / Examples

#### `fold -w[n]`

By using this option in fold command, we can change the column width from default width of 80.

~~~ bash
$ fold -w40 linux.txt
Linux is a family of open source Unix-li
ke operating systems based on the Linux
kernel, an operating system kernel first
 released on September 17, 1991, by Linu
s Torvalds. Linux is typically packaged
in a Linux distribution.
~~~


#### `fold -b[n]`

This option will contstrain the width of the output to the number of bytes specified rather than the number of columns.

~~~ bash
$ fold -b30 linux.txt
Linux is a family of open sour
ce Unix-like operating systems
 based on the Linux kernel, an
 operating system kernel first
 released on September 17, 199
1, by Linus Torvalds. Linux is
 typically packaged in a Linux
 distribution.
~~~

#### `fold -w[n] -s`

When using the -w option, fold will break words to wrap lines. The -s option will help you break on spaces so that words are not broken to wrap lines.

~~~ bash
$ fold -w40 -s linux.txt
Linux is a family of open source
Unix-like operating systems based on
the Linux kernel, an operating system
kernel first released on September 17,
1991, by Linus Torvalds. Linux is
typically packaged in a Linux
distribution.
~~~