#By Steven Richards
#ASCII encoder to frequency tone
import audiere
import bz2
from itertools import izip, cycle
device = audiere.open_device()

def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
openfile = raw_input("Enter path to file: ")
f = open(openfile)
userkey = raw_input("Enter a random key: ")
for line in f:
 #each_charline = [line]
 #enc_line = bz2.compress(line) #compression
 #each_charline = [enc_line] 
 enc_line = xor_crypt_string(line, userkey) #XOR'd OTP Encryption
 each_charline = [enc_line]
 for each_charline in enc_line:
  print(ord(each_charline))  #\-Debugging prints for  
  print(each_charline)       #/-Fatal error :(
  tone = device.create_tone(ord(each_charline) + 1000)
  tone.play()
 tone.stop()
 # print(bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in each_charline), 0))) #<-- Binary Only
f.close()
