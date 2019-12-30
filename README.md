Outcome Based Course Design
==========

Design and develop your own outcome-based courses

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Requirements
------------

```
1. Apache2
1. mysql-server
1. python3.7
1. python3-pip
1. python-mysqldb
1. django 3.0
1. libldap2-dev
1. libmysqlclient-dev
```

#### Installation

Use the following command to install and setup OutcomeBasedCourse.

```bash
git clone https://github.com/GreatDevelopers/OutcomeBasedCourse
cd OutcomeBasedCourse
chmod +x setup.sh
./setup.sh
```

#### OR

Installation of Requirements

```bash
sudo apt install apache2 mysql-server python python3-pip python-mysqldb libldap2-dev libmysqlclient-dev
sudo python3 -m pip install -r requirements.txt
```

Steps for installation of OutcomeBasedCourse
1. Clone the repository [OutcomeBasedCourse](https://github.com/GreatDevelopers/OutcomeBasedCourse)
```bash
git clone https://github.com/GreatDevelopers/OutcomeBasedCourse
```
1. Create a database for OutcomeBasedCourse
```bash
mysql -u root -p -e "create database outcomebasedcourse;"
```
1. Edit settings.py file in OutcomeBasedCourse/ directory. Things to be edited are:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "Your database name"
        "HOST": "Your MySQl server host",
        "PORT": "Your MySQl server port",
        "USER": "Your MySQL username",
        "PASSWORD": "Your MySQl password",
    }
}
1. Goto the project directory and run the following commands:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 127.0.0.1:8090
```
1. Open "http://127.0.0.1:8090" in your browser.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
