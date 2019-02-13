rsync
-------

- Rsync is usually used for remotely copying files to or from a computer to which you have ssh access.
- Rsync copies files either to or from a remote host, or locally on the current host (it does not support copying files between two remote hosts).


Usage
-------
Basic Syntax:
~~~ bash
rsync source destination
~~~

For example, copy files from a remote machine:
~~~ bash
$ rsync username@host:/some/path/on/remote/machine /some/path/on/my/machine/
~~~

Copy files to a remote machine:
~~~ bash
$ rsync /some/path/on/my/machine username@host:/some/path/on/remote/machine/
~~~

We can also use it to sync 2 directories on our local machine:
~~~ bash
$ rsync directory1 directory2
~~~

Rsync is great because if it fails or you stop it in the middle of operating, you can restart it and it will pick up where you left off. It does not blindly copy directories or files, but rather syncronizes them (makes sure they are the same). 

For example, if you try to copy a directory that you already have, rsync will detect this and transfer no files.

---

### Commonly Used Options:
--------

#### -a flag

##### Ensures that symbolic links, devices, attributes, permissions, ownerships, etc. are preserved in the transfer:
~~~ bash
$ rsync -a  username@myhost.university.edu:/my/source /my/destination/
~~~

#### -z flag

##### Compresses files during transfer.

#### -v flag

##### Verbose mode. Gives extra output.

#### --progress

##### Shows the progress of the file transfer.

We can use these flags all at once like this:
~~~ bash
$ rsync -azv --progress username@myhost.university.edu:/my/source /my/destination/
~~~

#### --dry-run

##### Allows us to preview rsync's behavior without actually transferring any files.
~~~ bash
$ rsync --dry-run username@myhost.university.edu:/my/source /my/destination/
~~~

For a full list of rsync flags and commands, visit: https://linux.die.net/man/1/rsync
