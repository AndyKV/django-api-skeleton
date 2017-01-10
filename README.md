# Django API skeleton

Implemented: restframework, uuid core model, basic userprofile api, celery tasks, settings environ format, swagger api docs,  deploy nginx config, system service config.

## INITIAL SETUP

### DEPENDENCIES
    sudo apt-get install -y python3-dev libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
    sudo apt-get install postgresql postgresql-client postgresql-contrib postgresql-server-dev-9.3
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install git
    sudo pip install virtualenv

### SETUP DATABASE

    sudo -u postgres psql
    postgres=# CREATE USER admin WITH PASSWORD '12345';
    postgres=# CREATE DATABASE api_db WITH OWNER = admin ENCODING = 'UTF8' ;


### SETUP DJANGO ENV
#### create virtual environment
    cd $PRJDIR
    virtualenv -p python3 .env 
(deactivate to leave virtual env)

#### install project requirements
    source .env/bin/activate
    pip3 install -r requirements.txt

#### configure settings
    
    add all settings options in .env file

    
#### migrate
    python3 manage.py migrate
    python3 manage.py migrate djcelery    
    

#### create admin user
    python3 manage.py createsuperuser


#### celery
    celery -A celery_app worker -B -l INFO
