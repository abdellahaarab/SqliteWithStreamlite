from gtts import gTTS
import os

tts = gTTS("hallo Wolten","de")

tts.save('output.mp3')

# os.system("start output.mp3")