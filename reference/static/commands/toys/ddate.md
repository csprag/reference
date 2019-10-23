ddate
-------
Gives the date according to the Discordian calendar.
More information can be found here: https://en.wikipedia.org/wiki/Discordian_calendar
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ ddate
Today is Sweetmorn, the 4th day of The Aftermath in the YOLD 3185
~~~

---

### Useful Options / Examples

(From the man page)

    %A     Full name of the day of the week (i.e., Sweetmorn)

    %a     Abbreviated name of the day of the week (i.e., SM)

    %B     Full name of the season (i.e., Chaos)

    %b     Abbreviated name of the season (i.e., Chs)

    %d     Ordinal number of day in season (i.e., 23)

    %e     Cardinal number of day in season (i.e., 23rd)

    %H     Name of current Holyday, if any

    %N     Magic code to prevent rest of format from being printed unless today is a Holyday.

    %n     Newline

    %t     Tab

    %X     Number of days remaining until X-Day. (Not valid if the SubGenius options are not compiled in.)

    %{ %}     Used to enclose the part of the string which is to be replaced with the words "St. Tib's Day" if the current day is St. Tib's Day.

#### Example command
~~~ bash
$ ddate +'Today is %{%A, the %e of %B%}, %Y. %N%nCelebrate %H'
Today is Sweetmorn, the 4th of The Aftermath, 3185.
~~~

##### Break it down

These commands are within the %{ %} so in the case of it being St. Tib's day, the date is displayed properly. Wherever there is a % followed by a character, the appropriate value will be replaced at that spot:
    1. %A requests the full name of the month, in this case Sweeetmorn (October in the Gregorian Calendar)
    2. %e gives the date in the ordinal format, in this case the 4th
    3. %B prints the full name of the season
Then, %Y will print the year in according the Discordian calendar.
These next commands will work when there if today is Holyday (the fifth day of every season)
    1. %N, as stated in the documentation is magical.
    2. %n will create a newline
    3. Print a celebration message

