file
-------
Determine the file type by running tests against a file. The input can be filenames of text, music, vedio, binary files, etc. The output might include more details for certain file types.

~~~ bash
$ file sample.cpp
sample.cpp: C++ source text, ASCII text
$ file 红楼梦.txt
红楼梦.txt: UTF-8 Unicode text, with very long lines, with CRLF line terminators
$ file Break_up.mp3
Break_up.mp3: Audio file with ID3 version 2.3.0, contains:MPEG ADTS, layer III, v1, 320 kbps, 44.1 kHz, Stereo
~~~

---

### Useful Options / Examples

#### Example command
~~~ bash
$ file -b sample.cpp     
C++ source text, ASCII text
~~~

##### Break it down
`-b` or `--brief` option emit the file name from the output

#### Example command
~~~ bash
$ file -F '->' sample.cpp 
sample.cpp-> C++ source text, ASCII text
~~~

##### Break it down
The default delimiter is a colon in the output.
```file -F "<delimiter>" <filename>```
customizes your output
