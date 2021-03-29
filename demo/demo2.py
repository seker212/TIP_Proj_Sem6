import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
BUFFER = []


def audio_input():
    global BUFFER
    audio_in = pyaudio.PyAudio()
    stream_in = audio_in.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    
    print('Recording...')
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream_in.read(CHUNK)
        BUFFER.append(data)

    print('Recording ENDED')

    stream_in.stop_stream()
    stream_in.close()
    audio_in.terminate()


def audio_output():
    global BUFFER
    audio_out = pyaudio.PyAudio()
    stream_out = audio_out.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, output=True)
    
    print('Playing')
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = BUFFER.pop()
        stream_out.write(data)
    print('END')

    stream_out.stop_stream()
    stream_out.close()
    audio_out.terminate()

audio_input()
BUFFER.reverse()
audio_output()