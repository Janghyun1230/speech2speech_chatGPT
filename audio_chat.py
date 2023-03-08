import os
from key import key
from record import record_stream, transcribe
from chat import chat
from tts import tts
from playsound import playsound

if __name__ == '__main__':
    os.makedirs('./cache', exist_ok=True)

    messages = []
    messages.append({
        "role": "system",
        "content": "You are a helpful assistant. Please reply concisely."
    })
    msg = ''

    print("** Enter to start recording, Ctrl+c to finish recording **")
    print("Hi, I'm you're chatbot:)\n")
    try:
        while True:
            record_stream()
            msg = transcribe()

            reply = chat(msg, messages)

            output_name = tts(reply)
            playsound(output_name)
    except KeyboardInterrupt:
        print("")
