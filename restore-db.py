#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import os
import re
import subprocess
import argparse
import psycopg2
import pdb
import requests as req
from requests.exceptions import ConnectionError
from user_agent import generate_user_agent

PORT_MAP = {'8':8069, '9': 9069, '10':10069, '11':11069, '12': 12069}

pattern = r'(?P<db_name>(?P<customer>[A-Za-z0-9]+)_[a-zA-Z0-9]+_[v|V]+(?P<version>[0-9]+)_\d+_\d+_\d+)'

parser = argparse.ArgumentParser()
parser.add_argument("dump", help="Db name")
parser.add_argument("-c",'--custom', action="store_true", help="Customer DB name if needed.")

args = parser.parse_args()

dump = os.path.abspath(args.dump)
match = re.search(pattern, os.path.basename(dump))
if match:
    values = match.groupdict()
    if 'db_name' in values and args.custom:
        name = raw_input("\nEnter the Custom Database name: ")
    if 'db_name' in values and not args.custom:
        name = values['db_name']
    if 'version' in values:
        ver = values['version']
        port = PORT_MAP[values['version']]
else:
    name = raw_input("\nEnter the Database name to restore: ")
    port = int(raw_input("\n Enter the running server port to restore: "))

files = {'backup_file':open(dump, 'rb')}
headers = {'User-Agent': generate_user_agent(navigator='firefox', os='linux')}

def update_password(level=None):
    print "Setting password at level {0}".format(level)
    try:
        conn_str = "dbname={!r} user='lsuser' host='localhost' password='lsuser'".format(name)
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        if int(ver) == 12:
            cur.execute("update res_users set password='admin', login='admin' where id=2")
        if int(ver) != 12:
            cur.execute("update res_users set login='admin', password='admin' where id=1")
        # cur.execute("update res_users set password='admin' where login='admin'")
        cur.execute("delete from ir_config_parameter where key='report.url'")
        cur.execute("delete from fetchmail_server")
        cur.execute("delete from ir_mail_server")
        conn.commit()
        cur.close()
        conn.close()
    except:
        print "Database Connection errors"

try:
    r = req.post('http://localhost:{0}/web/database/restore'.format(port),headers=headers, files=files, data={'master_pwd':'karthik', 'copy':'true', 'name':'{0}'.format(name)})
    update_password(level='1')
except ConnectionError as ce:
    update_password(level='2')
except Exception as e:
    if not isinstance(e, ConnectionError):
        raise e
