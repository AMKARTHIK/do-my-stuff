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
import base64

parser = argparse.ArgumentParser()
parser.add_argument('id', type=int, help='Enter the task or issue id to create task folder')
parser.add_argument('-i', '--issue', action='store_true')
parser.add_argument('-c', '--communications', action='store_true')
parser.add_argument('-u', '--update', action='store_true')
parser.add_argument('-a','--attachment', action='store_true')

args = parser.parse_args()
task_id = args.id
is_issue = args.issue
need_communication = args.communications
update = args.update
need_attachment = args.attachment

from dotenv import load_dotenv
load_dotenv()

# script, task_id = argv

server = os.environ.get('ODOO_SERVER')
db = os.environ.get('ODOO_DB')
user = os.environ.get('ODOO_USER')
pwd = os.environ.get('ODOO_PWD')
base_home = os.environ.get('PROJECT_BASE_HOME')

def clean_name(name):
    name = re.sub(r'/', ' or ', name)
    name = re.sub(r'&', ' and ', name)
    not_allowed_chars_pattern = r'[^a-zA-Z0-9.-_]'
    name = re.sub(not_allowed_chars_pattern, '_', name).lower()
    name = re.sub(r'_+', '_', name)
    return name

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
uid = common.authenticate(db, user, pwd, {})
api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

model = 'project.task'
field_list = ['name','description','x_customer_description','project_id']
if is_issue:
    model = 'helpdesk.ticket'
    field_list = ['name','description','project_id']
if need_communication or update:
    field_list += ['message_ids']

details =  api.execute_kw(db, uid, pwd, model, 'read',[[task_id], field_list])

if details:
    detail = details[0]
    description = detail.get('description', False)
    customer_description = detail.get('x_customer_description', False)
    project_name = clean_name(detail['project_id'][1])
    task_name = '_' + clean_name(detail['name'])
    project_location = os.path.join(base_home, project_name)
    if is_issue:
        project_location = os.path.join(project_location, 'Issues')
    task_location = os.path.join(project_location, task_name)
    file_name = 'info_{0}.txt'.format(detail['id'])
    file_path = os.path.join(task_location, file_name)

    if os.path.isdir(task_location) and os.path.isfile(file_path) and not update:
        pyperclip.copy(str(task_location))
        os.system("notify-send 'Task folder and its files already created in {0}'".format(task_location))
        os.chdir(str(task_location))
        os.system("/bin/bash")

    if not os.path.isdir(task_location):
        os.makedirs(task_location)
        pyperclip.copy(str(task_location))
        os.system("notify-send 'Task folder created in {0}'".format(task_location))
        with open(file_path, "a") as my_file:
            if description:
                my_file.write('Specs: \n{0}'.format(description))
            if customer_description:
                customer_description = customer_description.encode('UTF-8')
                my_file.write('\n\nCustomer Specs: \n{0}'.format(customer_description))
            if need_communication:
                msg_details = api.execute_kw(db, uid, pwd, 'mail.message', 'search_read', [[('author_id.id','not in',[2,3]),('id','in',detail['message_ids'])]],{'fields':['id','author_id','body'], 'order':'id'})
                if msg_details:
                    my_file.write('\n\nCommunications:\n')
                    for msg in msg_details:
                        if msg['body']:
                            text = re.sub('<.*?>', '\n', msg['body'])
                            text = re.sub('\n+', '\n', text)
                            my_file.write('\n{0}{1}\n'.format(msg['author_id'][-1], text.encode('UTF-8')))
        os.chdir(str(task_location))
        os.system("/bin/bash")

    if update:
        with open(file_path, "a") as my_file:
            pyperclip.copy(str(task_location))
            os.system("notify-send 'Message updated in Task folder {0}'".format(task_location))
            today = datetime.today().strftime('%Y-%m-%d')
            my_file.write('\nNew Messages on {}\n'.format(today))
            msg_details = api.execute_kw(db, uid, pwd, 'mail.message', 'search_read', [[('author_id.id','not in',[2,3]),('id','in',detail['message_ids'])]],{'fields':['id','author_id','body'], 'order':'id'})
            for msg in msg_details:
                if msg['body']:
                    text = re.sub('<.*?>', '\n', msg['body'])
                    text = re.sub('\n+', '\n', text)
                    my_file.write('\n{0}{1}\n'.format(msg['author_id'][-1], text.encode('UTF-8')))
        os.chdir(str(task_location))
        os.system("/bin/bash")

    if need_attachment:
        attachment_fields = ['datas_fname','res_model','store_fname','datas']
        attachment_details = api.execute_kw(db, uid, pwd, 'ir.attachment','search_read', [[['res_model','=',model],['res_id','=',task_id]]], {'fields':attachment_fields})
        for attachment_detail in attachment_details:
            if not os.path.isfile(os.path.join(task_location, attachment_detail['datas_fname'])):
                with open(os.path.join(task_location, attachment_detail['datas_fname']), 'w') as f:
                    f.write(base64.decodestring(attachment_detail['datas']))


