#By Steven Richards
#ASCII encoder to frequency tone
import audiere
#import bz2
from Crypto.Cipher import AES
import base64
import os
#from itertools import izip, cycle
device = audiere.open_device()

BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
secret = os.urandom(BLOCK_SIZE)
cipher = AES.new(secret)

#def xor_crypt_string(data, key):
 #   return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
openfile = raw_input("Enter path to file: ")
f = open(openfile)
for line in f:
 #each_charline = [line]
 #enc_line = bz2.compress(line) #compression
 #each_charline = [enc_line] 
 #enc_line = xor_crypt_string(line, userkey) #XOR'd Encryption
 enc_line = EncodeAES(cipher, line)
 each_charline = [enc_line]
 for each_charline in enc_line:
  print((ord(each_charline)+1000), 'Hz')  #\-Debugging prints for  
  print(each_charline)       #/-Fatal error :(
  tone = device.create_tone(ord(each_charline) + 1000)
  tone.play()
 tone.stop()
 # print(bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in each_charline), 0))) #<-- Binary Only
f.close()
