#!/usr/bin/python3.6
# Centos - Get the full DVD iso.  Custom select softwares - select GNU Desktop
# version while installing in VM.  

import subprocess
from logger import init_logger
import os

DB_SCRIPTS_PATH = '/home/puneet/mosip/mosip-platform/db_scripts/'

logger = None # Global

def command(cmd):
    err = subprocess.call(cmd, shell=True)
    if err: 
        logger.error(cmd)
        
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
    subprocess.call('sudo yum install postgresql-server postgresql-contrib', shell=True)
    subprocess.call('sudo postgresql-setup initdb; sudo systemctl start postgresql', shell=True)

def init_db_scripts():
    pwd = os.getcwd()    
    os.chdir(DB_SCRIPTS_PATH)
    os.chdir('./mosip_kernel') 
    subprocess.run('sudo -u postgres psql -f mosip_role_common.sql', shell=True)
    subprocess.run('sudo -u postgres psql -f mosip_role_kerneluser.sql', shell=True)
    subprocess.run('sudo -u postgres psql -f mosip_kernel_db.sql -U sysadmin -W', shell=True)
    

def main():
    global logger
    logger = init_logger('LAUNCHER', 'logs/launcher.log', 10000000, 'info', 2)

    give_home_read_permissions()
    #install_epel()
    #install_docker()
    #install_postgres()
    init_db_scripts() 

if __name__== '__main__':
    main()
