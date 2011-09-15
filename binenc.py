#Author: 
#Steven Richards <sbrichards@{mit.edu, gnu.org}>
#Binary Based AES256 Point-to-Point Laser Encoding

import audiere
import base64
import binascii
import os
from Crypto.Cipher import AES
from time import sleep
from math import sqrt
#key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
#mode = AES.MODE_ECB #ECB AES
#encryptor = AES.new(key, mode)
device = audiere.open_device()#Open and assign the audio device

openfile = raw_input("Enter path to file: ")#File to encrypt
f = open(openfile)
file_data = f.read()#Read whole file into memory

#if len(key) == 16:
#  file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
#else:
#  file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32

#enc_file = base64.b64encode(file_data)#Encrypt
#print enc_file
enc_file = bin(int(binascii.hexlify(file_data), 16))
print enc_file
enc_file = str(enc_file[2:])
print enc_file

def new_frequency(char):
    sleep(0.058252427144)
    if char == '1':
        tone = device.create_tone(450.00)
        tone.play()
        print '450 = 1'
    if char == '0':
        tone = device.create_tone(350.00)
        tone.play()
        print '350 = 0'
    

for char in str(enc_file):
  new_frequency(char)
f.close()
