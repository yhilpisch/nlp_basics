#
# From ChatGPT (o3-mini-high)
#

import time
import threading
import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer

# List of available models
models = [
    "Qwen/Qwen1.5-1.8B-Chat",
    "deepseek-ai/deepseek-coder-1.3b-base",
    "deepseek-ai/deepseek-coder-1.3b-instruct",
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    # "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
]

# Check for available device: CUDA > MPS > CPU
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
print(f"Using device: {device}")

# Global cache for loaded models and tokenizers.
loaded_models = {}

def load_model(model_name: str):
    if model_name not in loaded_models:
        print(f"Loading model {model_name} ...")
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model.to(device)
        loaded_models[model_name] = (model, tokenizer)
    return loaded_models[model_name]

def format_prompt(history):
    """
    Formats the conversation history into a prompt string.
    Expects history to be a list of dictionaries with keys "role" and "content".
    For the last assistant message with empty content, it appends "Assistant:" without a newline.
    """
    prompt = ""
    for i, message in enumerate(history):
        if message["role"] == "user":
            prompt += f"User: {message['content']}\n"
        elif message["role"] == "assistant":
            # For the last assistant message with empty content, do not add a newline.
            if i == len(history) - 1 and message["content"] == "":
                prompt += "Assistant:"
            else:
                prompt += f"Assistant: {message['content']}\n"
    return prompt

def chat_with_model(user_message, history, model_name, max_new_tokens):
    if history is None:
        history = []
    # Append new user message and an empty assistant message.
    history = history + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": ""}
    ]
    prompt = format_prompt(history)
    
    model, tokenizer = load_model(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device) if "attention_mask" in inputs else None

    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    generation_kwargs = dict(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=int(max_new_tokens),
        streamer=streamer,
        do_sample=True,
        temperature=0.7,
    )

    generation_thread = threading.Thread(target=model.generate, kwargs=generation_kwargs)
    generation_thread.start()

    start_time = time.time()
    token_count = 0
    generated_text = ""
    
    for new_text in streamer:
        generated_text += new_text
        token_count += len(tokenizer.tokenize(new_text))
        elapsed = time.time() - start_time
        tokens_per_sec = token_count / elapsed if elapsed > 0 else token_count
        history[-1]["content"] = generated_text
        yield history, f"{tokens_per_sec:.2f} tokens/s", history

    generation_thread.join()

with gr.Blocks(title="Chat with Transformers Models") as demo:
    gr.Markdown("## Chat with Transformers Models")
    
    with gr.Row():
        model_dropdown = gr.Dropdown(label="Select Model", choices=models, value=models[0])
        max_tokens_input = gr.Number(label="Max New Tokens", value=250)
    
    # Use the new 'messages' type for the Chatbot component.
    chatbot = gr.Chatbot(type="messages", label="Chat")
    token_speed_display = gr.Textbox(label="Token Speed (tokens/s)", interactive=False)
    
    with gr.Row():
        user_input = gr.Textbox(placeholder="Enter your message here...", label="Your Message")
        submit_btn = gr.Button("Submit")
    
    state = gr.State([])

    submit_btn.click(
        chat_with_model,
        inputs=[user_input, state, model_dropdown, max_tokens_input],
        outputs=[chatbot, token_speed_display, state],
        api_name="chat"
    )
    user_input.submit(
        chat_with_model,
        inputs=[user_input, state, model_dropdown, max_tokens_input],
        outputs=[chatbot, token_speed_display, state],
        api_name="chat"
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
