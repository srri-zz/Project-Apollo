#By Steven Richards <sbrichards@{mit.edu, gnu.org, ieee.org}> and Sam Phippen <samphippen@googlemail.com>
#ASCII encoder to frequency tone
import audiere
from Crypto.Cipher import AES
import base64
import os
from time import sleep
from binascii import hexlify
#key_input = raw_input('Define a key: ')
key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
mode = AES.MODE_ECB
encryptor = AES.new(key, mode)
device = audiere.open_device()

openfile = raw_input("Enter path to file: ")
f = open(openfile)
file_data = f.read()
file_data += "\n" * (16-len(file_data) % 16)
enc_file = base64.b64encode(encryptor.encrypt(file_data))
#create a one herz tone
tone = device.create_tone(440)
tone.play()
for char in enc_file:
  print char
  tone.pitchshift = (ord(char) * 1.0/256)
  sleep(0.01)
  print char
f.close()
