XCode
----
XCode is a free IDE (integrated development environment) for macOS. It is the go-to editor for iOS, macOS, iPadOS, watchOS, and tvOS. It also works great for C and C++. You can only use it on macOS. [Download Link](https://apps.apple.com/us/app/xcode/id497799835?mt=12)

---

## Why XCode?

#### Fully featured IDE
XCode supports crucial features like setting break points, jumping forward/back/into code, and a built in terminal.

#### Built in simulators
There are other options out there to avoid using XCode for Swift/Objective-C development. For instance, AppCode, or creating cross-platform products in languages like Vue or React-Native. However, these products do not have built-in simulators. XCode allows you to run your code for iOS on your computer through simulators. You can even select the OS version and device type to test.  

#### Run programs with a single press
You can create schemes that will pass in the required arguments to your script and then run it with a single click.

For example, if you have a C++ script that you would need to compile and then run from the command line with:
```
$ g++ -o program program.cpp
$ ./program.out <input_file> <output_file>
```

You can easily convert this to a new scheme. With the XCode editor open, click on the scheme dropdown (next to the stop button on the top toolbar). Select edit scheme -> run and then go to "Arguments Passed on Launch". You can then click the plus button to add a new argument.

You can then add the arguments that you would like to pass. For instance, you might add:
```
"~/usr/.../path/to/input.txt" "~/usr/.../path/to/output.txt"
```

Note that you need to use the absolute paths to the files and place the file names in double quotes.

See this [article](https://zeemee.engineering/how-to-set-up-multiple-schemes-configurations-in-xcode-for-your-react-native-ios-app-7da4b5237966) if you need more help


#### Easily create a testing suite
You can easily create a testing suite that you can run automatically.

When using Swift, XCode creates test file templates for you and provides easy to use tools such as setting up your test, tearing down your test, and measuring the speed to perform a block of code.

#### Visualize Git Diff

You can easily view all the changes you made since your last commit using the double arrow symbol on the top tool bar. On the left side is your most recent file and on the right side is the previous commit (by default). You can easily undo changes or pull things in you deleted. It makes it very easy to see exactly what you have done if you come back to some uncommitted changes.

#### Find anything
You can search within a file for text using CMD+F. You can search your entire project using CMD + SHIFT + F. XCode provides an easy interface for searching for patterns or for handling cases correctly. The global search will show you all the files that were matched and a preview of the text matched.

### Built in keyboard shortcuts
There are very useful keyboard shortcuts built into XCode.

| Shortcut               	| What it does                                                                	| Command         	|
|------------------------	|-----------------------------------------------------------------------------	|-----------------	|
| Open project navigator 	| Opens up your project navigator to view all your files.                     	| CMD + 1         	|
| Toggle Navigator Panel 	| Shows/closes the navigator panel that provides more details for your files  	| CMD + 0         	|
| Toggle Utilities Panel 	| Show/closes the utilities panel                                             	| CMD + OPT + 0   	|
| File Search            	| Search current file                                                         	| CMD + F         	|
| Project Search         	| Search through the entire project                                           	| CMD + SHIFT + F 	|
| File Jump              	| Easily jump to functions or sections                                        	| CTRL + 6        	|
| Open Quickly           	| Start typing in text or a file name and easily jump to instances of it      	| CMD + SHIFT + O 	|
| Quick C Switch         	| Switch easily between the header file and the corresponding .c or .cpp file 	| CTRL + CMD + Up 	|
| Format code            	| Easily format a block of selected code                                      	| CTRL + i        	|
