
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-3B-Instruct",
    task="text-generation",
    provider="featherless-ai"
)
 
model = ChatHuggingFace(llm=llm)

st.header("Research Tool")
text_input = st.text_input("Enter Your Prompt")

if st.button("Summarize"):
    result = model.invoke(text_input)
    st.write(result.content)
    

# result = model.invoke("What is the capital of India?")
