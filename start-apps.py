#!/usr/bin/env python

import os
import subprocess

apps_to_start = [
    # '/usr/bin/firefox -p normal',
    '/usr/bin/firefox -p dev-new -start-debugger-server',
    # '/usr/bin/firefox -p dev-new -ssb odoo.sodexis.com/web?debug=1 --window-size 1920,1080',
    '/opt/apps/thunderbird/thunderbird-bin',
    # 'export GOOGLE_API_KEY="AIzaSyCkfPOPZXDKNn8hhgu3JrA62wIgC93d44k" && '
    # 'export GOOGLE_DEFAULT_CLIENT_ID="811574891467.apps.googleusercontent.com" && '
    # 'export GOOGLE_DEFAULT_CLIENT_SECRET= "kdloedMFGdGla2P1zacGjAQh" && '
    # 'google-chrome-beta --app-id=knipolnnllmklapflnccelgolnpehhpl',
    '/opt/google/chrome/google-chrome "--profile-directory=Profile 1" --app-id=chfbpgnooceecdoohagngmjnndbbaeip',
    '/opt/google/chrome/google-chrome "--profile-directory=Profile 1" --app=https://odoo.sodexis.com/web',
    '/opt/google/chrome/google-chrome "--profile-directory=Profile 1" --app=https://discord.com/channels/@me',
    'tilix --maximize'
]

for app in apps_to_start:
    command_to_run = app + ' &>/dev/null'
    try:
        os.system(command_to_run)
    except Exception:
        subprocess.Popen(
            ['notify-send', "The command {0!r} failed to run".format(command_to_run)])
