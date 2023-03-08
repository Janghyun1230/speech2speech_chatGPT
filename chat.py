import os
import openai
from key import key

openai.api_key = key


def chat(msg, messages=None):
    if messages is None:
        messages = []
    messages.append({"role": "user", "content": msg})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    reply = completion['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": reply})
    print(reply, "\n")
    return reply


if __name__ == '__main__':
    messages = []
    messages.append({
        "role": "system",
        "content": "You are a helpful assistant. Please reply concisely."
    })
    msg = ''

    print("Hi, I'm you're chatbot:)\n")
    try:
        while True:
            msg = input("")
            reply = chat(msg, messages)
    except KeyboardInterrupt:
        print("")
