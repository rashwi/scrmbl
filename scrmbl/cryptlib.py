#!/usr/bin/env python3
"""This module provides the encryption/decryption functionality necessary for scrmbl"""
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# AESCipher Object to handle all encryption functions
class AESCipher:
    """AESCiper Object for convenient data transfer"""

    def __init__(self, key):
        """Initialization for AESCipher. Requires a keyword to use for encryption/decryption"""
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, cleartext):
        """encrypt(...) : AES256 encryption method.
        Usage:
            cipher = AESCipher(key_to_use)
            encrypted_bytes = cipher.encrypt(cleartext)

        Arguments:
            cleartext: Text to encrypt in clear text

        Returns:
            Bytes of encrypted data
        """
        raw = self._pad(cleartext)

        initial_value = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, initial_value)
        return initial_value + cipher.encrypt(raw.encode())

    def decrypt(self, ciphertext):
        """decrypt(...) : AES256 decryption method
        Usage:
            cipher = AESCipher(key_to_use)
            decrypted_bytes = cipher.decrypt(ciphertext)

        Arguments:
            ciphertext: Encrypted bytes

        Returns:
            Decrypted Text corresponding to the ciphertext"""
        initial_value = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, initial_value)
        return self._unpad(cipher.decrypt(ciphertext[AES.block_size:])).decode('utf-8')

    def _pad(self, inp_str):
        """Private function to pad all text to AES256 block size"""
        if len(inp_str) % self.block_size == 0:
            return inp_str
        return inp_str + (self.block_size - len(inp_str) % self.block_size) * \
            chr(self.block_size - len(inp_str) % self.block_size)

    def _unpad(self, inp_str):
        """Private function to unpad from the AES256 blocksize"""
        if len(inp_str) %  self.block_size == 0:
            return inp_str
        return inp_str[:-ord(inp_str[len(inp_str)-1:])]

def b64encode(inp_str):
    """Encodes input string to base64"""
    return base64.b64encode(inp_str)

def main():
    """Main function is defined for testing purposes only. """
    sample_key = '1234'
    sample_string = 'This is a string'

    ciph = AESCipher(sample_key)
    encrypted = ciph.encrypt(sample_string)
    with open('ciphertext.tmp', 'wb') as outfile:
        outfile.write(encrypted)

    # Read it back
    with open('ciphertext.tmp', 'rb') as infile:
        loaded = infile.read()

    print('Original : {}'.format(sample_string))
    print('Encrypted : {}'.format(b64encode(encrypted)))
    print('Loaded : {}'.format(b64encode(loaded)))
    print('Decrypted : {}'.format(ciph.decrypt(loaded)))

if __name__ == '__main__':
    main()
