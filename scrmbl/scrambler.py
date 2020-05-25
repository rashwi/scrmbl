#!/usr/bin/python3
from argparse import ArgumentParser
import random
import string
import pdb
from getpass import getpass


ASCII_START = 33
ASCII_END = 127
MAX_OFFSET = 126 - ASCII_START
MAX_LEN = 64


def scramble(sourceString, salt, maxLength=MAX_LEN):
    validChars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    randomString = ''.join([random.choice(validChars) for x in range(0,maxLength)])
    sourceLen = len(sourceString)

    # Scramble sourceString
    OFFSET = salt % MAX_OFFSET
    ordSource = [ord(x) + OFFSET for x in sourceString]
    modSource = [x if x < ASCII_END else ASCII_START + x - ASCII_END for x in ordSource] 
    scrambledSource = ''.join(chr(x) for x in modSource)

    if len(sourceString) < maxLength:
        startingIdx = random.randint(0, maxLength - sourceLen)
        paddedScrambledSource = randomString[0:startingIdx] + scrambledSource + randomString[startingIdx + sourceLen:]
    else:
        paddedScrambledSource = scrambledSource

    return paddedScrambledSource


def unscramble(sourceString, salt):
    OFFSET = salt % MAX_OFFSET
    ordSource = [ord(x) - OFFSET for x in sourceString]
    modSource = [x if x > ASCII_START -1 else x - ASCII_START + ASCII_END for x in ordSource]

    unscrambledSource = ''.join(chr(x) for x in modSource)
    return unscrambledSource


if __name__ == '__main__':
    argstring = getpass(prompt='String : ')
    saltstring = getpass(prompt='Pin : ')
    if not all([x in string.digits for x in saltstring]):
        raise ValueError('Pin must be numeric! Try again')
    salt = int(saltstring)
    scrambled = scramble(argstring, salt)
    reverted = unscramble(scrambled, salt)
    print('{}\n{}'.format(scrambled, reverted))
