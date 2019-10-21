
units
---

`units` helps you to convert from one measurement unit to another.

~~~ bash
$ units
You have: pounds
You want: ounces
	* 16
	/ 0.0625
~~~

---

### Useful Options / Examples
* `-q` : Suppress prompting of the user for units and the display of statistics about the number of units loaded.
* `-v` : Print the version number of the units command.

Command format: `$ units [OPTIONS] [FROM-UNIT] [TO-UNIT]`
or 
For interactive units program: `$ units`

#### `units [FROM-UNIT TO-UNIT]`  

~~~ bash
$ units [FROM-UNIT] [TO-UNIT]
	* [numeric value] 
	/ [numeric value 2]
~~~

1. `units` takes the FROM-UNIT and the TO-UNIT and finds the conversion rates between the two.
2. `[numeric value]` is the value you can multiply the FROM-UNIT by to get the TO-UNIT value.
3. `[numeric value 2]` is the value you can divide the TO-UNIT by to get the FROM-UNIT value.
4. Note that the units command can only specify conversions by multiplication or division. Ie. it cannot make conversions that involve addition/subtraction such as Fahrenheit to Celsius

### More Examples
~~~ bash
$ units
You have: 3 pounds
You want: ounces
	* 48
	/ 0.020833333
You have: 2*pi inches
You want: inches
	* 6.2831853
	/ 0.15915494
You have: liters/sec
You want: liters/min
	* 60
	/ 0.016666667
You have: 36884
You want: 2334
	* 15.802913
	/ 0.063279471

~~~
You can do conversions with constants. You can convert rates. You can even do some basic math. 

### Reference
To see the full documentation use the command `man units`
