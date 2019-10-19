gzip
-------
`gzip` is used to compress or decompress a file.

~~~ bash
$ touch file
$ gzip file
$ ls
file.gz
$ gzip -d file.gz
$ ls
file
~~~

---

### Useful Options / Examples

#### `gzip` file
~~~ bash
$ gzip file
$ ls
file.gz
~~~

##### Break it down
This command compresses _file_ into _file.gz_

_Note:_ this discards file


#### `gzip -d` file.gz
~~~ bash
$ gzip -d file.gz
$ ls
file
~~~

##### Break it down
This command unzips (_de_-zips) a file with the `.gz` extension.


#### `gzip -k` file
~~~ bash
$ gzip -k file
$ ls
file file.gz
~~~

##### Break it down
This command compresses and _keeps_ the file being compressed
