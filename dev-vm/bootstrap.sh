#!/usr/bin/env bash

#Create new hiremonk directory (mkdir hiremonk)
#Change to hiremonk directory (chdir hiremonk)
#Clone dev-vm repository(git clone https://github.com/HireMonk/dev-vm.git)
#Clone chef-repo repository(git clone https://github.com/HireMonk/chef-repo.git)
#Clone webapp repository(git clone https://github.com/HireMonk/webapp.git)
#Clone scott repository(git clone https://github.com/HireMonk/scott.git)

#chdir dev-vm
#vagrant up (Your dev box will be setup)
#ssh vagrant@local.hiremonk to go to the dev virtual box
#If you are behind a proxy, you can configure a proxy for apt-get by putting a file 95proxy into /etc/apt/apt.conf.d that has the following contents:

#Acquire::http::proxy "<proxy_url>";
#Acquire::ftp::proxy "<proxy_url>";
#Acquire::https::proxy "<proxy_url>";
#try out export proxies in the box before

#gem install vagrant-proxyconf

#vagrant plugin install vagrant-proxyconf

#update vm box with new updates
sudo apt-get update

#install git
sudo apt-get install -y git


#BackEnd Architecture - Python, Django, PostgreSQL, Nginx, Gunicorn

# install Python package installer
sudo apt-get install -y python-pip

# install django
sudo pip install django

#install postgres python connector
sudo apt-get install -y libpq-dev python-dev

#install postgres database
sudo apt-get install -y postgresql postgresql-contrib

sudo pip install psycopg2

#install nginx web server
sudo apt-get install -y nginx

#install gunicorn python WSGI( Web server gateway interface) and may be install virtualenv in future for python version configurations
sudo apt-get install -y gunicorn


#FrontEnd Architecture - HTML, CSS, Javascript, JQuery, Angular and Twitter Bootstrap

# install python-software-properties and common for add-apt-repository dependency
sudo apt-get install -y python-software-properties software-properties-common

# apt-get had older node.js repostiory updated to work with node.js 1.4.3 latest version to work for bower
sudo add-apt-repository ppa:chris-lea/node.js

sudo apt-get update

apt-get install -y nodejs

sudo npm install -g bower gulp browserify

cd /dev/webapp 

npm install gulp bower gulp-browserify gulp-concat gulp-rimraf rimraf gulp-jshint gulp-uglify gulp-minify-css gulp-connect --save

