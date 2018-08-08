Introduction to Linux
========================================================
author: Ouso D. O.
date: 09-08-2018
autosize: true

![The Penguin teacher!](Images/SenseiPenguin.png)

Objectives
========================================================
- Understand basic Linux terminologies
- Reasons to adopt linux
- Understand basic Linux filesystem
- Differentiate between relative and absolute paths
- Learn to make and commmon operations with directories
- Be able to explain the "ls" output
- Know how to manipulate files and file contents
- Basics of shell scripting

Basic Terminologies
========================================================

- **Kernel** - the core functionality of an operating system, translates commands from other
software directly to the hardware interfaces.

- **Distributions** - operating systems based on the Linux kernel, eg. Ubuntu (Deb), CentOS (Fedora) & openSUSE (SUSE)

- **CLI/Terminal** - a method of interaction with the computer based on text commands entered at the prompt

- **GUI** - a method of interaction with the computer that
makes use of visual representations of elements

Why Linux?
========================================================
- It is FLOSS-based
- World's largest and most prevanlent open source
- Long Term Support (LTS)
- Many developers around the world contribute to it
- Most secure
- Customizable 
- Multi-user, multi-tasking (servers)
- Major force in computing, eg. supercomps, phones, stock exchages etc

File System
========================================================
- Partition - a logical part of a disk
- Filesystem - a method of storing/finding files on a hard disk
Linux uses **'/'** to separate paths, windows uses **'\'**. A comparison between Win and Linux filesystems is illustrated in the image below

![Windows-Linux FS Comparison](Images/LinuxFS.png)

Linux
=====================================
_Below is the partial Linux FS representation_

![Linux File System](Images/LinuxVsWin.png)

- For more details see the Linux [Filesysytem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf)
- A new terminal will land you in the home directory
- While on the terminal you will be associated to one directory at a time called working dir/current dir

Paths
========================================================
- The command **_pwd_** (present working directory) returns the absolute path to your working dir

Two types of paths exist:
  - Absolute path - describe the path of a file/dir from the root (/) all the way to it
  - Relative path - describe the path to a file/dir from the current working dir

Let's illustrate the two paths with a fig
=================================================

![Dir Tree](Images/LinuxPath.png)

What is the absolute path to README.md? **_/home/oface/Git/Images/README.md_**
    
What is the path to LinuxFS.png assuming my current working directory is PythonCoding? **_./../Images/LinuxFS.png_**
  
Directories and Associated Commands
========================================================
- In Linux "__Directories__" are equivalent to Windows "__Folders__"

Some of the commands associated with directories include:
- To create a dir use **_mkdir_** <_dirName_>
- To remove a dir use **_rmdir_** <_dirNmae_>
- To move from one dir to another, use **_cd_** <_dirPath_>
- To list dir content, use **_ls_** whille inside the dir or **_ls_** <_dirPath_> from a different dir
- To rename a dir, use **_mv_** <_oldName_> <_newName_>

Output of the ls -lh Cmd
========================================================
![ls -lh output](Images/ls-lh.png)

 <ol type="I">
  <li>File(-) or Directory(d) or Symlink(l)</li>
  <li>Owner file permissions</li>
  <li>Group file oermissions</li>
  <li>Global user file permissions</li>
  <li>Number of links</li>
  <li>Owner name</li>
  <li>Owner group</li>
  <li>File size</li>
  <li>Date and time of last modification</li>
  <li>File/Directory name/li>
</ol> 

"__total BLOCKS__" means the total disk allocations of the dir content listed

Some shortcuts
========================================================
- **_cd ~_** or **_cd_**: takes you to home dir from wherever
- **_cd -_**: takes you to previous dir
- **_cd .._**: takes you to parent dir
- **_Ctrl+L_**: clears terminal
- **_Ctrl+C_**: cancels a running program
- **_Crtl+D_**: exit terminal
- **_Tab_**: auto complete
- **_Tab Tab_**: display possibities for autocomplete

Manipulating files
========================================================
- **_touch_**: to create, modify and change timestamp of a file; syntax **_touch_** <_fileName_>
- **_gedit_**: to create a text file; syntax **_gedit_** <_fileName_>
- **_wget_**: is a free utility for non-interactive download of files from the Web. It supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies; syntax **_wget_** <_option(s)_> <_URL_>
- **_cp_**: copy file/dir; syntax **_cp_** <_origiLocation_> <_finalLocation_>
- **_rm_**: delete files; syntax **_rm_** <_file_>
- **_mv_**: move file/dir; syntax **_mv_** <_origiLocation_> <_finalLocation_>

To figure out the many possible options of a command use **_man_** <_command_> to get a summary manual of how to use that command. Linux commands generally follow the syntax **_command_** <_option(s)_> <_argument(s)_>

Accessing file contents
========================================================
- **_cat_**: to view content of a small file in stdout; syntax **_cat_** <_file_>
- **_more_**: to view a large file in stdout by scrolling unilaterally - downwards; syntax **_more_** <_file_>. Use keyboard "__Spacebar__" to scroll page by page
- **_less_**: to view a large file in stdout by scrolling bilaterally - up/downwards; syntax **_more_** <_file_>. Use keyboard "__Spacebar__" to scroll page by page
- **_head_**: explore, by default, ten top lines of a file: syntax **_head_** <_file_>
- **_tail_**: explore, by default, ten last lines of a file: syntax **_tail_** <_file_>
- **_wc_**: word count, to explore number of lines, words and characters of a file: syntax **_wc_** <_file_>
 
Manipulating file contents
========================================================
- **_sort_**: re-order file content alphabeti/numeri-cally; syntax **_sort_** <_file_>
- **_uniq_**: remove redundancies; syntax **_uniq_** <_file_>
- **_join_**: compare content; syntax **_join_** <_file1_> <_file2_>. Output common entries
- **_diff_**: compare content; syntax **_diff_** <_file1_> <_file2_>. Output the differences
- **_grep_**: Global Regular Expression Pattern, search for patterns; syntax **_grep_** <_pattern_> <_file_>

__Wildcards__: special characters used as patterns to help with the quick targeting of files or file sections/dirs, see [document](https://bioinf.comav.upv.es/courses/linux/_downloads/fsf_cmd_manual.pdf) on wildcards starting from page 23

Shell scripting
========================================================
__What is a script?__
A short program written in of the programming languages used for automation, especially when halding huge amounts of data which require similar treatment. A shell script file basically contain a set of instructions in a shell language to be performed on files

__What is shebang?__
Begins a shell script, to set the interpreter environment to used to execute the set of instructions following, "_bash_" is such an interpreter, several others exist. Syntax **__#!AbsolutePathOfInterpreter__** eg. **__#!/bin/bash__** or **__#!/usr/bin/python__**

After writing your script you will need to make it executable by using the**_chmod_** command before you can run it


========================================================
Thank You

email: ousodaniel@gmail.com

twitter: @ousodanos
