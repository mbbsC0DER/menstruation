# pip install -q diffusers transformers accelerate

from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

prompt = input("Enter prompt: ")

image = pipe(prompt).images[0]

image.save("output.png")
image.show()
