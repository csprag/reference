
mktemp
---

`mktemp()` creates a unique temporary file or directory.

~~~ bash
$ mktemp temp.XXXXXX
temp.ayXVZb
~~~

---

### Useful Options / Examples
* `-d` : make a unique directory instead of a file 
* `-q` : fail silently if there's an error (i.e. if you're scripting and don't want an error message to print)
* `-t <prefix>` : generate a template string based on the <prefix> 
* `-u` : operate in 'unsafe mode', the temp file will be unlinked before `mktemp` exits -- not encouraged.

Command format: `$ mktemp [OPTIONS] [TEMPLATE]`

#### `mktemp [TEMPLATE]`  

~~~ bash
$ mktemp temp.XXXXXX
temp.TpCjWI
~~~

1. `mktemp` takes the given filename template and overwrites part of it to generate a unique temporary filename
2. The template may be any file name with some number of Xs' appended to it, for example "/tmp/temp.XXXXXX"
3. The trailing X's are replaced with an alphanumeric string that makes the file name unique
4. The number of unique file names mktemp() can return increases with the number of `Xs' provided
5. If `mktemp` can successfully make a unique filename, it will create that file and print the name it came up with
6. Now a file exists named "testing.TpCjWI" in the present working directory

#### `mktemp -d [TEMPLATE]`
makes a unique directory 

~~~ bash
$ mktemp -d ./temp.XXXXXX
temp.pPSsxv // this is a temporary directory

~~~


### Notes/Bugs
The `mktemp` function is useful but can be dangerous from a security perspective since it
creates filenames that can be guessed. The risk is minimized when large numbers of Xs' are used to increase the
number of possible temporary filenames. Use `mkstemp` or `mkostemp`  to increase security.

### Reference
To see the full documentation use the command `man mktemp`
