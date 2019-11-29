FIGlet
---
`figlet` is a command that can be used to draw large sized text banners

To use `figlet`, type:

~~~bash
$ figlet bannertext
~~~
---
FIGlet prints its input using large characters made up of ordinary screen characters. FIGlet output is generally reminiscent of the sort of "signatures" many people like to put at the end of e-mail and UseNet messages.

`figlet`  is not built-in to your terminal and in order to use it, you have to install it to your machine. 

To install on Linux, type:

~~~bash
$ sudo apt-get install figlet
~~~

To install on macOS, type:

~~~bash
$ brew install figlet
~~~

### Useful Commands / Examples 
- `figlet -c bannerText` centers the output
- `figlet -p < myfile` outputs text input from a file

#### Example command
~~~bash
$ figlet big baller brand
~~~
~~~ bash
 _     _         _           _ _             _                         _ 
| |__ (_) __ _  | |__   __ _| | | ___ _ __  | |__  _ __ __ _ _ __   __| |
| '_ \| |/ _` | | '_ \ / _` | | |/ _ \ '__| | '_ \| '__/ _` | '_ \ / _` |
| |_) | | (_| | | |_) | (_| | | |  __/ |    | |_) | | | (_| | | | | (_| |
|_.__/|_|\__, | |_.__/ \__,_|_|_|\___|_|    |_.__/|_|  \__,_|_| |_|\__,_|
         |___/                                                  
~~~
