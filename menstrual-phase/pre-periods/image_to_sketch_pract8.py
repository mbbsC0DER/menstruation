# This follows the PDF: sketch to colored image.

import torch
from diffusers import (
    StableDiffusionControlNetPipeline,
    ControlNetModel,
    UniPCMultistepScheduler
)
import cv2
from PIL import Image
from IPython.display import display

if not torch.cuda.is_available():
    raise RuntimeError("Select Runtime > Change runtime type > T4 GPU in Colab.")

# Validate the input before downloading the models.
input_path = input("Enter uploaded sketch path (e.g. /content/sketch.jfif): ").strip()
img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError(f"Could not read image: {input_path}")
# Bound memory use and keep both dimensions divisible by 8.
height, width = img.shape
scale = 512 / max(height, width)
size = (max(8, int(width * scale) // 8 * 8), max(8, int(height * scale) // 8 * 8))
img = cv2.resize(img, size)

# 1. Load ControlNet (scribble)
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-scribble", torch_dtype=torch.float16
)
# 2. Load Stable Diffusion
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5", controlnet=controlnet,
torch_dtype=torch.float16
)
pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
pipe.enable_attention_slicing()
# 3. Convert the uploaded image to edges, as in the PDF.

img = cv2.Canny(img, 100, 200)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
control_image = Image.fromarray(img)

# 4. Generate colored image
prompt = "a colorful illustration of a cute anime character in a fantasy world, vibrant colors"
output = pipe(prompt, image=control_image,
num_inference_steps=25).images[0]
# Save result
output.save("colored.png")
display(output)
