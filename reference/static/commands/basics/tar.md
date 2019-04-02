tar
-------
`tar` is a command that can be used in bash to store, list, or extract files from an archive.

~~~ bash
$ tar -xvzf starter-files.tar.gz 
starter-files/
starter-files/hello.cpp
~~~

---

## Common flags

#### File Arguments
 * The `-c` argument will create a tar archive and write the files to it
 * The `-x` argument will extract a tar archive and write the files from it into the current directory
 * The `-z` argument will put the archive through gzip (creating/extracting a tar.gz file)
 * The `-v` argument makes the output verbose so you can see what it's doing
 * The `-f` argument gives a name to the archive/folder being created.

#### Compression types
 * `-z` uses `gzip` for compression/decompression
 * `-J` uses `xz` for compression/decompression
 * `-j` uses `bzip2` for compression/decompression

#### Other useful arguments
 * `-p` maintains the permissions of any files that are written/read from an archive
 * `-t` only lists the contents of an archive instead of extracting it.
 * `-C` changes the directory that the files will be extracted to


#### Example command
~~~ bash
tar -xzvf archive-name.tar.gz
~~~
This command extracts the files from a tar.gz archive from archive-name.tar.gz into the current directory.

#### Example command
~~~ bash
tar -czvf archive-name.tar.gz source-name
~~~
This command creates a tar archive with the files from source-name.
