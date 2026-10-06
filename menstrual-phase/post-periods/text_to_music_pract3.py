# pip install -q transformers scipy

from transformers import AutoProcessor, MusicgenForConditionalGeneration
from IPython.display import Audio

p = AutoProcessor.from_pretrained("facebook/musicgen-small")
m = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

x = p(text="happy piano music", return_tensors="pt")
y = m.generate(**x, max_new_tokens=256)

Audio(y[0].numpy(), rate=32000)
