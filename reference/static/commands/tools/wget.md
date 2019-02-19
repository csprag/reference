wget
-------
`wget` is a non-interactive free network downloader that supports file retrieval via `HTTP`, 
`HTTPS`, and `FTP` protocols.

<!-- minimal example -->
~~~ bash
# Download the title page at the given url in a file called `index.html`
$ wget http://example.com/
~~~

---

### Useful Options / Examples

#### `wget -r`

##### Recursive download
With `wget`, you can recursively download any files and resources in a given web directory
hierarchy spawning from the root. This can be done like so:
~~~ bash
# Download a very reputable website recursively
$ wget -r https://www.latlmes.com/arts/return-of-the-golden-age-of-comics-1
~~~

#### `wget -A`

##### Filetype Filtering
With the `-A` flag (`--accept`), you can provide a list of filetypes to accept from the 
download. They are provided by their file extensions in a comma-delimited list.
Example:
~~~ bash
# Download all of the image files on a website
$ wget -A .png,.jpg,.gif https://www.example.com/
~~~

#### `-t`, `-w`, and `-T`

##### Error Handling 
With `-T`, the user can set a network timeout which, when reached for any given page, will
cancel the download of that particular page without stopping the transfer as a whole.

With `-t`, the user can specify the number of *tries* to attempt, allowing the user to continue
querying a site until it is fetched successfully.

With `-w`, the user can specify a delay, which the program applies between consecutive
fetch requests. This is useful to prevent getting rejected from a website for querying it too
frequently.

Ultimately, these three flags can be combined to attempt to retrieve a website for an 
extended period of time, as seen below.
~~~ bash
# Attempt to download a website that goes down a lot over the course of
# an hour
$ wget -T 30 -t 40 -w 60 https://www.google.com/
~~~
