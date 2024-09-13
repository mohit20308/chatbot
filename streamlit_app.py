import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = '/content/drive/MyDrive/ChatBot/trained_model'

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

if "messages" not in st.session_state:
    st.session_state.messages = []

dialog_no = 0

st.title("Cairo - A ChatBOT")
message = st.chat_message("assistant")
message.write("Hi, I am Cairo BOT. How can I help?")

while True:
    if prompt := st.chat_input("Type here..."):
        message = st.chat_message("user")
        message.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt == 'quit' or prompt == 'bye':
        break

    user_input_ids = tokenizer.encode('hi' + tokenizer.eos_token, return_tensors = 'pt')
    chat_bot_input_ids = torch.cat([chat_history_ids, user_input_ids], dim=-1) if dialog_no > 0 else user_input_ids
    chat_history_ids = model.generate(chat_bot_input_ids, max_length = 1000, pad_token_id = tokenizer.eos_token_id)

    message = st.chat_message("assistant")
    message.markdown(f'{tokenizer.decode(chat_history_ids[:, chat_bot_input_ids.shape[-1]:][0], skip_special_tokens=True), is_user=True}')
    st.session_state.messages.append({"assistant": "user", "content": prompt})
    
    dialog_no += 1

