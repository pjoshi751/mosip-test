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
    command('sudo yum check-update')
    command('curl -fsSL https://get.docker.com/ | sh')
        
def install_epel():
    logger.info('Installing  EPEL')
    command('sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')

def install_clamav():
    logger.info('Installing CLAMAV')
    command('sudo yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd')
    if not os.path.exists('/etc/clamd.d/scan.conf.original'): 
        command('sudo cp /etc/clamd.d/scan.conf /etc/clamd.d/scan.conf.original') 
    command('sudo sed -i -e "s/^Example/#Example/" /etc/clamd.d/scan.conf')
    command('echo "LocalSocket /var/run/clamd.scan/clamd.sock" | sudo tee -a /etc/clamd.d/scan.conf')
    command('sudo sed -i -e "s/^Example/#Example/" /etc/freshclam.conf')
    command('sudo freshclam')
    command('sudo systemctl start clamd@scan') 
    command('sudo systemctl enable clamd@scan') 
  
def main():
    global logger
    init_logger(logger, 'logs/launcher.log', 10000000, 'info', 2)

    give_home_read_permissions() # For various access
    #install_epel()
    #install_docker()
    #install_postgres()
    #init_db()
    install_clamav()
    logger.info('Install done')

if __name__== '__main__':
    main()
       
