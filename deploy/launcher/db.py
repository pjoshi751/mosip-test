import subprocess
import os
import logging
from common import *
from config import *

logger = logging.getLogger(__name__)

def install_postgres():
    logger.info('Installing postgres')
    command('sudo yum install postgresql-server postgresql-contrib')
    command('sudo postgresql-setup initdb; sudo systemctl start postgresql')

def configure_postgres():
    logger.info('Modify the pg_hba.conf file for "trust" access')
    command('sudo -u postgres mv /var/lib/pgsql/data/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf.bak')
    command('sudo -u postgres cp resources/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf')
    command('sudo systemctl restart postgresql') 

def init_db():

    configure_postgres()
    pwd = os.getcwd()    
    os.chdir(DB_SCRIPTS_PATH)
    os.chdir('./mosip_kernel') 
    command('sudo -u postgres psql -f mosip_role_common.sql')
    command('sudo -u postgres psql -f mosip_role_kerneluser.sql')
    command('sudo -u postgres psql -f mosip_kernel_db.sql')
    
