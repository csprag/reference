pdflatex
-------

LaTeX is a markup language used to typeset technical documents. It's especially effective for documents which contain lots of mathematics, and is commonly used in a variety of STEM fields. `pdflatex` is a command used to compile a LaTeX document into a PDF from the command line.

~~~ bash
pdflatex [filename].tex
~~~

---

### Useful Options / Examples

- The `-8bit` option ensures that all characters are printable, i.e., don't use any `^^X` sequences.
- The `-halt-on-error` option makes compilation stop as soon as an error is found.
- The `-version` prints important version information about `pdflatex` and the LaTeX distribution on your computer.
- The `-help` option prints out information about the program, which can be used to learn more about some of the more advanced flags.

#### Example 1

~~~ bash
pdflatex -8bit myTexFile.tex
~~~

This will compile `myTexFile.tex` into `myTexFile.pdf`, and ensure that all characters can be printed.

#### Example 2

~~~ bash
pdflatex -halt-on-error buggyTexFile.tex
~~~

This will attempt to compile `buggyTexFile.tex` into `buggyTexFile.pdf`, but will halt if an error is found. If/when this occurs, it will output the location and cause of the error, making it useful for quickly debugging.