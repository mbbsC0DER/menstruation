# pip install -q transformers accelerate

from transformers import pipeline

bot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

while True:
    q = input("You: ")

    if q.lower() in ["exit", "quit", "bye"]:
        break

    messages = [{"role": "user", "content": q}]

    result = bot(messages, max_new_tokens=100)

    print("Bot:", result[0]["generated_text"][-1]["content"])
