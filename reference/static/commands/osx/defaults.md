defaults
-------

`defaults` is an OSX command that gives access to the Mac OS X user defaults system. 

~~~ bash
$ defaults write com.apple.finder AppleShowAllFiles -bool TRUE 
~~~

---

### Details
`defaults` allows the user to read, write, and delete Max OS X defaults from terminal. These preferences are meant to be persistent when apps aren't running.   

*Note:* Avoid modifying defaults of a running application.

Defaults belong to __domains__ which typically correspond to individual applications. A domain has a dictionary of key-value pairs representing defaults. Keys are always strings, but the values can be complex data structures such as arrays, binary, etc. 

Below is the synopsis from the man page:


```
defaults [-currentHost | -host hostname] read [domain [key]]

defaults [-currentHost | -host hostname] read-type domain key

defaults [-currentHost | -host hostname] write domain { 'plist' | key 'value' }

defaults [-currentHost | -host hostname] rename domain old_key new_key

defaults [-currentHost | -host hostname] delete [domain [key]]

defaults [-currentHost | -host hostname] { domains | find word | help }
```
### Useful Options / Examples

### defaults domains
~~~ bash
$ defaults domains

Mixpanel, MobileMeAccounts, ckkeyrolld, com.apple.ActivityMonitor, com.apple.AddressBook, com.apple.AppleMultitouchMouse, com.apple.AppleMultitouchTrackpad,
...
~~~

#### Break it down
- This command lets you see all valid domains already being used by an application. 


#### `defaults write [domain] [key] -[datatype] [value]` 
~~~ bash
$ defaults write com.apple.finder AppleShowAllFiles -bool TRUE
~~~

#### Break it down

- The `defaults write` command is used for setting a default setting.
- Access the list of domains with `defaults domains`.
- Some valid datatypes:
    * `-string` 
    * `-data` (takes in raw bytes as hexidecimal)
    * `-int[eger]`
    * `-float`
    * `bool[ean]` (values must be TRUE, FALSE, YES, or NO)
    * `-date`
    * `-array` (example: `defaults write somedomain preferenceKey -array element1 element2 element3`)
    * `-dict` (example: `defaults write somedomain preferenceKey -dict key1 value1 key2 value2`)
    * `-dict-add` (allows the user to update an existing dictionary)
