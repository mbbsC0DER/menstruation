# pip install -q transformers

from transformers import pipeline

story = pipeline("text-generation", model="gpt2")

prompt = input("Enter story starting line: ")

result = story(
    prompt,
    max_new_tokens=100
)

print(result[0]["generated_text"])
