basename
----
`basename` takes any pathname and deletes everything upto the last slash (' / ') character and return the result.

```bash
$ basename /home/testPath/foo.wiki
foo.wiki
```

---

### Useful Options / Examples
#### `$ basename pathname suffix`
Specifying a suffix after the pathname will also delete the trailing suffix in the result.
```bash
$ basename /home/path/thisIsAnExample Example
thisIsAn
```
You can use this to get the name of a file without its extension and play around with it in other bash commands.
```bash
$ basename /oneMore/example.pdf .pdf
example
```
#### Additional Details
The converse of `basename` is called `dirname`, which basically takes everything from the start of the pathname to the trailing slash.
