#!/usr/bin/env python

import os
import subprocess

apps_to_start = [
        # 'firefox -p hangout-firefox',
        '/home/harmony/Desktop/Karthik/firefox/firefox -p hangout-firefox',
        '/home/harmony/Desktop/Karthik/firefox/firefox -p Odoo --new-tab=www.gaana.com',
        # 'hexchat',
        'thunderbird',
        'google-chrome --app-id=knipolnnllmklapflnccelgolnpehhpl',
        'tilix'
        ]

for app in apps_to_start:
    command_to_run = app + ' &>/dev/null'
    try:
        os.system(command_to_run)
    except Exception:
        subprocess.Popen(
            ['notify-send', "The command {0!r} failed to run".format(command_to_run)])
