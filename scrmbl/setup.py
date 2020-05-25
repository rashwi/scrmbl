#!/usr/bin/python3

# Initial setup to use scrmbl
# Creates all private files necessary for proper functionality

from os import path, mkdir, chmod
from constants import ScrmblConstants
import stat
from getpass import getpass
import random
from AESCipher import AESCipher
import string


def setup_scrmbl():
    if not path.isdir(ScrmblConstants.DIR):
        mkdir(ScrmblConstants.DIR)
        chmod(ScrmblConstants.DIR, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

    if not path.isfile(ScrmblConstants.KEY_FILE):
        setup_keyfile()

    print('Setup complete!')

def setup_keyfile():
    # Read passcode from user
    passcode = getpass(prompt='Enter Password : ')
    verification = getpass(prompt='Repeat Password: ')

    if not passcode == verification:
        raise ValueError('Passwords do not match! Try again!')

    # Construct random string
    hw = 'helloworld'
    testword = hw + ''.join(random.choice(string.printable) for i in range(ScrmblConstants.SENTENCE_LENGTH - len(hw)))

    # Encrypt random string using keyfile and passcode
    cipher = AESCipher(passcode)
    encrypted_testword = cipher.encrypt(testword)


    # Write string out back to test file
    with open(ScrmblConstants.KEY_FILE, 'wb') as key_file:
        key_file.write(encrypted_testword)
    
    chmod(ScrmblConstants.KEY_FILE, stat.S_IRUSR)

    print('Encrypted test word is of size {}'.format(len(encrypted_testword)))


if __name__ == '__main__':
    import pdb, traceback, sys
    try:
        setup_scrmbl()
    except:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)



