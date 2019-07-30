#!/usr/bin/python3.6
# Centos - Get the full DVD iso.  Custom select softwares - select GNU Desktop
# version while installing in VM.  

import subprocess
from logger import init_logger
import os

DB_SCRIPTS_PATH = '/home/puneet/mosip/mosip-platform/db_scripts/'

logger = None # Global

def command(cmd):
    r = subprocess.run(cmd, shell=True)
    if r.returncode != 0: 
        logger.error(r)
        
def give_home_read_permissions():
    logger.info('Giving read persmissons to home directory')
    command('chmod 755 %s' % os.environ['HOME']) 

def install_docker():
    logger.info('Install Docker')
    subprocess.call('sudo yum check-update', shell=True)
    subprocess.call('curl -fsSL https://get.docker.com/ | sh', shell=True)
    # TODO: Handle case of ^C to abort the above operation.

def install_epel():
    logger.info('Installing  EPEL')
    subprocess.call('sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm', shell=True)

def install_postgres():
    # Runs on port 5432
    logger.info('Installing postgres')
    command('sudo yum install postgresql-server postgresql-contrib')
    command('sudo postgresql-setup initdb; sudo systemctl start postgresql')

def configure_postgres():
    logger.info('Modify the pg_hba.conf file for "trust" access')
    command('sudo -u postgres mv /var/lib/pgsql/data/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf.bak')
    command('sudo -u postgres cp resources/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf')
    #command('sudo systemctl restart postgresql') 

def init_db():

    configure_postgres()
    pwd = os.getcwd()    
    os.chdir(DB_SCRIPTS_PATH)
    os.chdir('./mosip_kernel') 
    command('sudo -u postgres psql -f mosip_role_common.sql')
    command('sudo -u postgres psql -f mosip_role_kerneluser.sql')
    command('sudo -u postgres psql -f mosip_kernel_db.sql')
    

def main():
    global logger
    logger = init_logger('LAUNCHER', 'logs/launcher.log', 10000000, 'info', 2)

    give_home_read_permissions() # For various access
    #install_epel()
    #install_docker()
    #install_postgres()
    init_db()

if __name__== '__main__':
    main()
       
