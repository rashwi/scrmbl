# Module to store all constants
import os.path

class ScrmblConstants():
    # Storage area for all local data
    DIR = os.path.join(os.path.expanduser('~'),'.scrmbl')

    # File to store AES key in
    KEY_FILE = os.path.join(DIR,'test')

    # Time to display decoded strings for (seconds)
    KEY_DISPLAY_TIME = 5

    # Length of each stored sentence
    SENTENCE_LENGTH = 64

    # key length in bytes
    KEY_LENGTH = 32

    # File extension for scrmbl
    EXT = '.scr'
