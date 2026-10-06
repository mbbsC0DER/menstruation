# pip install -q transformers pillow

from transformers import pipeline
from PIL import Image

captioner = pipeline(
    "image-text-to-text",
    model = "Salesforce/blip-image-captioning-base"
)

image = Image.open("/content/mountain.jpg")

result = captioner(
    image,
    "",
    max_new_tokens=100
)

print(result[0]['generated_text'])