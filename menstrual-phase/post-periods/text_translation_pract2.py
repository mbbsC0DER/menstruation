# pip install -q transformers sentencepiece

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-hi"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = input("Enter text: ")

inputs = tokenizer(text, return_tensors="pt")
output = model.generate(**inputs)

print(tokenizer.decode(output[0], skip_special_tokens=True))
