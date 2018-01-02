#!/usr/bin/env python

import os
from sys import argv
import re
import xmlrpclib
from datetime import datetime

server = 'http://282559-10-0-1bfcdc.runbot8.odoo.com:80'
db = '282559-10-0-1bfcdc-all'
user = 'admin'
pwd = 'admin'

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
uid = common.authenticate(db, user, pwd, {})
print uid


api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)
print api


for i in range(1,501):

    sale_detail =  api.execute_kw(db, uid, pwd, 'sale.order', 'create' ,[{
        'partner_id':12,
        'date_order':'11/30/2017 20:04:56',
        'pricelist_id':1,
        'warehouse_id':1,
        'picking_policy':'direct'
        }])
    print i, sale_detail
#print uid
#print task_detail

