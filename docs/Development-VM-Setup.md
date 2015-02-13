## Dev VM Setup

We will create a new development virtual machine so that everyone is having the same configuration, Vagrant helps us to setup the development environment very easily. Hiremonk currently has these repositories:

* webapp (Frontend applications will be in this repostiory - Angular.js, Javascript, HTML, CSS)
* scott (Backend applications will be in this repository - Django, Postgres)
* dev-vm (All development setup scripts and vagrant files)
* chef-repo (In future, all chef repos will be in this repository)
* docs (All documentation will be in this repository)


### 1) Create Hiremonk project directory
* ```mkdir ~/hiremonk```
* ```cd hiremonk```

### 2) Clone hiremonk repositories

* ```git clone https://github.com/HireMonk/webapp.git```
* ```git clone https://github.com/HireMonk/scott.git```
* ```git clone https://github.com/HireMonk/dev-vm.git```
* ```git clone https://github.com/HireMonk/chef-repo.git```
* ```git clone https://github.com/HireMonk/docs.git```
* 

### 3) Install gem and other git ssh etc for vagrant proxy issues

* ```cd dev-vm```
* export http_proxy and https_proxy in case if you are using from IIIT Hyderabad in .bashrc
* ```gem install vagrant-proxyconf```
* Add the below line to the end of ```/etc/hosts``` file 
* ```192.168.10.10 local.hiremonk www.local.hiremonk static.local.hiremonk```
* Add ssh keys to GIT based on https://help.github.com/articles/generating-ssh-keys

### 4) Vagrant up
* This step will take some time as new virtual box will be downloaded for the first time and required softwares such as python, pip, django, postgresql, nginx, gunicorn will be setup 


### 5) Connect to dev box
* ```ssh vagrant@local.hiremonk```
* username - vagrant
* host - local.hiremonk
* password - vagrant

### 6) In case there was any problem with vagrant up due to ssh issues
* ```scp ~/.ssh/id_rsa.pub vagrant@local.hiremonk:~/```
* ```ssh vagrant@local.hiremonk```
* ```mv id_rsa.pub ~/.ssh/authorized_keys```

### 7) Vagrant provision now, if there was any problem with vagrant up
* ```vagrant provision```
