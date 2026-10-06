from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy.io.wavfile
import torch
from IPython.display import Audio, display

def generate_music(prompt, max_new_tokens=256):
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = MusicgenForConditionalGeneration.from_pretrained(
        "facebook/musicgen-small", low_cpu_mem_usage=True
    ).to(device).eval()
    inputs = processor(text=[prompt], padding=True, return_tensors="pt").to(device)
    # The generate method returns a tensor of audio values. We need to
    # get the first item from the batch
    # and convert it to a NumPy array for scipy.io.wavfile.write.
    with torch.inference_mode():
        audio = model.generate(**inputs, do_sample=True, max_new_tokens=max_new_tokens)
    return audio.cpu(), model.config.audio_encoder.sampling_rate

if __name__ == "__main__":
    prompt = input("Enter a music description: ")
    if prompt.strip():
        audio, sampling_rate = generate_music(prompt)
        audio_values = audio[0, 0].numpy()
        scipy.io.wavfile.write("musicgen_out.wav", rate=sampling_rate,
data=audio_values)
        print("Music generated and saved as musicgen_out.wav")
        display(Audio("musicgen_out.wav"))
    else:
        print("Error: Prompt cannot be empty.")
