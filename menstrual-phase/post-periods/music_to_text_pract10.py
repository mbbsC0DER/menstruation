# pip install -q openai-whisper

import whisper

model = whisper.load_model("base")

audio = "/content/music.mp3"

result = model.transcribe(audio)

print(result["text"])

open("music_text.txt", "w").write(result["text"])
