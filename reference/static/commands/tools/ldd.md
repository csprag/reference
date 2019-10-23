ldd
------

 `ldd`, or *List Dynamic Dependencies*, is a Linux command that displays the shared libraries that are required by a given program. This is useful for finding out whether there are missing dependencies, functions, or objects required by the program.                              

~~~bash
$ldd [option]... file...
~~~

Be wary of running this command on untrusted program executables because `ldd` could execute the program. In this case, `objdump` may be a safer option for displaying information .

------

### Useful Options / Examples

An example use of `ldd`:

~~~bash
$ldd filter_test
	linux-vdso.so.1 (0x00007ffe668af000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f7a19453000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f7a190b5000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f7a18e9d000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f7a18aac000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f7a199e7000)
~~~

Using one or more of the following command flags will do as describes:

#### `ldd -d` 

The `-d` option tells the script to process any relocations of data.

#### `ldd -r` 

The `-r` option tells the script to process relocations of both data and functions.

#### `ldd -u`

The `-u` option tells the script to print all unused direct dependencies.

#### `ldd -v`

The `-v` option tells the script to be verbose, or to print out all information while running. This mainly means it will show version information of the shared libraries, as well as their paths and addresses in memory.

And example using the `-v` flag with the same executable as above:

~~~bash
$ldd -v filter_test
	linux-vdso.so.1 (0x00007ffcc8773000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fbbd1233000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fbbd0e95000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fbbd0c7d000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fbbd088c000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fbbd17c7000)

	Version information:
	./filter_test:
		libgcc_s.so.1 (GCC_3.0) => /lib/x86_64-linux-gnu/libgcc_s.so.1
		libm.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libm.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
		libstdc++.so.6 (GLIBCXX_3.4.11) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
		libstdc++.so.6 (GLIBCXX_3.4.9) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
		libstdc++.so.6 (CXXABI_1.3.9) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
		libstdc++.so.6 (CXXABI_1.3) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
		libstdc++.so.6 (GLIBCXX_3.4.21) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
		libstdc++.so.6 (GLIBCXX_3.4) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
	/usr/lib/x86_64-linux-gnu/libstdc++.so.6:
		libm.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libm.so.6
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		libgcc_s.so.1 (GCC_4.2.0) => /lib/x86_64-linux-gnu/libgcc_s.so.1
		libgcc_s.so.1 (GCC_3.3) => /lib/x86_64-linux-gnu/libgcc_s.so.1
		libgcc_s.so.1 (GCC_3.0) => /lib/x86_64-linux-gnu/libgcc_s.so.1
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.18) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.16) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.17) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3.2) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libm.so.6:
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_PRIVATE) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libgcc_s.so.1:
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libc.so.6:
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
~~~

##### Tips for Usage

When using `ldd` you must either be in the directory of the executable or have the path to the directory the executable is in. A reliable way to find this path is to type:

~~~bash
$whereis file
~~~

This will output the path to the executable, which you can use with the `ldd` command.

 