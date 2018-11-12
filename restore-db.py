#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import os
import subprocess
import argparse
import psycopg2

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
    a = subprocess.check_output(command, shell=True)
    conn_str = "dbname={!r} user='lsuser' host='localhost' password='lsuser'".format(name)
    try:
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        cur.execute("update res_users set password={!r} where login='admin'".format('$pbkdf2-sha512$25000$DmGsVYpxrnUOAaBUak2pNQ$z.G9HCdTYsuUC66quhYfgbP6yIcHq7EfVZFRToOP6RzVha851B9t5a.CaP6jLABKRkYFrlcjFj.ISARujMn42g' if port == '12069' else 'admin'))
        conn.commit()
        cur.close()
    except:
        print "Connection errors"
    finally:
        if conn is not None:
            conn.close()
except Exception:
    print "db-restore-error"
