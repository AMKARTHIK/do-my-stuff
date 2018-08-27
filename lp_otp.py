#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python



import os
import pyperclip
import pyotp
from dotenv import load_dotenv
load_dotenv()

secret = os.environ.get('SOD_LP_SEC')

if secret:
    totp = pyotp.TOTP(secret)
    pyperclip.copy(int(totp.now()))
