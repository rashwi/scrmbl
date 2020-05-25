#!/usr/bin/python3

# Initial setup to use scrmbl
# Creates all private files necessary for proper functionality

from os import path, mkdir
from constants import ScrmblConstants

def setup_scrmbl():
    if not path.isdir(ScrmblConstants.DIR):
        mkdir(ScrmblConstants.DIR)

    if not path.isfile(ScrmblConstants.KEYFILE):
        setup_keyfile()

    print('Setup complete!')

def setup_keyfile():
    # TBD will do later


if __name__ == '__main__':
    setup_scrmbl()



