man
-------

man is a command used to display the user manual of commands run in the terminal.

~~~ bash
$man ls
~~~

---

###Details
These manuals or "man pages" are compiled from different sources depending on what programs you have installed and you can find this information at the top of the man page.

Every manual is divided into serveral sections to help users learn more about the commands they are running. These sections include: Name, Synopsis, Description, Examples, Diagnostics, Environment, Exit Status, Compatability, See Also, Standards, History, and Bugs.

### Useful Options / Examples

####man echo
~~~bash
$man echo
ECHO(1)			BSD General Commands Manual 		Echo(1)
NAME
	echo -- write arguments to the standard output

SYNOPSIS
	echo [-n] [string ...]

DESCRIPTION
	The echo utility writes any specified operands, separated by single blank
	(` ') characters and followed by a newline(`\n') character, to the stan-
	dard output.
	
	The following option is available:

	-n	Do not print the trailing newline character. This may also be
		achieved by appending `\c' to the end of the string, as is done by
		iBCS2 compatible systems. Note that this option as well as the
		effect of `\c; are implementation-defined in IEEE Std 1003.1-2001
		(``POSIX.1'') as amended by Cor. 1-2002. Applications aiming for
		maximum portability are strongly encouraged to use printf(1) to
		suppress the newline character.

	Some shells may provide a builtin echo command which is similar or iden-
	tical to this utility. Most notably, the builtin echo in sh(1) does not
	accept the -n option. Consult the builtin(1) manual page.

EXIT STATUS
	The echo utilit exits 0 on success, and >0 if error occurs.

SEE ALSO
	builtin(1), csh(1), printf(1), sh(1)

STANDARDS
	The echo utility conforms to the IEEE Std 1003.1-2001 (``POSIX.1'') as
	amended by Cor. 1-2002.

BSD				April 12, 2003				     BSD
~~~

