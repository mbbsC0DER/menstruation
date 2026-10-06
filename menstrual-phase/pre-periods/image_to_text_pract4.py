from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large", low_cpu_mem_usage=True).eval()

def describe_image(image_path):
    if not os.path.exists(image_path):
        return "Error: Image file not found."
    try:
        # The processor expects images in RGB format
        raw_image = Image.open(image_path).convert("RGB")

        # Prepare the image for the model
        inputs = processor(images=raw_image, return_tensors="pt")

        # Generate captions
        outputs = model.generate(**inputs, max_new_tokens=100,
num_beams=5)

        # Decode the generated tokens to a human-readable caption
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error: Failed to process image. Details: {e}"

if __name__ == "__main__":
    image_path = input("Enter image path: ").strip()
    if image_path:
        description = describe_image(image_path)
        print("Description:", description)
    else:
        print("Error: Image path cannot be empty.")
