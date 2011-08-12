#By Steven Richards
#ASCII encoder to frequency tone
import audiere
import bz2
device = audiere.open_device()
openfile = raw_input("Enter path to file: ")
f = open(openfile)
for line in f:
 #each_charline = [line]
 enc_line = bz2.compress(line)
 each_charline = [enc_line] #compression
 for each_charline in enc_line:
  print(ord(each_charline))  #\-Debugging prints for  
  print(each_charline)       #/-Fatal error :(
  tone = device.create_tone(ord(each_charline) + 1000)
  tone.play()
 tone.stop()
 # print(bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in each_charline), 0))) #<-- Binary Only
f.close()
