fortune
-------
fortune is a Linux command that displays random, silly, or inspirational quotes and phrases.

To use fortune, simply type:
~~~ bash
fortune
~~~

---

### Useful Options / Examples

#### Example command
~~~ bash
fortune
The day after tomorrow is the third day of the rest of your life.
~~~
##### Break it down
In order to use fortune, you have to install it to your machine. If you are using a linux machine, do the following step to install:
~~~ bash
sudo apt install fortune
~~~
#### Example command
~~~ bash
fortune
Keep in mind always the four constant Laws of Frisbee:
(1) The most powerful force in the world is that of a disc straining to land under a car, just out of reach (this force is technically termed "car suck").
(2) Never precede any maneuver by a comment more predictive than "Watch this!"
(3) The probability of a Frisbee hitting something is directly proportional to the cost of hitting it.  For instance, a Frisbee will always head directly towards a policeman or a little old lady rather than the beat up Chevy.
(4) Your best throw happens when no one is watching; when the cute girl you've been trying to impress is watching, the Frisbee will invariably bounce out of your hand or hit you in the head and knock you silly.
~~~
# Please enter the commit message for your changes. Lines starting
##### Break it down
-l - when run with -l, fortune will only use quotations longer than the length specified by -n, or 160 characters if -n is not used

-s - when run with -s, fortune will only use quotations shorter than the length specified by -n, or 160 characters if -n is not used

-n - this will set the length used by -l and -s to determine "long" and "short"messages (default is 160 characters)

-o - when run with -o, fortune will only display "offensive" messages. By default, fortune will only display messages deemed inoffensive

-a - when run with -a, fortune will display a message from all databases, whether or not they are "offensive"
