#Currently cherry picked code from ETS/PyAudio - does not work
import pyaudio
import wave
import sys
from numpy import zeros, linspace, short, fromstring, hstack, transpose
from scipy import fft

##NUM_SAMPLES = 1024
##SAMPLING_RATE = 11025
##SPECTROGRAM_LENGTH = 100

sinput = (raw_input("Hit enter to start recording: "))
srecordTime = (raw_input("How many seconds would you like to record?"))

def get_audio_data():
    pa = pyaudio.PyAudio()
    _stream = pa.open(format=pyaudio.paInt16, channels=1, rate=SAMPLING_RATE,
                 input=True, frames_per_buffer=NUM_SAMPLES)
    audio_data  = fromstring(_stream.read(NUM_SAMPLES), dtype=short)
    normalized_data = audio_data / 32768.0
    return (abs(fft(normalized_data))[:NUM_SAMPLES/2], normalized_data)
get_audio_data()
##
##
##chunk = 1024
##FORMAT = pyaudio.paInt16
##CHANNELS = 1
##RATE = 44100
####WAVE_OUTPUT_FILENAME = "output.wav"
##
##p = pyaudio.PyAudio()
##
##stream = p.open(format = FORMAT,
##                channels = CHANNELS,
##                rate = RATE,
##                input = True,
##                frames_per_buffer = chunk)
##
##print "* recording"
##all = []
##for i in range(0, RATE / chunk * srecordTime):
##    data = stream.read(chunk)
##    all.append(data)
##print "* done recording"
##
##stream.close()
##p.terminate()

### write data to WAVE file
##data = ''.join(all)
##wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
##wf.setnchannels(CHANNELS)
##wf.setsampwidth(p.get_sample_size(FORMAT))
##wf.setframerate(RATE)
##wf.writeframes(data)
##wf.close()
