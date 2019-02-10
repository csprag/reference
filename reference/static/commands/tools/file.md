file
-------
determine the file type by running tests against a file.

~~~ bash
$ file sample.cpp
sample.cpp: C++ source text, ASCII text
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