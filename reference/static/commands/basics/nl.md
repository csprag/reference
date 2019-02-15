nl
-------

`nl` is used to display the line number of each line in a specified file.

~~~ bash
$ nl csprag-notes.md
     1   Date: 11 January 2019
     2   Topic: Syllabus day
     3   This class seems awesome! :)
~~~

---

### Useful Options / Examples

The command has many different options; the defaults (which will automatically be selected if not specified otherwise) are:

~~~ bash
$ nl -v1 -i1 -l1 -s$'\t' -w6 -nrn -hn -bt -fn csprag-notes.md
     1   Date: 11 January 2019
     2   Topic: Syllabus day
     3   This class seems awesome! :)
~~~

Let's take a closer look at each of these flags by changing them slightly...

#### nl -v2 csprag-notes.md

~~~ bash
 $ nl -v2 csprag-notes.md
     2   Date: 11 January 2019
     3   Topic: Syllabus day
     4   This class seems awesome! :)
~~~

##### Break it down

 * The -v<*number*> flag (which can be expanded to --starting-line-number=<*number*>) specifies the number at which to start numbering the lines; the default is 1, but the user can specify a different number, as in our previous example

#### nl -i2 csprag-notes.md

~~~ bash
 $ nl -i2 csprag-notes.md
     1   Date: 11 January 2019
     3   Topic: Syllabus day
     5   This class seems awesome! :)
~~~

##### Break it down

 * The -i<*number*> flag (which can be expanded to --line-increment=<*number*>) specifies the number by which each line is incremented, so if the user specifies -v201 -i5, the first line will be numbered 201, the next will be numbered 206, the next 211, and so on

 #### nl -ba csprag-notes.md

 For this example, let's add two blank lines to the end of csprag-notes.md

~~~ bash
 $ nano csprag-notes.md
 $ nl -ba csprag-notes.md
     1   Date: 11 January 2019
     2   Topic: Syllabus day
     3   This class seems awesome! :)
     4   
     5   
~~~

##### Break it down

 * The -b<*style*> flag (which can be expanded to --body-numbering=<*style*>) modifies the numbering type for the body of our file; the options are:
    1. -ba (numbers all lines)
    2. -bt (numbers all nonempty lines)
    3. -bn (numbers no lines)
    4. -bp*BRE* (number lines containing a match for the regular expression, BRE)

#### nl -l2 -ba csprag-notes.md

~~~ bash
 $ nl -l2 -ba csprag-notes.md
     1   Date: 11 January 2019
     2   Topic: Syllabus day
     3   This class seems awesome! :)

     4   
~~~

##### Break it down

 * The -l<*number*> flag (which can be expanded to --join-blank-lines=<*number*>) specifies the number of blank lines that are counted as one when being numbered, so if the user specifies -l3 for a file with just six blank lines, the third line will be numbered 1, the sixth line will be numbered 2, and the rest of the lines will not be numbered (NOTE: for this flag to have any effect, the user must specify -ba; see above for details about this flag)

#### nl -sEECS201 csprag-notes.md

No more blank lines at the end of the file from here on out

~~~ bash
 $ nano csprag-notes.md
 $ nl -sEECS201 -ba csprag-notes.md
     1EECS201Date: 11 January 2019
     2EECS201Topic: Syllabus day
     3EECS201This class seems awesome! :)
~~~

##### Break it down

 * The -s<*string*> flag (which can be expanded to --number-seperator=<*string*>) specifies the string to be printed between the line numbers and the contents of the line itself, although the default prints a tab, which will probably make the output the most readable

 #### nl -w3 csprag-notes.md

~~~ bash
 $ nl -w3 csprag-notes.md
   1    Date: 11 January 2019
   2    Topic: Syllabus day
   3    This class seems awesome! :)
~~~

##### Break it down

 * The -w<*number*> flag (which can be expanded to --number-width=<*number*>) specifies the number of the "column" at which the line numbers will be printed; essentially, it is (numSpacesFromLeft + 1) and must be strictly greater than 0

 #### nl -nrz csprag-notes.md

~~~ bash
$ nl -nrz csprag-notes.md
000001   Date: 11 January 2019
000002   Topic: Syllabus day
000003   This class seems awesome! :)
~~~

##### Break it down

 * The -n<*format*> flag (which can be expanded to --number-format=<*format*>) specifies the format that the line numbers will follow, and is limited to the following options:
    1. -nrn (numbers are right-justified with no leading zeroes)
    2. -nln (numbers are left-justified with no leading zeroes)
    3. -nrz (numbers are right-justified with leading zeroes)

 #### nl -ha -fa csprag-notes.md

 For this example, let's add two blank lines to the end of csprag-notes.md

~~~ bash
 $ nl -ha -fa csprag-notes.md
     1   Date: 11 January 2019
     2   Topic: Syllabus day
     3   This class seems awesome! :)
~~~

##### Break it down

 * The -h<*style*> and -f<*style*> flags (which can be expanded to --header-numbering=<*style*> and --header-numbering=<*style*> respectively) modify the numbering type for the header and footer of the file; the options are the same as the -b<*style*> flag, and since most files we'll be working with in this class do not have a header or footer, we won't mess around with these flags too much

#### Other useful information about nl

There is also a --help flag as well as a --version flag, and I believe that the default flags consistently produce fairly readable output, feel free to mess around with all of the settings and see what works best for you. Happy line-counting! :)