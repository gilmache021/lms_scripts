#!/usr/bin/env python3

# SCRIPT WITH MORE INTERACTION TO MAKE THE LMS LESS TEDIOUS
# SCRIPT MAKES USE OF RELATED SCRIPTS
import os
from sys import argv
from time import sleep

from sqlalchemy import true

version = '0.5'
valid_commands = ['credits', 'help', 'version', 'help', 'exit', 'login', 'submit', 'review', 'details', 'grade', 'history']

if len(argv) == 2:
    if argv[1] == '-v' or argv[1] == '-V' or argv[1] == '--version':
        print(f'lmsbot version: {version}')
        exit()

    elif argv[1] == '-c' or argv[1] == '-C' or argv[1] == '--credits':
        print('fzondi021-JHB')
        exit()

    elif argv[1] == '-h' or argv[1] == '-H' or argv[1] == '--help':
        os.system('python3 help_commands.py')
        exit()


print(f'\nWTC-LMS BOT {version}\nHello friend.')


# GET USER COMMAND
def get_command():
    command = input('\nWhat do you wanna do? ').lower().strip()
    return execute_command(command)


def execute_command(command):
    global valid_commands
    while True:
        if command not in valid_commands:
            return get_command()

        elif command == 'exit':
            return True, print('Byzies...'), sleep(3)

        elif command == 'credits':
            print('fzondi021-JHB')
            get_command()

        elif command == 'help':
            os.system('python3 help_commands.py')
            get_command()

        elif command == 'version':
            print(f'lmsbot version: {version}')
            get_command()

        elif command == 'login':
            os.system('lms')
            get_command()

        elif command == 'start':
            os.system('start-project')
            get_command()

        elif command == 'submit':
            os.system('submit')
            get_command()

        elif command == 'review':
            os.system('review')
            get_command()

        elif command == 'details':
            os.system('details')
            get_command()

        elif command == 'grade':
            os.system('grade')
            get_command()

        elif command == 'history':
            os.system('project-history')
            get_command()




if __name__ == '__main__':
    get_command()