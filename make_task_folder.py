#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import os
from sys import argv
import re
import xmlrpclib
import argparse
import pyperclip
import pdb

parser = argparse.ArgumentParser()
parser.add_argument('id', type=int, help='Enter the task or issue id to create task folder')
parser.add_argument('-i', '--issue', action='store_true')
args = parser.parse_args()
task_id = args.id
is_issue = args.issue

from dotenv import load_dotenv
load_dotenv()

# script, task_id = argv

server = os.environ.get('ODOO_SERVER')
db = os.environ.get('ODOO_DB')
user = os.environ.get('ODOO_USER')
pwd = os.environ.get('ODOO_PWD')

BASE_HOME = '/home/harmony/Desktop/'

LOCATIONS = {
        51:'/home/harmony/Desktop/Extraction',
        56:'/home/harmony/Desktop/Extraction',
        6:'/home/harmony/Desktop/Sodexis',
        43:'/home/harmony/Desktop/Jodee',
        55:'/home/harmony/Desktop/Jodee',
        35:'/home/harmony/Desktop/Sohre',
        8:'/home/harmony/Desktop/SF',
        50:'/home/harmony/Desktop/Trinity',
        52:'/home/harmony/Desktop/Sublimation',
        21:'/home/harmony/Desktop/Trillium',
        41:'/home/harmony/Desktop/Conservation'
        }

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
uid = common.authenticate(db, user, pwd, {})


api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

model = 'project.task'
field_list = ['name','description','x_customer_description','project_id']
if is_issue:
    model = 'project.issue'
    field_list = ['name','description','project_id','message_ids']

detail =  api.execute_kw(db, uid, pwd, model, 'read',[[task_id], field_list])
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
# pdb.set_trace()

if detail:
    task_dict = detail[0]
    file_name = 'info_{0}.txt'.format(task_dict['id'])
    folder_name = ('{1}{0}'.format(task_dict['name'].encode('UTF-8'),'_')).lower().replace(' ','_')
    location = LOCATIONS.get(task_dict.get('project_id') and task_dict['project_id'][0], False)
    project_name = (task_dict.get('project_id') and
            task_dict['project_id'][1]).replace(' ','_').replace('/','_').encode('UTF-8').lower()
    if not location:
        location = os.path.join(BASE_HOME, project_name)
        if not os.path.isdir(location):
            os.makedirs(location)
    msg_details = False
    if is_issue:
        msg_details = api.execute_kw(db, uid, pwd, 'mail.message', 'search_read', [[('author_id.id','!=',3),('id','in',task_dict['message_ids'])]],{'fields':['id','author_id','body'], 'order':'id'})
        location = os.path.join(location, 'Issues')
        if not os.path.isdir(location):
            os.makedirs(location)

    dir_name = unicode(os.path.join(location,folder_name))
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    mkfile = unicode(os.path.join(dir_name, file_name))
    if os.path.isfile(mkfile):
        pyperclip.copy(str(dir_name))
        os.system("notify-send 'Task folder and its files already created in {0}'".format(dir_name))
    if not os.path.isfile(mkfile):
        with open(mkfile, "a") as my_file:
            description = task_dict.get('description')
            if description:
                description = description.encode('UTF-8')
                my_file.write('Specs: \n{0}'.format(description))
            customer_description = task_dict.get('x_customer_description')
            if customer_description:
                customer_description = customer_description.encode('UTF-8')
                my_file.write('\n\nCustomer Specs: \n{0}'.format(customer_description))
            if msg_details:
                my_file.write('\n\nCommunications:\n')
                for msg in msg_details:
                    if msg['body']:
                        text = re.sub('<.*?>', '\n', msg['body'])
                        text = re.sub('\n+', '\n', text)
                        my_file.write('\n{0}{1}\n'.format(msg['author_id'][-1], text.encode('UTF-8')))
        pyperclip.copy(str(dir_name))
        os.system("notify-send 'Task folder created in {0}'".format(dir_name))




