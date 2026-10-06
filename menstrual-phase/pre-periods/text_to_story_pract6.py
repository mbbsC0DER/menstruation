from transformers import pipeline

# Initialize the GPT-2 text generation pipeline

generator = pipeline("text-generation", model="gpt2")

# Function to generate a story

def generate_story(prompt, max_new_tokens=150):

    # Generate text

    if not prompt.strip():
        raise ValueError("Enter a non-empty story prompt.")
    if len(generator.tokenizer.encode(prompt)) + max_new_tokens > generator.model.config.n_positions:
        raise ValueError("Prompt is too long. Shorten it to leave room for the story.")
    story = generator(
        prompt, max_new_tokens=max_new_tokens, do_sample=True,
        num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id
    )[0]["generated_text"]

    return story

# Example usage

if __name__ == "__main__":

    prompt = input("Enter a story prompt (e.g., 'Once upon a time in a magical forest'): ")

    generated_story = generate_story(prompt)

    print("\nGenerated Story:\n", generated_story)
