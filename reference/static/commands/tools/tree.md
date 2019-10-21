tree
-------

`tree` Returns a list of all of the contents of a directory in a tree-like format.

~~~ bash
$ tree eecs201
eecs201
├── HW1
│   └── csprag-wk1-homework.pdf
├── HW2
│   └── csprag-wk2-homework.pdf
├── HW3
│   └── csprag-wk3-homework.pdf
├── HW4
│   └── csprag-wk4-homework.pdf
├── HW5
│   └── csprag-wk5-homework.pdf
└── HW6
    └── csprag-wk6-homework.pdf

~~~

---

### Useful Options / Examples

### `tree`

~~~bash
$ tree  [-acdfghilnpqrstuvxACDFQNSUX] [-L level [-R]] [-H baseHREF] [-T title] 
[-o filename] [--nolinks] [-P pattern] [-I pattern] [--inodes] [--device] 
[--noreport] [--dirsfirst] [--version] [--help] [--filelimit #] [--si] [--prune]
[--du] [--timefmt format] [--matchdirs] [--fromfile] [--] [directory ...]
~~~

`–help` : Outputs a verbose usage listing with details on all options available.
`-a` : All files are printed. By default, tree does not print hidden files (files beginning with a dot 
'.'). Tree also does not print the file system constructs '.' (current directory) and '..' (previous 
directory).
`-d` : Lists only directories.
`-f` : Prints the full path prefix for each file.

#### `tree -d file`

~~~bash
$ tree -d eecs201
eecs201
├── HW1
├── HW2
├── HW3
├── HW4
├── HW5
└── HW6
~~~

##### Break it down
The `-d` flag is useful because it returns only the directories in the tree as opposed to all of the 
items in the tree.

#### `tree -f file`

~~~bash
$ tree -f eecs201
eecs201
├── eecs201/HW1
│   └── eecs201/HW1/csprag-wk1-homework.pdf
├── eecs/HW2
│   └── eecs201/HW2/csprag-wk2-homework.pdf
├── eecs/HW3
│   └── eecs201/HW3/csprag-wk3-homework.pdf
├── eecs/HW4
│   └── eecs201/HW4/csprag-wk4-homework.pdf
├── eecs/HW5
│   └── eecs201/HW5/csprag-wk5-homework.pdf
└── eecs/HW6
    └── eecs201/HW6/csprag-wk6-homework.pdf
~~~

##### Break it down
The `-f` flag is useful because it returns the full path prefix for each item in the tree.
