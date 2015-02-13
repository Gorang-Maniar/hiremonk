dev-vm
======
## Platform Setup

## Software Installation

#### Minimum System Requirements:
* Mac OSX, Linux preferred
* At least 2GB of RAM

### 1) Virtualbox
* Download the installer here:  https://www.virtualbox.org/wiki/Downloads/  
* Use the **amd64** version.

### 2) Ruby
Vagrant requires Ruby. Use the following command to check if you have Ruby installed:

```ruby -v```

* If it returns an error, install Ruby
* The easiest way to install Ruby is via RVM https://rvm.io/rvm/install/

### 3) Vagrant
Install Vagrant. 

* Use version above **version 1.6.3** 
* Download the installer here: http://www.vagrantup.com/downloads.html

### 4) NFS
NFS is required to synchronize the files on the host computer's hard drive to the files on the virtual server's drive.

Use the following command to check if you have NFS installed.

```man nfsd```

If it reports nsfd not being installed on the system, use the following command to install it:

```sudo apt-get install nfs-kernel-server nfs-common```

### 5) GIT

Install GIT. You can download it here: http://git-scm.com/downloads

### 6) iTerm 2
We use iterm2 as our development terminal, because it allows us to split the window horizontally and vertically into multiple terminals. This is essential for productivity, because its not uncommon to have 7 or 8 terminals open.

* Download iterm2 here: http://iterm2.com/

### 8) Sublime Text 2
We use sublime text editor for our development. you can download it here at http://www.sublimetext.com/2
