# speech2speech_chatGPT
Simple Python wrapper for ChatGPT with speech modules (STT, TTS)  
#### Ingredients: 
- recording: pyaudio
- transcribe: whisper
- chat: ChatGPT
- TTS: gTTS

#### Support languages:
- Korean, English

### Requirements
```
pip install -r requirement.txt
```
#### Set your openai API key
1. Create key.py 
2. Write your openai key in key.py
```
key = "[Your Key]"
```

### Usage
To chat via speech 
```
python audio_chat.py
```

![example](example.png)

To chat via text 
```
python chat.py
```

