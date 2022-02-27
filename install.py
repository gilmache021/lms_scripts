#!/usr/bin/env python3
from time import sleep
import os


# PROMPT USER CREDS
def get_user_credentials():
    sudo_pass = input('Enter computer login password: ').strip()
    lms_pass = input('And your wtc-lms login password: ').strip()

    return validate(sudo_pass, lms_pass)


# VALIDATE CREDS
def validate(sudo_pass, lms_pass):
    if not sudo_pass or not lms_pass:
        print('Some details missing...')
        get_user_credentials()

    else:
        print(f'''
        SUDO PASSWORD: {sudo_pass}
        LMS PASSWORD : {lms_pass}\n
        ya sure these details are correct?
        ''')

        confirm = input('(y) or (n): ').lower().strip()
        while not confirm:
            confirm = input('(y) or (n): ').lower().strip()

        if confirm == 'y' or confirm == 'yes':
            print('alright then...')
            sleep(3)
            return run_installation(sudo_pass, lms_pass)
        
        else:
            print('get your sh*t together!')
            sleep(3)
            return get_user_credentials() 


# PASS CREDS TO INSTALL SCRIPT
def run_installation(sudo_pass, lms_pass):
    os.system(f'echo "{sudo_pass}" | sudo -S ./_package')
    os.system(f'sudo sudo sed -i "s/keycloak password here/{lms_pass}/" /usr/local/bin/lms')


if __name__ == '__main__':
    get_user_credentials()