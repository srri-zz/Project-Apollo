#Authors: 
#Steven Richards <sbrichards@{mit.edu, gnu.org}>
#Sam Phippen <samphippen@googlemail.com>
#ASCII encoder to frequency tone
import audiere
from Crypto.Cipher import AES
import base64
import os
from time import sleep
from binascii import hexlify
key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
mode = AES.MODE_ECB #ECB AES
encryptor = AES.new(key, mode)
device = audiere.open_device()#Open and assign the audio device

openfile = raw_input("Enter path to file: ")#File to encrypt
f = open(openfile)
file_data = f.read()#Read whole file into memory
if len(key) == 16:
  file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
else:
  file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32
enc_file = base64.b64encode(encryptor.encrypt(file_data))#Encrypt
tone = device.create_tone(440)#Base Tone set to 440
tone.play()#Play!
for char in enc_file:
  tone.pitchshift = (ord(char) * 1.0/256)#Each loop, adjust pitch, still need to look into it
  sleep(0.01)
f.close()
