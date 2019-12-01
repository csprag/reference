WSL
-------

Windows Subsystem for Linux is a Windows app that lets you run a Linux terminal alongside your Windows desktop. WSL is great for those who want to run Bash commands and common Linux tools like `sed` and `awk` without the clunkiness virtual machine.


### Installation Guide
---
1. Open PowerShell as Administrator and run:
```sh
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
2. Install the Linux distro of your choice from the Microsoft Store.   
Some common distros for WSL:   
  **[Ubuntu 16.04](https://www.microsoft.com/en-us/p/ubuntu-1604-lts/9pjn388hp8c9?rtc=1&activetab=pivot:overviewtab)**   
  **[Ubuntu 18.04](https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?rtc=1&activetab=pivot:overviewtab)**   
  **[OpenSUSE Leap 15](https://www.microsoft.com/en-us/p/opensuse-leap-15/9n1tb6fpvj8c?rtc=1&activetab=pivot:overviewtab)**   
  **[Debian GNU/Linux](https://www.microsoft.com/en-us/p/debian/9msvkqc78pk6?rtc=1&activetab=pivot:overviewtab)**

3. Setup Your Subsystem   
Launch your new app and enter a username and password when prompted.
Then update your packages:
~~~ bash
$ sudo apt update && sudo apt upgrade
~~~

### FAQ's
##### Where are my files?
Your Linux root is mounted beneath the C Drive. To access your windows files
~~~ bash
$ cd /mnt/c
~~~

Or to access the desktop

~~~ bash
$ cd /mnt/c/Users/<your username>/Desktop
~~~

##### Can I customize the terminal?
Are the base colors or font of WSL are really grinding your gears? What if you're like me and you really want tabs? Your best bet is probably downloading a console emulator such as Cmder.
This is a pretty good tutorial that shows you how to do just that:  
**[Cmder with WSL](https://jackwarren.info/blog/cmder)**  
Right now I'm digging the 'SolarMe' color scheme


### Tips
##### Open up your current directory in File Explorer
~~~ bash
$ explorer.exe .
~~~

This even works if you're in your Linux files below the C drive

##### Change default directory
If you'd rather WSL open an other folder than the root directory by default (such as your eecs281 folder), you have to change you .bashrc file located in the root directory.
Navigate to root directory
~~~ bash
cd ~
~~~
Then add cd <default directory> to the end of the .bashrc file using your terminal editor.
~~~ bash
$ nano ~/.bashrc .
~~~
or by opening it in the File Explorer

~~~ bash
$ explorer.exe .
~~~

##### Where to store project files
Of course do whatever works best for you, but I like to store my project files in a folder directly after the C drive in order to make them easily accessible from the file Explorer for copying/drag and drop, while also minimizing your file path
