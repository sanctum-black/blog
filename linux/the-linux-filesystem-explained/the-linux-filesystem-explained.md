# The Linux Filesystem Explained
A **filesystem** is a method and data structure used by operating systems to manage how data is stored, organized and retrieved. Each operating system has a different filesystem with different logical rules and structure. Also, every external storage device has a filesystem included. Without this, data storage & data retrieval would be impossible.

File systems perform multiple functions. They are responsible for:
- User data management
- Space management
- Filenames
- Directories
- Metadata
- Access permission & restriction
- Data integrity

In this article, we will go over the Linux directory tree starting from the root directory. We will then discuss the utility and functions of each directory, their relation with the Linux Kernel and some important utilities for interacting with the filesystem.

We will be using a terminal emulator and `bash` commands in order to illustrate some examples.

---

## Table of Contents
- Overview
	- The Windows filesystem
	- The macOS filesystem
	- The Linux filesystem
- Preparing our environment
	- A word of caution
	- Choosing a distribution, an emulator and a shell
	- Installing a useful package

---

## Overview
As stated earlier, a filesystem is a way for operating systems to interact with the data saved in hard drives. Each operating system family has its own filesystem. Without going much into detail, we can  mention the 3 main operating systems used today.

### 1. The Windows filesystem
The current Windows filesystem dates back to MS-DOS *(Microsoft Disk Operating System)*, the command-line based operating system which originally was used to run the Windows operating system. MS-DOS used letters to assign drives, which, back in the time represented physical floppy disks. Some years later, internal hard drives were made available and Microsoft designated the letter `C` for its internal hard drive. Currently, all Windows program files are installed on `C:\Program Files`.

### 2. The Linux filesystem
Linux is a UNIX-like operating system. The UNIX structure was fundamentally different from MS-DOS when created, and upon evolving, Linux adopted most of its conventions, including the filesystem. Linux, as opposed to Windows, has a hierarchical file structure; it contains a root directory and its subdirectories. Also, Linux treats most of it's components as files.

