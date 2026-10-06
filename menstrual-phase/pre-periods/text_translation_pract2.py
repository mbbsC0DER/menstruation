

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model_name = "facebook/m2m100_418M"

tokenizer = M2M100Tokenizer.from_pretrained(model_name)

model = M2M100ForConditionalGeneration.from_pretrained(model_name, low_cpu_mem_usage=True)

langs = { "1": ("English", "en"), "2": ("Hindi", "hi"), "3": ("Marathi",
"mr"), "4": ("Gujarati", "gu"), "5": ("French", "fr"), "6": ("German",
"de"), "7": ("Spanish", "es"), "8": ("Japanese", "ja"), "9": ("Arabic",
"ar") }

print("Languages:")

for n, (name, code) in langs.items():

    print(n, name)

src = input("\nSource language number: ").strip()

dest = input("Destination language number: ").strip()

text = input("Enter text: ").strip()
if src not in langs or dest not in langs:
    raise ValueError("Choose language numbers from 1 to 9.")
if not text:
    raise ValueError("Enter some text to translate.")

src_name, src_code = langs[src]

dest_name, dest_code = langs[dest]

tokenizer.src_lang = src_code

encoded = tokenizer(text, return_tensors="pt")

output = model.generate( **encoded,
forced_bos_token_id=tokenizer.get_lang_id(dest_code), max_new_tokens=256 )

translation = tokenizer.decode(output[0], skip_special_tokens=True)

print("\nOriginal:", text)

print("Translation:", translation)
