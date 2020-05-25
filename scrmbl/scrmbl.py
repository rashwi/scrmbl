#!/usr/bin/python3

from constants import ScrmblConstants
from argparse import ArgumentParser

def main(options):
    print('Running main!')


def scramble(text):
    # Given a string, scramble and hash


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--add', help="Add entries to scrambled file", action='store_true')
    parser.add_argument('--unscramble', help='Unscramble entries in a scramble file')
    main(parser.parse_args())

