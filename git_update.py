#!/usr/bin/env python
from git import Repo
# repo list to clone or update
test = {
    'ping-me':'git@github.com:ULTIMATEUPGRADE/ping-me.git',
    'odoo---karthik':'git@github.com:ULTIMATEUPGRADE/odoo---karthik.git',
}

CLONE_LOCATION = '/home/karthik/Desktop/toodo/test/'
for key,value in test.iteritems():
    b = CLONE_LOCATION+'{0}'.format(key)
    print b
    Repo.clone_from(value,b)
