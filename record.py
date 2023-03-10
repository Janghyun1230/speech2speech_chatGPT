# reference: https://realpython.com/playing-and-recording-sound-python/
# import pyaudio
import openai
from key import key

import queue
import sys
import os
import sounddevice as sd
import soundfile as sf

openai.api_key = key


def record_stream(fs=44100, channels=1, filename='./cache/input.wav'):
    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    _ = input("press enter to start recording..\r")
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(CURSOR_UP_ONE + ERASE_LINE, end='\r')
    try:
        os.remove(filename)
        with sf.SoundFile(filename, mode='x', samplerate=fs, channels=channels) as file:
            with sd.InputStream(
                    samplerate=fs,
                    # device=args.device,
                    channels=channels,
                    callback=callback):
                print('press Ctrl+C to stop the recording', end='\r')
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print(" " * 40, end='\r')
        print('transcribing..', end='\r')
        print(" " * 40, end='\r')


def transcribe(filename='./cache/input.wav'):
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    transcript = transcript['text']

    print(transcript)
    return transcript


if __name__ == "__main__":
    record_stream()
    transcribe()
