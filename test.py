import sys
import base64
import os
from Crypto.Cipher import AES

key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
mode = AES.MODE_ECB #ECB AES
encryptor = AES.new(key, mode)

openfile = raw_input("Enter path to file: ")#File to encrypt
f = open(openfile)
file_data = f.read()#Read whole file into memory
if len(key) == 16:
  file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
else:
  file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32
enc_file = base64.b64encode(encryptor.encrypt(file_data))

#outputstring_enc += (chr(int(thefreq)))
brokenstring = ''
for char in enc_file:
    brokenstring += str(ord(char)) + ','
print brokenstring
decrypted_string = (encryptor.decrypt(base64.b64decode(brokenstring)))
#print decrypted_string
