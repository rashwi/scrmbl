#!/usr/bin/python3
""" Initial setup to use scrmbl
  Creates all private files necessary for proper functionality
"""
import stat
import random
import string
from os import path, mkdir, chmod
from getpass import getpass
from scrmbl import ScrmblConstants
from cryptlib import AESCipher

def setup_keyfile():
    """Create and setup the keyfile"""
    # Read passcode from user
    passcode = getpass(prompt='Enter Password : ')
    verification = getpass(prompt='Repeat Password: ')

    if not passcode == verification:
        raise ValueError('Passwords do not match! Try again!')

    # Construct random string
    testword = 'helloworld'
    word_length = ScrmblConstants.SENTENCE_LENGTH - len(testword)
    random_letters = (random.choice(string.printable) for i in range(word_length))
    testword += ''.join(random_letters)

    # Encrypt random string using keyfile and passcode
    cipher = AESCipher(passcode)
    encrypted_testword = cipher.encrypt(testword)


    # Write string out back to test file
    with open(ScrmblConstants.KEY_FILE, 'wb') as key_file:
        key_file.write(encrypted_testword)
    chmod(ScrmblConstants.KEY_FILE, stat.S_IRUSR)

    print('Encrypted test word is of size {}'.format(len(encrypted_testword)))


def setup_scrmbl():
    """Run initial setup if it hasn't already happened"""
    if not path.isdir(ScrmblConstants.DIR):
        mkdir(ScrmblConstants.DIR)
        chmod(ScrmblConstants.DIR, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

    if not path.isfile(ScrmblConstants.KEY_FILE):
        setup_keyfile()

    print('Setup complete!')

if __name__ == '__main__':
    setup_scrmbl()
