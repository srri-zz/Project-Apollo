#Author Steven Richards <sbrichards@mit.edu>
#Faster Fascii Decoding over Laser/Audio

import pyaudio
import wave
import sys
import numpy as np
import base64
import binascii
import os
from math import sqrt
#from Crypto.Cipher import AES
from time import sleep

chunk = 1024
FORMAT = pyaudio.paInt16
HOST = pyaudio.paOSS
CHANNELS = 1
RATE = 44100
print "\nAvg. Message (120 characters) takes 1 minute\n"
RECORD_SECONDS = raw_input("How Many Seconds would you like to record?: ")
#key = raw_input("Enter expected key with a length of 16, or 32 Characters: ")
#mode = AES.MODE_CBC
#encryptor = AES.new(key, mode)
raw_input("Press any key to start recording")
WAVE_OUTPUT_FILENAME = "read.wav"

asciiRange = range(0,255)
asciiDict = {}
for num in asciiRange:
 asciiDict = {chr(num), num}

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

print "* recording"
all = []
for i in range(0, RATE / chunk * int(RECORD_SECONDS)):
    data = stream.read(chunk)
    all.append(data)
print "* done recording"

stream.close()
p.terminate()

# write data to WAVE file
data = ''.join(all)
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(data)
wf.close()

# open up a wave
wf = wave.open('read.wav', 'rb') #edit the path to load up a sample wave file like sample.wav
swidth = wf.getsampwidth()
RATE = wf.getframerate()
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)

# read some data
data = wf.readframes(chunk)
# play stream and find the frequency of each chunk
outputstring = ''
found = 'false'
start = 1
lasttone = 0
while len(data) == chunk*swidth:
    # write data out to the audio stream
    stream.write(data)
    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))*window
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        if int(round(thefreq, -2)) > 2000:
          found = 'true'
          if start == 1:
              start = 0
              currentmode = 2
              juststarted = 1
          
        if found == 'true' and (int(round(thefreq, -2)) != (lasttone) or juststarted == 1) and (int(round(thefreq, -2))) > 2000:
                print ('in found loop currentmode =',currentmode)
                if currentmode % 2 == 0:
					tempvar = ((int(round(thefreq, -2)) - 2100)/100)
					outputstring += chr(tempvar)
					print (chr(tempvar))
					lasttone = int(round(thefreq, -2))
					print 'in even'
					print currentmode
					currentmode += 1
					print currentmode
                else:
					tempvar = ((int(round(thefreq, -2)) - 1900)/100)
					outputstring += chr(tempvar)
					print (chr(tempvar))
					lasttone = int(round(thefreq, -2))
					print 'in odd'
					print currentmode
					currentmode += 1
					print currentmode
                juststarted = 0
    # read some more data
    data = wf.readframes(chunk)
if data:
    stream.write(data)
stream.close()
p.terminate()

#decrypted_string = base64.b64decode(outputstring_enc)
print ""
print "Message Data: " + outputstring
print ""
##if str(outputstring_enc.find('DATA:MESSAGE')) == '0':
##	outputstring_enc = outputstring_enc.replace('DATA:MESSAGE','')
##	print outputstring_enc
##if str(outputstring_enc.find('DATA:FILE')) == '0':
##	name = raw_input("What would you like to name the file?: ")
##	fileobjl = open(name + ".laze", "w")
##	filetype = outputstring_enc[outputstring_enc.find('EXT:'):4]
##	fileobj = open(name + filetype, "w")
##	fileobjl.write(outputstring_enc)
##	outputstring_enc = outputstring_enc.replace('DATA:FILE', '')
##	outputstring_enc = outputstring_enc.replace('EXT:' + filetype, '')
##	fileobj.write(outputstring_enc)
##	fileobj.close()
##	fileobjl.close()
##	raw_input("write successful, press enter to close")
##	exit()

		
