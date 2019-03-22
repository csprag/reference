cal
-------
cal shows a ascii calendar in terminal that has the current date highlighted.
(ncal and cal are roughly the same thing)


~~~ bash
cal
   February 2019      
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28      


ncal
    February 2019     
Su     3 10 17 24   
Mo     4 11 18 25   
Tu     5 12 19 26   
We     6 13 20 27   
Th     7 14 21 28   
Fr  1  8 15 22      
Sa  2  9 16 23   
~~~

---

### Useful Options / Examples
- `-h` - Turns off highlighting of today.
- `-j` - Display Julian Calendar, if combined with the -o option, display date of Orthodox Easter according to the Julian Calendar.
- `ncal -e` -  Display date of Easter (for western churches).
- `-m month` - Display the specified month.  If month is specified as a decimal number, appending ‘f’ or ‘p’ displays the same month of the following or previous year respectively.
- `ncal -o` - Display date of Orthodox Easter
- `ncal-p` - Print the country codes and switching days from Julian to Gregorian Calendar
- `-y` - Display a calendar for the specified year.
- `-3` - Display the previous, current and next month surrounding today.
- `-1` - Display only the current month. This is the default.
- `-A number` - Months to add after. The specified number of months is added to the end of the display.
- `-B number` - Months to add before. The specified number of months is added to the beginning of the display.
- `-C` - Completely switch to cal mode. For cal like output only, use -b instead.
- `-N` - Switch to ncal mode.
- `-M` - Weeks start on Monday.
- `-S` - Weeks start on Sunday.
- `-b` - Use oldstyle format for ncal output.
- `` - 


#### Example command
- `cal -y 1999`
~~~ bash
cal -y 1999
                                  1999
    January           February          March             April             
Su     3 10 17 24 31     7 14 21 28        7 14 21 28        4 11 18 25   
Mo     4 11 18 25     1  8 15 22        1  8 15 22 29        5 12 19 26   
Tu     5 12 19 26     2  9 16 23        2  9 16 23 30        6 13 20 27   
We     6 13 20 27     3 10 17 24        3 10 17 24 31        7 14 21 28   
Th     7 14 21 28     4 11 18 25        4 11 18 25        1  8 15 22 29   
Fr  1  8 15 22 29     5 12 19 26        5 12 19 26        2  9 16 23 30   
Sa  2  9 16 23 30     6 13 20 27        6 13 20 27        3 10 17 24      

    May               June              July              August            
Su     2  9 16 23 30     6 13 20 27        4 11 18 25     1  8 15 22 29   
Mo     3 10 17 24 31     7 14 21 28        5 12 19 26     2  9 16 23 30   
Tu     4 11 18 25     1  8 15 22 29        6 13 20 27     3 10 17 24 31   
We     5 12 19 26     2  9 16 23 30        7 14 21 28     4 11 18 25      
Th     6 13 20 27     3 10 17 24        1  8 15 22 29     5 12 19 26      
Fr     7 14 21 28     4 11 18 25        2  9 16 23 30     6 13 20 27      
Sa  1  8 15 22 29     5 12 19 26        3 10 17 24 31     7 14 21 28      

    September         October           November          December          
Su     5 12 19 26        3 10 17 24 31     7 14 21 28        5 12 19 26   
Mo     6 13 20 27        4 11 18 25     1  8 15 22 29        6 13 20 27   
Tu     7 14 21 28        5 12 19 26     2  9 16 23 30        7 14 21 28   
We  1  8 15 22 29        6 13 20 27     3 10 17 24        1  8 15 22 29   
Th  2  9 16 23 30        7 14 21 28     4 11 18 25        2  9 16 23 30   
Fr  3 10 17 24        1  8 15 22 29     5 12 19 26        3 10 17 24 31   
Sa  4 11 18 25        2  9 16 23 30     6 13 20 27        4 11 18 25    
~~~

#### Example command
- `cal -3`
~~~ bash
cal -3
                            2019
      January               February               March          
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
       1  2  3  4  5                  1  2                  1  2  
 6  7  8  9 10 11 12   3  4  5  6  7  8  9   3  4  5  6  7  8  9  
13 14 15 16 17 18 19  10 11 12 13 14 15 16  10 11 12 13 14 15 16  
20 21 22 23 24 25 26  17 18 19 20 21 22 23  17 18 19 20 21 22 23  
27 28 29 30 31        24 25 26 27 28        24 25 26 27 28 29 30  
                                            31                  
~~~





