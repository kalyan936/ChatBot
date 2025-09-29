import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

# Load model
llm = Ollama(model="llama2")

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])

# Create chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit UI
st.title("My-ChatBot")
user_input = st.text_input("Ask me anything")

if user_input:
    response = chain.invoke({"question": user_input})
    st.write(response)

