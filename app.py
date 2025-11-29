from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate,load_prompt


load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    openai_api_key = OPENROUTER_API_KEY,
    openai_api_base = OPENROUTER_API_BASE
)

st.header("Research Assistant Tool")

# user_input = st.text_input("Enter your prompt here")

paper_input = st.selectbox("Select Research paper name",["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select explaination style",["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select explaination length",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')
#filling placeholders
prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)