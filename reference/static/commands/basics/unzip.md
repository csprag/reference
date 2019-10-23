unzip
====

ZIP is an archive [file format](https://en.wikipedia.org/wiki/Zip_(file_format)) that supports lossless data compression. In order to access the files zipped up in a .zip file, then file needs to be unzipped. The command `unzip` lists, tests and extracts compressed files in a ZIP archive.

---
#### Usage
To unzip a file `[filename].zip`, type the following command into terminal:
~~~ bash
unzip [filename].zip
~~~
The zip file will then be inflated into a folder containing the contents of the zip file.

##### Example
An example of the command being used to unzip a zip file:

![examplepic](https://i.ibb.co/3yN2cW3/Screen-Shot-2019-10-23-at-5-37-35-PM.png "Terminal Unzip Screenshot")

#### Notable Flags
| Flag | Description |
| ---- | ----------- |
| -l   | list archive files (short format). This flag will list information about the files which exist inside the zipped archive without actually unzipping the files. The names, uncompressed file sizes and modification dates and times of the specified files are printed, along  with  totals  for  all files  specified. |
| -v   | list  archive files (verbose format) or show diagnostic version info. Similar to -l flag but more verbose. |
| -p   | extract  files  to  pipe (stdout).  Nothing but the file data is sent to stdout, and the files are always extracted in binary format, just as they are stored (no conversions). You can get some really weird results with this one -- for example if your archive contained pdf files. Then printing out the contents of the pdf file to stdout will give you a bunch of inscrutable characters. |
| -T   | set the timestamp on the archive(s) to that of the newest file in each one. |
| -t   | test archive files.  This option extracts each specified file in memory and compares the CRC (cyclic redundancy check, an enhanced checksum) of the  expanded  file  with the original file's stored CRC value. Does not actually extract files |
| -z   | display only the archive comment. |

#### A Useful Script
If you have multiple .zip files in a folder, the following bash script can be useful for extracting them all at once:
~~~
for file in $1/*
do
	unzip $file
done
~~~
I use this often when I am downloading teaching curriculum resources for my church's children's ministry. It makes the unzipping much faster, and it is a cool way to make use of bash scripts! 


