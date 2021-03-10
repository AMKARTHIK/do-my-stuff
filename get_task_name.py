#!/opt/helpers/.venv/bin/python

import os
import xmlrpc.client as xmlrpclib
import argparse
import pyperclip

parser = argparse.ArgumentParser()
parser.add_argument('ids', type=str, help='Enter the task ID')

args = parser.parse_args()
task_ids = args.ids.split(',')
task_ids = [int(x) for x in task_ids]

from dotenv import load_dotenv
load_dotenv(dotenv_path="/opt/helpers/.env")


server = os.environ.get('ODOO_SERVER')
db = os.environ.get('ODOO_DB')
user = os.environ.get('ODOO_USER')
pwd = os.environ.get('ODOO_PWD')

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
uid = common.authenticate(db, user, pwd, {})
api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

model = 'project.task'
field_list = ['name']

details =  api.execute_kw(db, uid, pwd, model, 'read',[task_ids, field_list])

formatted_name = [] 
for detail in details:
    formatted_name.append("[ID: {0}] {1}".format(detail['id'], detail['name']))

final = "\n".join(formatted_name)
pyperclip.copy(final)
print(final)

