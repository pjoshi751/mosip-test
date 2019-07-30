#!/usr/bin/python3.6
# Centos - Get the full DVD iso.  Custom select softwares - select GNU Desktop
# version while installing in VM.  

import subprocess
from logger import init_logger
from db import *
from config import *
from common import *
import os

logger = logging.getLogger() # Root Logger 

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

def main():
    global logger
    init_logger(logger, 'logs/launcher.log', 10000000, 'info', 2)

    give_home_read_permissions() # For various access
    #install_epel()
    #install_docker()
    #install_postgres()
    init_db()

if __name__== '__main__':
    main()
       
