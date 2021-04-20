import pyaudio
from typing import Optional
from settings import *

class AudioHelper:
    def __init__(self):
        self.pyaudio_in: pyaudio.PyAudio = pyaudio.PyAudio()
        self.pyaudio_out: pyaudio.PyAudio = pyaudio.PyAudio()
        self.audio_stream_in: Optional[Stream] = None
        self.audio_stream_out: Optional[Stream] = None

    def terminate(self) -> None:
        #TODO: Check if audio_stream_in and audio_stream_out is stopped and closed
        self.pyaudio_in.terminate()
        self.pyaudio_out.terminate()

    def open_input_stream(self) -> None:
        self.audio_stream_in = self.pyaudio_in.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    def audio_input_read(self):
        return self.audio_stream_in.read(CHUNK)
    
    def close_input_stream(self) -> None:
        self.audio_stream_in.stop_stream()
        self.audio_stream_in.close()

    def open_output_stream(self) -> None:
        self.audio_stream_out = self.pyaudio_out.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, output=True)

    def audio_output_write(self, data) -> None:
        self.audio_stream_out.write(data)
    
    def close_output_stream(self) -> None:
        self.audio_stream_out.stop_stream()
        self.audio_stream_out.close()