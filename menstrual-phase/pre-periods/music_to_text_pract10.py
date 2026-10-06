
import whisper
import torch
import shutil

if shutil.which("ffmpeg") is None:
    raise RuntimeError("Run !apt-get update -qq && apt-get install -y -qq ffmpeg in Colab first.")

from google.colab import files

uploaded = files.upload()

if not uploaded:
    raise ValueError("No audio uploaded. Run again and choose an audio file.")
audio = list(uploaded.keys())[0]

model = whisper.load_model("base")

result = model.transcribe(audio, fp16=torch.cuda.is_available())

print("Generated Text:")

print(result["text"])



with open("music_text.txt", "w", encoding="utf-8") as f:

  f.write(result["text"])

files.download("music_text.txt")
