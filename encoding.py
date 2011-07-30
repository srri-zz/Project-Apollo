#By Steven Richards
#ASCII encoder to frequency tone
import audiere
device = audiere.open_device()
openfile = raw_input("Enter path to file: ")
f = open(openfile)
for line in f:
 each_charline = [line]
 for each_charline in line:
   tone = device.create_tone(ord(each_charline) + 500)
   tone.play()
f.close()
####print(bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in n), 0))) <-- Binary Only
                                  
