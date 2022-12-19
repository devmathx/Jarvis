from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import core

# Síntese de texto
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Reconhecimento de fala
model = Model("model") 
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconheciment de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        
        if result is not None:
            text = result["text"]
        
            print(">>", text)

            if text == 'que horas são' or 'me diga as horas' or 'horas':
                speak(core.SystemInfo.getTime())