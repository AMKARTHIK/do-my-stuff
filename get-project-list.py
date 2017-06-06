#!/usr/bin/env python

import xmlrpclib

server = 'http://localhost:10069'
db = 'sodexis-test'
user = 'admin'
pwd = 'admin'

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
print common.version()
uid = common.authenticate(db, user, pwd, {})

print uid


api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

#print api.execute_kw(db, uid, pwd, 'hr.attendance', 'read' ,[[att_id], ['name']])

#api.execute_kw(db, uid, pwd, 'hr.attendance', 'write' ,[[att_id], {'name':'2017-02-09 04:43:17'}])

#print api.execute_kw(db, uid, pwd, 'hr.attendance', 'read' ,[[att_id], ['name']])


