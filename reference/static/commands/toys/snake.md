snake
-------
`snake` is a command that allows a snake game to be played in the terminal.

To start `snake`, simply type the following:

<!-- minimal example -->
~~~ bash
$ sudo apt install bsdgames
$ snake
~~~

---

### Useful Options / Examples
~~~ bash
 Usage: snake [-w width] [-l length] [-t]
 -w: Width of the field
 -l: Length of the field
 -t: Game assumes you are on a slow terminal
~~~

#### Example command
~~~ bash
snake -w 50
snake -l 100
snake -t
~~~

##### Break it down

`snake` is a display-based game which must be played on a CRT terminal. The object of the game is to make as much money as possible without getting eaten by the snake. To earn money, move to the same square the money is on. The main controls are h, j, k, and l work as well as the arrow keys.

#### Controls
- arrow keys
- `hjkl` - Same moving conventions as used in vi
- `sefc` - These keys are like hjkl but form a directed pad around the d key
- `HJKL` - These keys move you all the way in the indicated direction to the same row or column
- `ATPB` - These keys move you to the four edges of the screen

#### Useful Commands
- `x` - quit the game
- `p` - points in direction you might want to go
- `w` - space warp to get out of tight squeezes
