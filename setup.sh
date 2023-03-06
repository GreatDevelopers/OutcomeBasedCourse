#!/bin/bash

# Install dependencies
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt install apache2 mysql-server python3 python3-pip python3-mysqldb libldap2-dev libmysqlclient-dev python3.11-dev
pip install --upgrade pip
sudo pip3 install virtualenv
virtualenv env
source env/bin/activate
sudo python3 -m pip install -r requirements.txt
