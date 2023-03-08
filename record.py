# reference: https://realpython.com/playing-and-recording-sound-python/
import pyaudio
import wave
import openai
from key import key

openai.api_key = key


def record_stream(fs=44100, channels=2, filename='./cache/input.wav'):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample

    _ = input("Enter to start recording..\r")
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(CURSOR_UP_ONE + ERASE_LINE, end='\r')

    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    try:
        while True:
            data = stream.read(chunk)
            frames.append(data)
    except KeyboardInterrupt:
        print(" " * 20, end='\r')

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    print('transcribing..', end='\r')


def transcribe(filename='./cache/input.wav'):
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    transcript = transcript['text']

    print(transcript)
    return transcript


if __name__ == "__main__":
    # sec = int(input("Input seconds.. "))
    record_stream()
    transcribe()
