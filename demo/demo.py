import pyaudio

audio = pyaudio.PyAudio()

raw_file = open('demo.raw', 'rb')
audio_stream = audio.open(format=pyaudio.paInt8,
                channels=2,
                rate=44100,
                output=True)

data = raw_file.read(1024)
while data:
    audio_stream.write(data)
    data = raw_file.read(1024)

audio_stream.stop_stream()
audio_stream.close()
audio.terminate()
raw_file.close()