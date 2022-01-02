#!/usr/bin/env python3
"""This module provides ascii scrambing/descrambling methods for scrmbl"""
import random
import string
from getpass import getpass

ASCII_START = 33
ASCII_END = 127
MAX_OFFSET = 126 - ASCII_START
MAX_LEN = 64

def scramble(source_string, salt, max_length=MAX_LEN):
    """scrmable() : Method to scramble a given input string

    Arguments:
        source_string: Input string to scramble
        salt: value to salt the scrambling offset by

    Returns:
        Scrambled version of source_string with padding applied
        """
    valid_chars = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + string.punctuation
    random_string = ''.join([random.choice(valid_chars) for x in range(0, max_length)])
    source_len = len(source_string)

    # Scramble source_string
    offset = salt % MAX_OFFSET
    ord_source = [ord(x) + offset for x in source_string]
    mod_source = [x if x < ASCII_END else ASCII_START + x - ASCII_END for x in ord_source]
    scrambled_source = ''.join(chr(x) for x in mod_source)

    if len(source_string) < max_length:
        starting_idx = random.randint(0, max_length - source_len)
        padded_scrambled_source = random_string[0:starting_idx] + \
            scrambled_source + random_string[starting_idx + source_len:]
    else:
        padded_scrambled_source = scrambled_source

    return padded_scrambled_source

def unscramble(scrambled_source, salt):
    """Unscrambles strings based on salt

    Arguments:
        scrambled_source: scrambled string
        salt: Password based salt to unscramble the string with
    Returns:
        unscrambled string
    """
    offset = salt % MAX_OFFSET
    ord_source = [ord(x) - offset for x in scrambled_source]
    mod_source = [x if x > ASCII_START -1 else x - ASCII_START + ASCII_END for x in ord_source]

    unscrambled_result = ''.join(chr(x) for x in mod_source)
    return unscrambled_result

def main():
    """main() function provided for test purposes only"""
    argstring = getpass(prompt='String : ')
    saltstring = getpass(prompt='Pin : ')
    if not all([x in string.digits for x in saltstring]):
        raise ValueError('Pin must be numeric! Try again')
    salt = int(saltstring)
    scrambled = scramble(argstring, salt)
    reverted = unscramble(scrambled, salt)
    print('{}\n{}'.format(scrambled, reverted))

if __name__ == '__main__':
    main()
