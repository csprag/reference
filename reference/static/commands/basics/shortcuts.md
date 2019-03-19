keyboard shortcuts
-------

Keyboard shortcuts can be used to quickly and efficiently work in the command-line.

~~~ bash
$ cd Doc<Tab>
$ cd Documents/
~~~

---

### Useful Shortcuts

#### Tab Completion

 * `Tab` automatically completes the file, directory, or command being typed

#### Cutting and Pasting

 * `ctrl+W` cuts the word before the cursor, adding it to the clipboard.
 * `ctrl+U` cuts the part of the line before the cursor, adding it to the clipboard.
 * `ctrl+K` cuts the part of the line after the cursor, adding it to the clipboard.
 * `ctrl+Y` pastes the last thing cut from the clipboard.
 * Note: `ctrl+Y` only pastes the last thing cut from the clipboard using `ctrl+W`, `ctrl+U`, or `ctrl+K`.  To paste something you cut/copied from outside the terminal, use `Shift+Insert`.

#### Recalling Previous Commands

 * Pressing the `Up Arrow` key or `ctrl+P` goes to the previous command in the command history. Can be used multiple times in a row to walk back through the history.
 * Pressing the `Down Arrow` key or `ctrl+N` goes to the next command in the command history. Can be used multiple times in a row to walk forward through the history.
 * `ctrl+R` enters recall mode. Press this shortcut and start typing to search your command history for a command.
 * `ctrl+O` runs a command found with `ctrl+R`.
 * `ctrl+G` leaves recall mode without running a command.

#### Controlling Active Commands/Processes

 * `ctrl+C` interrupts and ends the current command/process.
 * `ctrl+Z` pauses the current command/process and moves it into the background.
 * `ctrl+D` closes the terminal

#### Controlling the Screen

 * `ctrl+L` clears the screen, similar to the `clear` command.
 * `ctrl+S` stops all output to the screen. This is useful when running commands with lots of output.
 * `ctrl+Q` resumes printing output to the screen after stopping it with `ctrl+S`.

#### Moving the Cursor

 * `ctrl+A` moves to the beginning of the line, similar to the `Home` key.
 * `ctrl+E` moves to the end of the line, similar to the `End` key.
 * `ctrl+B` moves left (back) one character.
 * `ctrl+F` moves right (forward) one character.
 * `alt+B` moves left (back) one word.
 * `alt+F` moves right (forward) one word.
 * `ctrl+XX` moves between the beginning of the line and the current position of the cursor.

#### Editing Text

##### Deleting Text

 * `ctrl+D` deletes the character under the cursor, similar to the `Delete` key.
 * `alt+D` deletes all characters after the cursor on the current line.
 * `ctrl+H` deletes the character before the cursor, similar to the `Backspace` key.

##### Fixing Typos

 * `ctrl+T` swaps the last two characters before the cursor with each other.
 * `alt+T` swaps the current word with the previous word.
 * `ctrl+_` undose the last key press.

##### Capitalizing Characters

 * `alt+U` capitalizes every character from the cursor to the end of the current word.
 * `alt+L` uncapitalizes every character from the cursor to the end of the current word.
 * `alt+C` capitalizea the character under the cursor. The cursor will then move to the end of the current word.
