from constants import ScrmblConstants
from getpass import getpass
from AESCipher import AESCipher
import sys
import time


class UserModule
    def __init__(self):
        self._t0 = time.clock()
        self.cipher = _verifyID()
        self.pin = _getPIN()

    def update(self):
        if time.clock() - self.t0 < ScrmblConstants.TIMEOUT:
            self._cipher = _verifyID()
            self._pin = _getPIN()

        return self

    def getinput(input_prompt)
        return getpass(prompt=input_prompt)
        
        
        
    
    @staticmethod    
    def _verifyID():
        
        # Test decryption of test file and see if it works
        with open(ScrmblConstants.KEY_FILE, 'rb') as key_file:
            enc_test_string = key_file.read()

        passcode = getpass(prompt='Enter Password :')
        cipher = AESCipher(passcode)

        try:
            dec_test_string = cipher.decrypt(enc_test_string)
        except UnicodeDecodeError:
            print('Could not verify password. Exiting')
            sys.exit(1)

        return cipher

    def _getPIN():
        pin_string = getpass(prompt='Pin : ')
        if not all ([x in string.digits for x in pin_string]):
            raise ValueError('Pin must be numeric! Try again')

        return int(pin)

