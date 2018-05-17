#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("port", help="Enter port of the running server.")
parser.add_argument("dump", help="Enter port of the running server.")
parser.add_argument("name", help="Enter port of the running server.")
args = parser.parse_args()
port = args.port
dump = os.path.abspath(args.dump)
name = args.name

command = """curl -F 'master_pwd=karthik' -F 'backup_file=@{dump}' -F 'copy=true' -F 'name={name}' http://localhost:{port}/web/database/restore""".format(port=port,dump=dump,name=name)

try:
    os.system(command)
except Exception:
    print "db-restore-error"