Interestingly, not all Linux distributions manage their directory structure equally. For example, a given distribution may use `/media` for mounting external drives, while another one may use `/run`. Still, the detailed information regarding directory structures for a given distribution, can be found on it's respective documentation site. Ubuntu's filesystem structure can be found [here](https://help.ubuntu.com/community/LinuxFilesystemTreeOverview). 

### 3. The macOS filesystem
MacOS is more similar to Linux since it evolved from a similar UNIX-like operating system called BSD. It has the same hierarchical file structure, but the executables are not binary-compatible with Linux.

---

## Preparing our environment

### 1. A word of caution

**A word of caution before we begin:** Some of the directories we'll review, such as `/boot`, contain vital information for the Linux operating system to function properly. If we were to access them using `root` privileges and accidentally delete or modify their content, we could easily break our operating system.

A great option for avoiding messing up when tinkering around, is to use a Virtual Machine; if we were to break anything, we could easily restore from a snapshot, or even do a fresh reinstall.

### 2. Choosing a distribution, an emulator and a shell

Given that we already have a Linux distribution installed, we can start by getting our hands on a terminal emulator and a shell. All distributions come with at least one terminal emulator and one shell already installed. The most common shell is `bash`. As for terminal emulators, it depends which family of distributions and which desktop manager we installed.

In our case, we'll be using Ubuntu running on Windows WSL2. We'll be using the windows Terminal as our terminal emulator, and `zsh` as our shell. The WSL2 setup process is out of the scope of this article, but will be covered in the future.

Ubuntu is a distribution which is based on Debian, so the filesystem will be similar for the two, and also, we'll be able to use either the `apt` or the `dpkg` package managers for installing terminal utilities.

### 3. Installing two useful packages
A great deal of the packages we'll be using already come preinstalled on Ubuntu. For the remaining ones, we can use the two package managers mentioned, depending on our preference:
- `apt` : The native Ubuntu package manager.
- `dpkg` : The native Debian package manager.

For this example, we'll be using Ubuntu's `apt`.

We'll first install the `tree` package used for visualizing our directory structure in a tree-like diagram.
To confirm we don't yet have the `tree` package:

##### **Code**
```Bash
tree
```

##### **Output**
```
Command 'tree' not found, but can be installed with:
sudo apt install tree
```

We can then install it:

##### **Code**
```Bash
sudo apt install tree
```

The shell will prompt us for our `sudo` password.

Upon inputting it, we can see what `apt` will install for us:

##### **Output**
```
The following NEW packages will be installed:
  tree
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
```

We can also install the `htop` command line utility used for monitoring and managing active processes, something similar to the Task manager application on Windows.

##### **Code**
```Bash
sudo apt install htop
```

---

## /
This is the root directory, and is the uppermost directory in the Linux system containing all the files, device data and system information. 

If we're executing our terminal emulator as a user different than `root`, the shell will start in `/home/ourusername`. This is the home directory for our user. We can confirm where we are by executing the following command:

##### Code
```Bash
pwd
```

##### Output
```
/home/pabloagnck
```

Now that we know where we are, we can change directories to the `root` directory by executing the following:

##### Code
```Bash
cd ../..

pwd
```

The two periods `..` allow us to change directory to the relative parent directory we are currently in.
If we do that two times with a slash `/` in between, we can change directories to the `root` directory  `/`.

##### Output
```
/
```

If we execute the `tree` command without any parameters, it will recursively go over every directory and file on `/` and list it. We don't want that. Instead, we can specify a recursion level which will list only the immediate directories.

##### **Code**
```Bash
tree -L 1
```

##### **Output**
```
.
|-- bin -> usr/bin
|-- boot
|-- dev
|-- etc
|-- home
|-- lib -> usr/lib
|-- lost+found
|-- media
|-- mnt
|-- opt
|-- proc
|-- root
|-- run
|-- sbin -> usr/sbin
|-- snap
|-- srv
|-- sys
|-- tmp
|-- usr
`-- var
```

We can see that 21 directories were listed:
- The first directory `.` denotes the current directory `/`.
- The ones with the arrow symbol on the right `->` denote symbolic links, or `symlinks`. This means they're actually links pointing to other directory.

Each directory has an `owner` and a `group` assigned. If we recall, the file structure in Linux is hierarchical. It's based on a set of standards called the [FHS](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) *(File Hierarchy Standard)*; all directories immediately below `/` will have `root` as their owner. We can confirm this by using the list `ls` command with the single column output parameter `-l`:

##### **Code**
```Bash
ls -l
```

##### **Output**
```
lrwxrwxrwx   1 root root       7 Oct 25 16:34 bin -> usr/bin
drwxr-xr-x   2 root root    4096 Apr 18  2022 boot
drwxr-xr-x  10 root root    3040 Jan 27 22:19 dev
drwxr-xr-x  79 root root    4096 Jan 27 22:19 etc
drwxr-xr-x   3 root root    4096 Dec 16 12:07 home
-rwxrwxrwx   1 root root 1939720 Dec 31  1969 init
lrwxrwxrwx   1 root root       7 Oct 25 16:34 lib -> usr/lib
lrwxrwxrwx   1 root root       9 Oct 25 16:34 lib32 -> usr/lib32
lrwxrwxrwx   1 root root       9 Oct 25 16:34 lib64 -> usr/lib64
lrwxrwxrwx   1 root root      10 Oct 25 16:34 libx32 -> usr/libx32
drwx------   2 root root   16384 Dec 16 12:06 lost+found
drwxr-xr-x   2 root root    4096 Oct 25 16:34 media
drwxr-xr-x   6 root root    4096 Dec 16 12:06 mnt
drwxr-xr-x   2 root root    4096 Oct 25 16:34 opt
dr-xr-xr-x 263 root root       0 Jan 27 22:19 proc
drwx------   4 root root    4096 Dec 16 23:31 root
drwxr-xr-x   7 root root     140 Jan 27 22:45 run
lrwxrwxrwx   1 root root       8 Oct 25 16:34 sbin -> usr/sbin
drwxr-xr-x   8 root root    4096 Oct 25 16:36 snap
drwxr-xr-x   2 root root    4096 Oct 25 16:34 srv
dr-xr-xr-x  11 root root       0 Jan 27 22:19 sys
drwxrwxrwt   3 root root    4096 Jan 27 22:19 tmp
drwxr-xr-x  14 root root    4096 Oct 25 16:34 usr
drwxr-xr-x  13 root root    4096 Oct 25 16:35 var
```

The third column from left to right, denotes the `owner`. The fourth one denotes the `group`.

As we go over the directory structure, we will notice that, as opposed to Windows, the directory & system file names are intuitive; they're acronyms for actual names describing their purpose. This is also part of the UNIX philosophy and applies not just to the directory structure, but to commands also.

---

## /bin
The `/bin` directory stands for **binary**, and contains the most basic executables such as `ls`, `man` and `cat`. 


---

## /boot
The `/boot` directory contains everything necessary for the operating system to boot. Here, we can find:
- The bootloader
- The Linux image files

We need to be careful with this directory, since deleting or modifying files could cause our system to stop working.

---

## /dev
The `/dev` directory stands for **devices**. A device in the Linux context refers to any `I/O` device we.


---

## /etc
The `/etc` directory stands for **etcetera**, and contains all system-wide configuration files. Applications installed for all users will have system-wide settings in this directory. 

---

## /home
The `/home` directory

---

## /lib, /lib32, /lib64
The `/lib`, `/lib32` and `/lib64` stand for **libraries**, and contain files that applications can use to perform various functions. 

---

## /lost+found
The `/lost+found` directory

---

## /media
The `/media` directory contains the files representing the mounted drives. If we were to attach an external hard drive to our operating system, `/media` would be one of the options where the system could mount it. This is handled differently by each distribution, but has become the standard for mounts handled automatically by the system.

---

## /mnt
The `/mnt` directory stands for **mount**, and was the original mounting point for external devices. Nowadays, most distributions use `/media` instead.

---

## /opt
The `/opt` directory stands for **optional**, and contains installed software from external sources. We can also use this directory to host software we create. 

---

## /proc
The `/proc` directory stands for **processes**, and contains information about system processes. Every process executed will have a directory inside `/proc`, and will be assigned a unique `pid`, or process id.

##### Code
```Bash
dr-xr-xr-x  9 root       root                     0 Jan 27 22:19 1
dr-xr-xr-x  9 pabloagnck pabloagnck               0 Jan 27 22:19 10
dr-xr-xr-x  9 pabloagnck pabloagnck               0 Jan 27 22:41 13
dr-xr-xr-x  9 root       root                     0 Jan 27 22:41 4
dr-xr-xr-x  9 pabloagnck pabloagnck               0 Jan 28 00:22 552
dr-xr-xr-x  9 root       root                     0 Jan 27 22:41 8
dr-xr-xr-x  9 pabloagnck pabloagnck               0 Jan 27 22:19 88
dr-xr-xr-x  9 root       root                     0 Jan 27 22:41 9
dr-xr-xr-x  9 pabloagnck pabloagnck               0 Jan 27 22:41 90
...
```

We can identify a process by its `pid`, by using the `htop` utility we installed earlier:

##### **Code**
```Bash
htop
```

##### **Output**
![[figure_1_htop_PID.png]]

We can see that the system is currently running 10 processes. We can identify each process by it's respective PID by looking at the first column.

Processes 1 through 9 are being run by `root`, while the remaining ones are being run by our user. If we go back to `/proc` and look for process 88, we can see that there is a directory. We then `cd` into it and list its contents:

##### **Code**
```Bash
cd 88

ls -l
```

##### **Output**
```
total 0
-r--r--r--  1 pabloagnck pabloagnck 0 Jan 28 00:32 arch_status
dr-xr-xr-x  2 pabloagnck pabloagnck 0 Jan 28 00:32 attr
-r--------  1 pabloagnck pabloagnck 0 Jan 28 00:32 auxv
-r--r--r--  1 pabloagnck pabloagnck 0 Jan 28 00:32 cgroup
--w-------  1 pabloagnck pabloagnck 0 Jan 28 00:32 clear_refs
-r--r--r--  1 pabloagnck pabloagnck 0 Jan 27 22:41 cmdline
-rw-r--r--  1 pabloagnck pabloagnck 0 Jan 27 22:41 comm
-rw-r--r--  1 pabloagnck pabloagnck 0 Jan 28 00:32 coredump_filter
-r--r--r--  1 pabloagnck pabloagnck 0 Jan 28 00:32 cpuset
lrwxrwxrwx  1 pabloagnck pabloagnck 0 Jan 28 00:32 cwd -> /
-r--------  1 pabloagnck pabloagnck 0 Jan 28 00:32 environ
lrwxrwxrwx  1 pabloagnck pabloagnck 0 Jan 27 22:41 exe -> /usr/bin/zsh
```

We can see that there is a binary executable `/usr/bin/zsh` being run, which makes sense since we're using the `zsh` shell for this precise action.

---

## /root
The `/root` directory

---

## /run
The `/run` directory

---

## /sbin
The `/sbin` directory stands for **system binaries**, and contains executables that the system administrator would use. 

---

## /snap
The `/snap` directory

---

## /srv
The `/srv` directory

---

## /sys
The `/sys` directory

---

## /tmp
The `/tmp` directory

---

## /usr
The `/usr` directory

---

## /var
The `/var` directory

---

## Conclusions
We've reviewed multiple yet simple mechanisms we can employ to make our code cleaner, more elegant, modular, usable, scalable and safer. These measures can not only help us become better programmers but better collaborators. It will make reading code a pleasure instead of an agonizing process and instantly boost our credibility.

---

## References
- [Python Documentation, Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Documentation, Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Towards Data Science, What happens when you import a Python module?](https://towardsdatascience.com/what-happens-when-you-import-a-python-module-ad6c0efd2640)
- [Towards Data Science, 3 data structures for faster Python Lists](https://towardsdatascience.com/3-data-structures-for-faster-python-lists-f29a7e9c2f92)