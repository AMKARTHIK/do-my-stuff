#!/opt/helpers/.venv/bin/python

# env_file = '/opt/helpers/.venv/bin/activate_this.py'
# import sys
# exec(open(env_file).read(), dict(__file__=env_file))


import os
import pyperclip
import pyotp
import argparse
from datetime import datetime, timedelta

from dotenv import load_dotenv
load_dotenv(dotenv_path="/opt/helpers/.env")

secret = os.environ.get('SOD_LP_SEC')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",'--next', action="store_true", help="Next minute otp")

    args = parser.parse_args()

    if secret:
        totp = pyotp.TOTP(secret)
        now = datetime.now()
        if args.next:
            now = now + timedelta(minutes=1)
        print('OTP at: {}'.format(now))
        pyperclip.copy(int(totp.at(now)))
