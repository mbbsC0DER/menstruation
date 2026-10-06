# Image to Black & White Sketch
# pip install -q diffusers transformers accelerate

from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
from IPython.display import display
import torch

p = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

img = Image.open("/content/scenery.jpg").convert("RGB").resize((512, 512))

out = p(
    "detailed black and white pencil sketch, monochrome, no color",
    image=img,
    strength=0.7
).images[0]

out = out.convert("L")
display(out)
