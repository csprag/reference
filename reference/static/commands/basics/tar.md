tar
-------
<!-- one line explanation would go here -->
`tar` is a command that can be used in bash to store, list, or extract files from an archive.
<!-- minimal example -->
~~~ bash
$ tar -xvzf starter-files.tar.gz 
starter-files/
starter-files/hello.cpp
~~~

---

### Useful Options / Examples

#### Example command
~~~ bash
tar -czvf archive-name.tar.gz source-name
~~~

##### Break it down

 * The `-c` argument will create a tar archive and write the files to it
 * The `-z` argument will put the archive through gzip (creating a tar.gz file)
 * The `-v` argument makes the output verbose so you can see what it's doing
 * The `-f` argument makes the tar.gz file get written to the named tar.gz file.

#### Example command
~~~ bash
tar -xzvf archive-name.tar.gz source-name
~~~

##### Break it down
 * The `-x` argument will extract a tar archive and write the files to it
 * The `-z` argument will put the archive through gzip (creating a tar.gz file)
 * The `-v` argument makes the output verbose so you can see what it's doing
 * The `-f` argument makes the extracted files get written to the named output file.

#### Other useful arguments
 * `-p` maintains the permissions of any files that are written/read from an archive
 * `-t` only lists the contents of an archive instead of extracting it.

#### Compression types
 * `-z` uses `gzip` for compression/decompression
 * `-J` uses `xz` for compression/decompression
 * `-j` uses `bzip2` for compression/decompression

