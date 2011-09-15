#Decoder code modified from Sample code for PyAudio
#Added AES256 Encryption

import pyaudio
import wave
import sys
import numpy as np
import base64
import binascii
import os
from math import sqrt
from Crypto.Cipher import AES

chunk = 2048
FORMAT = pyaudio.paInt16
HOST = pyaudio.paOSS
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = raw_input("How Many Seconds would you like to record?: ")
#key = raw_input("Enter expected key with a length of 16, or 32 Characters: ")
#mode = AES.MODE_CBC
#encryptor = AES.new(key, mode)
raw_input("Press any key to start recording")
WAVE_OUTPUT_FILENAME = "read.wav"

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
wf = wave.open('read.wav', 'rb')
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
outputstring_enc = '0b'

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
        print thefreq
        if int(thefreq) < 500 and int(thefreq) > 400 :
                outputstring_enc += '1'
        elif int(thefreq) < 400 and int(thefreq) > 300:
                outputstring_enc += '0'
    # read some more data
    data = wf.readframes(chunk)
if data:
    stream.write(data)
stream.close()
p.terminate()
print outputstring_enc
decodedstring = int(outputstring_enc, 2)
outputstring_enc = binascii.unhexlify('%x' % decodedstring)
#decrypted_string = base64.b64decode(outputstring_enc)
print outputstring_enc
