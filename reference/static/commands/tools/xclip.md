xclip
-------

`xclip` is useful for copying the contents of files to the clipboard

~~~ bash
$ echo "clipped text" > file.txt
$ xclip file.txt -sel c
~~~

---

### Useful Options / Examples

#### `xclip -i [filename] -selection "clipboard"`

-i, -in is on by default, reads in text from standard input or files to selection

~~~ bash
$ xclip ~/.ssh/id_rsa.pub -sel c 
~~~

This copies to the standard clipboard and will function like you want and will paste to any window.

This will copy the contents of `~/.ssh/id_rsa.pub` to the clipboard (XA_CLIPBOARD)to be pasted with ctrl-v or right click paste.

~~~ bash
$ xclip ~/.ssh/id_rsa.pub -selection clipboard
~~~

This is the full command for those wondering.

#### `xclip`

This will allow you to type in standard input to be copied to selection

#### `xclip [filename]` 

~~~ bash
$ xclip ~/.ssh/id_rsa.pub 
~~~

This will copy the contents of `~/.ssh/id_rsa.pub` to XA_PRIMARY.

THIS IS NOT THE STANDARD CLIPBOARD

You can paste to [X](https://en.wikipedia.org/wiki/X_Window_System) applications by cliking the middle mouse button.

This plays well with most Linux applications like the Terminal, Gedit, and Firefox.

Cannot paste this with ctrl-v or right click, which might be beneficial because it doesn't overwrite what you have on the clipboard so you can have two pasteable strings at the same time.

Also it's less typing than -selection clipboard.

The above command is handy when dealing with adding ssh keys to github/gitlab

#### `xclip -o`

-o, -out prints the selection to standard out (generally for piping to a file or program) 

The above command will print what is in XA_PRIMARY to standard out
