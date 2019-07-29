#!/usr/bin/python3.6

import subprocess
from logger import init_logger

logger = None # Global


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
    logger = init_logger('LAUNCHER', 'logs/launcher.log', 10000000, 'info', 2)

    install_epel()
    install_docker()

if __name__== '__main__':
    main()
