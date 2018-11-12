#!/usr/bin/env python

env_file = '/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/activate_this.py'
import sys

exec(open(env_file).read(), dict(__file__=env_file))


import os
import pyperclip
import pyotp
from dotenv import load_dotenv
load_dotenv()

secret = os.environ.get('SOD_LP_SEC')

if secret:
    totp = pyotp.TOTP(secret)
    pyperclip.copy(int(totp.now()))
