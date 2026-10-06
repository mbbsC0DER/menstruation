


from llama_cpp import Llama, llama_supports_gpu_offload

# Load model

llm = Llama.from_pretrained(

    repo_id="TheBloke/zephyr-7B-beta-GGUF",

    filename="zephyr-7b-beta.Q4_K_M.gguf",

    n_ctx=4096,

    n_gpu_layers=-1 if llama_supports_gpu_offload() else 0,

    chat_format="zephyr"

)

# Keep chat history

history = [{"role": "system", "content": "You are a helpful AI assistant."}]

while True:

    prompt = input("You: ").strip() # <-- this acts as your textbox

    if prompt.lower() in ["exit", "quit", "bye"]:

      print("Exiting chat.")

      break

    if not prompt:
        continue
    if prompt.lower() == "reset":
        history = history[:1]
        print("Chat history cleared.")
        continue

    history.append({"role": "user", "content": prompt})

    # Get model response

    try:
        output = llm.create_chat_completion(messages=history, max_tokens=256)
    except ValueError as exc:
        history.pop()
        print(f"Could not generate: {exc}. Type reset to clear history, or shorten your message.")
        continue

    reply = output["choices"][0]["message"]["content"]

    history.append({"role": "assistant", "content": reply})

    print(f"Assistant: {reply}\n")
