#!/usr/bin/python3
"""scrmbl.py : A simple scrambling utility for secrets storage
Safely stores secrets by scrambling the contents of the secret with a unique pin
  and then encrypting the resulting string using the a user password.

Run scrmbl.py --help for help"""
import stat
import time
import os.path
from getpass import getpass
from argparse import ArgumentParser

import scrambler
from usermodule import UserModule
from scrmblconsts import ScrmblConstants

def keyprint(sentence):
    """Safe method to print to terminal. Will clear output after a timeout period"""
    print(sentence, end="\r")
    time.sleep(ScrmblConstants.KEY_DISPLAY_TIME)

    print(" " * ScrmblConstants.SENTENCE_LENGTH)

def get_decrypted_string(user, enc_bytes):
    """Helper to get decrypted human readable string from an encrypted bytestring"""
    user = user.update()
    decr_bytes = user.cipher.decrypt(enc_bytes)
    return scrambler.unscramble(decr_bytes, user.pin)

def read_from_file(user, file_path):
    """Helper to decrypt secret from the encrypted secret storage file"""
    with open(file_path, 'rb') as bin_file:
        enc_bytes = bin_file.read()
    return get_decrypted_string(user, enc_bytes)


def getfilepath(file_input):
    """Helper to construct file path if user input filename instead"""
    filepath = file_input
    if not os.path.isfile(file_input):
        filepath = os.path.join(ScrmblConstants.DIR, file_input + ScrmblConstants.EXT)

    #TODO: Wrap in logger
    print(f"Working with {filepath}")
    return filepath

def get_encrypted_bytes(user, plaintext):
    """Helper to get encrypted bytestring from plaintext"""
    user = user.update()
    scr_str = scrambler.scramble(plaintext, user.pin)
    return user.cipher.encrypt(scr_str)

def add_to_file(user, file_path, plaintext):
    """Helper to add encrypted data to the secret storage file.

    Arguments:
        user: UserModule object representing encryptor
        file_path: Path to the secrets file
        plaintext: Plain text string to be encrypted
    """
    enc_bytes = get_encrypted_bytes(user, plaintext)
    with open(file_path, 'wb') as bin_file:
        bin_file.write(enc_bytes)

    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

    #TODO: Wrap in logger
    print('Wrote to {}'.format(file_path))

def test_file_integrity(file_path):
    """Helper function for debugging. Checks file integrity"""

    # Write a sample check
    test_str = 'integrity'

    encrypt_user = UserModule()
    print(f"Testing with string '{test_str}'")
    add_to_file(encrypt_user, file_path, test_str)

    # Try to decrypt
    decrypt_user = UserModule()
    decr_string = read_from_file(decrypt_user, file_path)

    print(f'Unscrambled Test String:\n')
    print(decr_string)

    # Check to see if the decrypted string contains the input string
    if test_str not in decr_string:
        print(f'ERROR! Unscrambled string does not match expected value!' +\
            'File integrity check failed!')

def main():
    """Main Driver for the scrmbl module. Handles user I/O"""
    parser = ArgumentParser()
    parser.add_argument('file', help='File path to decrypt or encrypt to', action='store')
    parser.add_argument('--add', help="Add entries to scrambled file", action='store_true')
    parser.add_argument('--test', help="Check for file integrity.", action='store_true')

    options = parser.parse_args()
    file_path = getfilepath(options.file)

    if options.test:
        test_file_integrity(file_path)
    elif options.add:
        user = UserModule()
        dec_str = getpass('Input String: ')
        add_to_file(user, file_path, dec_str)
    else:
        user = UserModule()
        # Read and display the contents of the file
        decr_string = read_from_file(user, file_path)
        print(f"Unscrambled [will disappear]:\n")
        keyprint(decr_string)

if __name__ == "__main__":
    main()
