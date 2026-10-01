

from diffusers import StableDiffusionPipeline
import torch
# Load the pre-trained model

if not torch.cuda.is_available():
    raise RuntimeError("Select Runtime > Change runtime type > T4 GPU in Colab.")
pipe = StableDiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16
)
pipe.enable_model_cpu_offload()
pipe.enable_attention_slicing()
prompt = "A futuristic city at sunset, cyberpunk style"
image = pipe(prompt).images[0]
# Save the image

image.save("output.png")
from IPython.display import display
display(image)
