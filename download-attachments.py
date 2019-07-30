#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import os
import sys
from sys import argv
import re
import xmlrpclib
import argparse
import pyperclip
import pdb
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('id', type=int, help='Enter the task or issue id to create task folder')
# parser.add_argument('-i', '--issue', action='store_true')
# parser.add_argument('-c', '--communications', action='store_true')
# parser.add_argument('-u', '--update', action='store_true')

args = parser.parse_args()
task_id = args.id
# is_issue = args.issue
# need_communication = args.communications
# update = args.update

from dotenv import load_dotenv
load_dotenv()

# script, task_id = argv

server = os.environ.get('ODOO_SERVER')
db = os.environ.get('ODOO_DB')
user = os.environ.get('ODOO_USER')
pwd = os.environ.get('ODOO_PWD')
# base_home = os.environ.get('PROJECT_BASE_HOME')


common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
uid = common.authenticate(db, user, pwd, {})
api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

field_list = ['datas_fname','res_model','store_fname','datas']

details = api.execute_kw(db, uid, pwd, 'ir.attachment','search_read', [[['res_model','=','project.task'],['res_id','=',task_id]]], {'fields':field_list})

print details[0]['datas']
