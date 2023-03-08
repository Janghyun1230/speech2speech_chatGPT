from gtts import gTTS
from playsound import playsound


def tts(text, output_name='./cache/output.wav'):
    tts = gTTS(text)
    tts.save(output_name)

    return output_name


if __name__ == "__main__":
    output_name = tts("hello")
    playsound(output_name)
