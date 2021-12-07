
def save_pass():
    password = input('Enter password: ')
    if '$' in password:
        print(password)
        new_pass = password.replace('$', '\-')
        print(new_pass)
    else:
        print('password saved...')

if __name__ == '__main__':
    save_pass()