#!/usr/bin/env python

import os
from sys import argv
import re
import xmlrpclib
from pprint import pprint as pp

from dotenv import load_dotenv

load_dotenv()

server = os.environ.get('ODOO_SERVER')
db = os.environ.get('ODOO_DB')
user = os.environ.get('ODOO_USER')
pwd = os.environ.get('ODOO_PWD')


script, sheet_id = argv
sheet_id = int(sheet_id)



common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
uid = common.authenticate(db, user, pwd, {})


api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

att_id =  api.execute_kw(db, uid, pwd, 'hr.attendance', 'search',[[['sheet_id','=',sheet_id]]])
print sorted(att_id)

# att_detail =  api.execute_kw(db, uid, pwd, 'hr.attendance', 'read', [37978])
# pp(att_detail)

# api.execute_kw(db, uid, pwd, 'hr.attendance', 'write', [[37978],{'check_in':'2018-10-22 08:58:28'}])

# att_detail =  api.execute_kw(db, uid, pwd, 'hr.attendance', 'read', [37978])
# pp(att_detail)
