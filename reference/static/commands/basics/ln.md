ln
---
`ln` is used to create a link to another file. They can be thought of as similar to a pointer to another file, an alias, or a shortcut. 

The value of making links is to save storage space, and make sure that scripts are all referencing the correct files without dealing with multiple copies.

The `ln` command fundamentally can make two types of links: *hard links* and *symbolic links*. By default, `ln` will use hard links, even though in practice you will typically want a symbolic link if you are using this command.

~~~ bash
ln -s largeSourceFile.cpp smallLink.link
~~~

---

### Useful Options / Examples

#### Symbolic Links

The most common flag to be familiar with is `-s`, which creates a symbolic link.

So, what *is* a symbolic link? It is a pointer to a file or directory in your filesystem, this can be useful if you are referencing the same data from multiple locations, but comes with a few upsides and drawbacks. The biggest advantage is their absolutely tiny filesize. They will typically be a few *bytes* at the most, so memory-wise they are virtually free for how powerful they are. The main downside is that if you move the original file or even change its name, your link will be broken (think like pointer invalidation). 

##### Usage

The first argument is the name of the file you want to make a link to (required). You can then optionally specify where you want to place the link in an additional second argument (this is a very typical usage). 

If you give three or more arguments, it will make links to each of the given target files.

~~~ bash
ln -s largeSourceFile.cpp
~~~

*or* 

~~~ bash
ln -s largeSourceFile.cpp ~/other/directory/smallLink.link
~~~

####  Hard Links

It is less common to use ln to create a hard link, since it uses much more memory (it will take about the same amount as if you had just copied the original target file).

Hard links create a link to the physical inode reference to the target file on your hard drive. This means the link will still work even if you move the target file's location or name.

**Note:** Hard Links can only be used to link to a *file*, you **cannot** create a hard link to a *directory* .

##### Usage

~~~ bash
ln largeSourceFile.cpp
~~~

*or* 

~~~ bash
ln largeSourceFile.cpp ~/other/directory/smallLink.link
~~~

**Note:** Usage for creating a hard link or a symbolic link should be virtually identical.
