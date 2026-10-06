# pip install -q gtts

from gtts import gTTS
from IPython.display import Audio

text = "Hello, this is my generated music"
tts = gTTS(text)
tts.save("music.mp3")

Audio("music.mp3")
