nl
---

`nl` command is used to list the lines of a file in a numbered fashion
~~~ bash
$ cat one.txt
 fedora
 debian
 arch
 slack
$ nl one.txt
 1 fedora
 2 debian
 3 arch
 4 slack
~~~

---

### Useful Options / Examples

When the files completely match, there is no output from `diff`.

~~~ bash
$ printf "same" > first.txt
$ printf "same" > second.txt
$ diff first.txt second.txt
$
~~~
