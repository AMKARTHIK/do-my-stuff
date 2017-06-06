#!/usr/bin/env python

import os
import subprocess
import shutil
from datetime import date, timedelta

# Variable used globally
user = os.environ["USER"]
BACKUP_FOLDER_PATH = '/home/harmony-12/Desktop/karthik' # CHANGE THIS TO AS PER YOUR BACKUP FOLDER PATH USE ABS PATH NOT RELATIVE PATH
MAKE_FOLDER_PATH = '/home/{0}/Desktop/'.format(user)

today = date.today()
today_folder = today.strftime("%d%m%Y")

# variable used for path
day_0 = '/home/{0}/Desktop/{1}'.format(user, today_folder)


# conditons checking whether the yesterday_folder exsist or not.
# variable used here
z = os.path.exists(day_0)

# path to create Today Folder
path = '{0}{1}'.format(MAKE_FOLDER_PATH, today_folder)

if not z:
    os.mkdir(path)
    today_message = 'Today Folder Created'
    subprocess.Popen(['notify-send', today_message])
    for i in range(1, 7):
        to_be_backuped = (today - timedelta(i))
        to_be_backuped_folder = to_be_backuped.strftime("%d%m%Y")
        to_be_backuped_path = '/home/{0}/Desktop/{1}'.format(user, to_be_backuped_folder)
        to_be_backuped_path_check = os.path.exists(to_be_backuped_path)
        if to_be_backuped_path_check:
            shutil.move(to_be_backuped_path, BACKUP_FOLDER_PATH)
            backup_message = '{0} folder backuped'.format(to_be_backuped_folder)
            subprocess.Popen(['notify-send', backup_message])

else:
    done_message = 'Already Done Backup'
    subprocess.Popen(['notify-send', done_message])
