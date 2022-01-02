"""Module representing user actions for scrmbl.
Used to conveniently handle authentication for crypto operations"""
import string
import sys
from datetime import datetime
from getpass import getpass
from cryptlib import AESCipher
from scrmblconsts import ScrmblConstants

class UserModule:
    """Module representing user. Used to handle authentication"""
    def __init__(self):
        self.t0: datetime = datetime.now()
        self.cipher: AESCipher = UserModule.verify_id()
        self.pin: int = UserModule.get_pin()


    @staticmethod
    def verify_id() -> AESCipher:
        """Method to re-authenticate user.
        Verifies the password by attempting to unencrypt a canary file

        Arguments: None

        Returns:
            AESCipher object, if the correct password is given by the user"""

        # Test decryption of test file and see if it works
        with open(ScrmblConstants.KEY_FILE, 'rb') as key_file:
            enc_test_string = key_file.read()

        passcode = getpass(prompt='Enter Password :')
        cipher = AESCipher(passcode)

        try:
            _ = cipher.decrypt(enc_test_string)
        except UnicodeDecodeError:
            print('Could not verify password. Exiting')
            sys.exit(1)

        return cipher

    @staticmethod
    def get_pin() -> int:
        """Get a pin from the user. The pin is used later to salt the scrambling function"""
        pin_string = getpass(prompt='Pin : ')
        if not all([x in string.digits for x in pin_string]):
            raise ValueError('Pin must be numeric! Try again')

        return int(pin_string)

    def update(self):
        """Method to check if reauthentication with the user is necessary.
        Will ask the user for the password again if the time elapsed since last
        password check is greater than 'TIMEOUT'"""
        if (datetime.now() - self.t0).total_seconds() > ScrmblConstants.TIMEOUT:
            self.t0 = datetime.now()
            self.cipher = self.verify_id()
            self.pin = self.get_pin()

        return self
