#Currently cherry picked code from ETS - does not work
import pyaudio
from numpy import zeros, linspace, short, fromstring, hstack, transpose
from scipy import fft

NUM_SAMPLES = 1024
SAMPLING_RATE = 11025
SPECTROGRAM_LENGTH = 100

_stream = None
def get_audio_data():
    global _stream
    if _stream is None:
        pa = pyaudio.PyAudio()
        _stream = pa.open(format=pyaudio.paInt16, channels=1, rate=SAMPLING_RATE,
                     input=True, frames_per_buffer=NUM_SAMPLES)
    audio_data  = fromstring(_stream.read(NUM_SAMPLES), dtype=short)
    normalized_data = audio_data / 32768.0
    return (abs(fft(normalized_data))[:NUM_SAMPLES/2], normalized_data)
get_audio_data()
