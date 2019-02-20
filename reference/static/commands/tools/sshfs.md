sshfs
-------

sshfs allows you access files from a server using SSH, as if they were on your local machine.

~~~ bash
cd ~/Desktop
mkdir new_folder
sshfs uniqname@login.engin.umich.edu: new_folder
~~~

---

### Useful Options / Examples

#### `sshfs uniqname@login.engin.umich.edu: new_folder`

Connects to the SSH server at `uniqname@login.engin.umich.edu` and mounts the root directory where `new_folder` is located on your computer.

##### Break it down

sshfs requires a user to specify a folder (`new_folder` in this instance) as a location for the root directory. Then, it will connect to the specified server (in this case, a user's CAEN account) and mount that user's `~` directory at that folder – `folder` will be replaced by a disk that contains the `~` folder. You can then access the SSH server as any other folder on your computer, dragging and dropping files in and out of it, or accessing it through Terminal.

#### `umount new_folder`

End the SSH session and unmount the SSH directory.

##### Break it down

This command unmounts the directory from your computer. The mounted disk will be replaced by the initial folder (`new_folder` in this case), and the session will end. This command requires you to remember the name of the folder you created for sshfs purposes.
