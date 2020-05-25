#!/usr/bin/python3

from constants import ScrmblConstants
from argparse import ArgumentParser
from UserModule import UserModule
import sys
import os.path
import os.chmod
import stat

def main(options):
    file_path = getfilepath(options.file)
    user = UserModule.UserModule()
   
    if options.add:
        addfile(user, file_path)

 

def readfile(user, file_input):
    user = user.update()
    
    with open(file_path, 'rb') as bin_file:
        enc_bytes = bin_file.read()

    scr_str = user.cipher.decrypt(


def getfilepath(file_input):
    if os.path.isfile(file_input):
        return file_input
    else:
        return os.path.join(ScrmblConstants.DIR, file_input + ScrmblConstants.EXT)


def addfile(user, file_path):
    user = user.update()

`   dec_str = user.getinput('Input String: ')
    scr_str = scrambler.scramble(dec_str, user.pin)
    enc_bytes = user.cipher.encrypt(scr_str)

    with open(file_path,'wb') as bin_file:
        bin_file.write(enc_bytes)

    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

    print('Wrote to {}'.format(file_path))


    
    

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('file', help='File path to decrypt or encrypt to', action ='store')
    parser.add_argument('--add', help="Add entries to scrambled file", action='store_true')
    main(parser.parse_args())


