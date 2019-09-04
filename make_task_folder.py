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
# parser.add_argument('-c', '--communications', action='store_true')
parser.add_argument('-s', '--subissue', action='store_true')

# for testing
parser.add_argument('-t','--test', action='store_true')

args = parser.parse_args()

task_id = args.id
is_issue = args.issue
need_subissue = args.subissue

# if is_issue or need_subissue:
#     args.communications = True

# need_communication = args.communications

is_test = args.test


from dotenv import load_dotenv
load_dotenv()

# script, task_id = argv

server = os.environ.get('ODOO_SERVER')
db = os.environ.get('ODOO_DB')
user = os.environ.get('ODOO_USER')
pwd = os.environ.get('ODOO_PWD')
base_home = os.environ.get('PROJECT_BASE_HOME')
attachment_fields = ['datas_fname','res_model','store_fname','datas']

if is_test:
    base_home = os.path.join(base_home, '_test')

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
field_list = ['name','description','x_customer_description','project_id', 'message_ids']
if is_issue:
    model = 'helpdesk.ticket'
    field_list = ['name','description','project_id','message_ids']
if need_subissue:
    sub_model = 'helpdesk.ticket'
    sub_model_fields = ['name','description','project_id','message_ids']

details =  api.execute_kw(db, uid, pwd, model, 'read',[[task_id], field_list])

def create_communications(detail, task_location):
    today = datetime.today()
    communication_file_name = '{}.txt'.format(today.strftime('%Y_%m_%d'))
    communication_file = os.path.join(task_location, communication_file_name)
    with open(communication_file, "a") as my_file:
        os.system("notify-send 'Message updated in Task folder {0}'".format(task_location))
        msg_details = api.execute_kw(db, uid, pwd, 'mail.message', 'search_read', [[('author_id.id','not in',[2,3]),('id','in',detail['message_ids'])]],{'fields':['id','author_id','body'], 'order':'id'})
        for msg in msg_details:
            if msg['body']:
                text = re.sub('<.*?>', '\n', msg['body'])
                text = re.sub('\n+', '\n', text)
                my_file.write('\n{0}{1}\n'.format(msg['author_id'][-1], text.encode('UTF-8')))

def download_attachments(rec_id, model, task_location):
    attachment_details = api.execute_kw(db, uid, pwd, 'ir.attachment','search_read', [[['res_model','=',model],['res_id','=',rec_id]]], {'fields':attachment_fields})
    for attachment_detail in attachment_details:
        if not os.path.isfile(os.path.join(task_location, attachment_detail['datas_fname'])):
            with open(os.path.join(task_location, attachment_detail['datas_fname']), 'w') as f:
                f.write(base64.decodestring(attachment_detail['datas']))

def create_task_folders_files(detail, task_location, file_path, sub=False):

    if os.path.isdir(task_location) and os.path.isfile(file_path):
        os.system("notify-send 'Task folder and its specs files already created in {0}'".format(task_location))

    if not os.path.isdir(task_location):
        os.makedirs(task_location)
        description = detail.get('description', False)
        customer_description = detail.get('x_customer_description', False)
        with open(file_path, "a") as my_file:
            if description:
                my_file.write('Specs: \n{0}'.format(description))
            if customer_description:
                customer_description = customer_description.encode('UTF-8')
                my_file.write('\n\nCustomer Specs: \n{0}'.format(customer_description))
        os.system("notify-send 'Task folder created in {0}'".format(task_location))

    if not sub:
        download_attachments(task_id, model, task_location)
    if sub:
        download_attachments(task_id, sub_model, task_location)

    create_communications(detail, task_location)


for detail in details:
    project_name = clean_name(detail['project_id'][1])
    task_name = '_' + clean_name(detail['name'])
    project_location = os.path.join(base_home, project_name)
    if is_issue:
        project_location = os.path.join(project_location, 'Issues')
    task_location = os.path.join(project_location, task_name)
    file_name = 'info_{0}.txt'.format(detail['id'])
    file_path = os.path.join(task_location, file_name)


    # create task_folder_files
    create_task_folders_files(detail, task_location, file_path)


    # create sub issue folders and files:
    if need_subissue:
        sub_issue_details = api.execute_kw(db, uid, pwd, sub_model,'search_read', [[['task_id','=',task_id]]], {'fields':sub_model_fields})
        for sub_issue_detail in sub_issue_details:
            sub_issue_name = '_' + clean_name(sub_issue_detail['name'])
            sub_task_location = os.path.join(task_location, '_sub')
            sub_task_location = os.path.join(sub_task_location, sub_issue_name)
            subfile_name = 'info_{0}.txt'.format(sub_issue_detail['id'])
            sub_file_path = os.path.join(sub_task_location, subfile_name)
            create_task_folders_files(sub_issue_detail, sub_task_location, sub_file_path, sub=True)

    # copy the task location to clipboard for users purpose
    pyperclip.copy(str(task_location))

