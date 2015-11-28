#!/usr/bin/env python

import os
import subprocess
import shutil
from datetime import date, timedelta

# Variable used globally
user = os.environ["USER"]
BACKUP_FOLDER_PATH = '/home/karthik/Desktop/DESK/' # CHANGE THIS TO AS PER YOUR BACKUP FOLDER PATH USE ABS PATH NOT RELATIVE PATH
MAKE_FOLDER_PATH = '/home/{0}/Desktop/'.format(user)

today = date.today()
today_folder = today.strftime("%d%m%Y")

yesterday = (today - timedelta(1))
yesterday_folder = yesterday.strftime("%d%m%Y")

day_before_yesterday = (today - timedelta(2))
day_before_yesterday_folder = day_before_yesterday.strftime("%d%m%Y")

day_before_yesterdays_yesterday = (today - timedelta(3))
day_before_yesterdays_yesterday_folder = day_before_yesterdays_yesterday.strftime("%d%m%Y")

#variable used for path
day_1 = '/home/{0}/Desktop/{1}'.format(user, yesterday_folder)
day_2 = '/home/{0}/Desktop/{1}'.format(user, day_before_yesterday_folder)
day_3 = '/home/{0}/Desktop/{1}'.format(user, day_before_yesterdays_yesterday_folder)


#conditons checking whether the yesterday_folder exsist or not.
# variable used here
a = os.path.exists(day_1)
b = os.path.exists(day_2)
c = os.path.exists(day_3)

# path to create Today Folder
path = '{0}{1}'.format(MAKE_FOLDER_PATH, today_folder)

if a:
    shutil.move(day_1, BACKUP_FOLDER_PATH)
    try:
        os.mkdir(path)
    except Exception:
        raise "Today folder already created"

    print "True - yesterday"
elif b:
    shutil.move(day_2,BACKUP_FOLDER_PATH)
    try:
        os.mkdir(path)
    except Exception:
        raise "Today folder already created"

    print "True - day_before_yesterday"
elif c:
    shutil.move(day_3,BACKUP_FOLDER_PATH)
    try:
        os.mkdir(path)
    except Exception:
        raise "Today folder already created"

    print "True - day_before_yesterdays_yesterday"
else:
    print "No Folders to be backuped"
