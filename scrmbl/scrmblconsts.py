"""Constants definitions for scrmbl"""
import os.path
from dataclasses import dataclass

@dataclass
class ScrmblConstants():
    """Defined constants used within the module
    TODO: Change to read from config file"""
    # Storage area for all local data
    DIR: str = os.path.join(os.path.expanduser('~'), '.scrmbl')

    # File to store AES key in
    KEY_FILE: str = os.path.join(DIR, 'test')

    # Time to display decoded strings for (seconds)
    KEY_DISPLAY_TIME: int = 5

    # Timeout for password authentication (seconds)
    # Minutes * seconds
    TIMEOUT: int = 30 * 60

    # Length of each stored sentence
    SENTENCE_LENGTH: int = 64

    # key length in bytes
    KEY_LENGTH: int = 32

    # File extension for scrmbl
    EXT: str = '.scr'
