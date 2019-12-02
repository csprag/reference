htop
---
`htop` is an interactive alternative to `top` that also offers various graphical displays of system information (e.g. CPU load).
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ htop
~~~

---

### Useful Options / Examples

#### Killing a process
One use is to easily kill a process that is seen to be using up resources:

1. Select the process with the cursor or arrow keys
    * You can select multiple processes to perform the same action on by tagging/untagging them by pressing `Space` when the process is highlighted
1. Open the "Kill" menu by pressing `F9`
2. Navigate to the signal to send and press `Enter` or type the number of its value

#### Sorting by a column
In `htop`'s sorted view, processes can be sorted by any column:

* Click on the column to sort by

OR

1. Enter the "SortBy" menu by pressing `F6` 
2. Navigate to the column to sort by and press `Enter`

#### Switching between views
Besides the default sorted view, `htop` also offers a tree view. Press `F5` to toggle between the two.

#### Installation
##### Ubuntu
~~~ bash
$ sudo apt-get install htop
~~~

##### macOS
~~~ bash
$ brew install htop
~~~
