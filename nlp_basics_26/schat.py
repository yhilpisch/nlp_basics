import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# List of available models
models = [
    "Qwen/Qwen1.5-1.8B-Chat",
    "deepseek-ai/deepseek-coder-1.3b-instruct"
]

# Cache to store loaded models and tokenizers
model_cache = {}

def load_model(model_name):
    if model_name not in model_cache:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
        model_cache[model_name] = (model, tokenizer)
    return model_cache[model_name]

def chatbot_interface(model_name, user_input, history):
    model, tokenizer = load_model(model_name)
    
    # Combine history with new input
    conversation = "".join([f"User: {h[0]}\nBot: {h[1]}\n" for h in history]) + f"User: {user_input}\nBot:"
    inputs = tokenizer(conversation, return_tensors="pt").to(model.device)
    
    # Generate response
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=200, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True).split("Bot:")[-1].strip()

    history.append((user_input, response))
    return history

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Simple ChatBot Interface")
    
    with gr.Row():
        model_name = gr.Dropdown(choices=models, label="Select Model", value=models[0], scale=1)
        user_input = gr.Textbox(label="Your Message", scale=3)
    
    chatbot = gr.Chatbot(height=400)

    def respond(user_input, history, model_name):
        history = chatbot_interface(model_name, user_input, history or [])
        return history, ""

    user_input.submit(respond, [user_input, chatbot, model_name], [chatbot, user_input])

# Launch the app
demo.launch()
