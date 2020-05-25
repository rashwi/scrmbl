import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import pdb


# AESCipher Object to handle all encryption functions
class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)

        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        #return base64.b64encode(iv + cipher.encrypt(raw.encode()))
        return iv + cipher.encrypt(raw.encode())

    def decrypt(self, enc):
        #enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        if len(s) % self.bs == 0:
            return s
        else:
            return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        if len(s) %  self.bs == 0:
            return s
        else:
            return s[:-ord(s[len(s)-1:])]

def b64encode(s):
    return base64.b64encode(s)

if __name__ == '__main__':
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

    
