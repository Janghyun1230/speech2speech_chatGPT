from gtts import gTTS
from playsound import playsound
import regex


def is_korean(text):
    if regex.search(r'\p{IsHangul}', text):
        return 'ko'
    return 'en'


def tts(text, output_name='./cache/output.wav'):
    lang = is_korean(text)

    tts = gTTS(text, lang=lang)
    tts.save(output_name)

    return output_name


if __name__ == "__main__":
    output_name = tts("hello?")
    playsound(output_name)
