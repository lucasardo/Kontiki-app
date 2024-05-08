# Import necessary libraries.
import streamlit as st
import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai import MistralAIEmbedding

mistral_key = st.secrets["mistral_key"]

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="Store")
index = load_index_from_storage(storage_context, embed_model=MistralAIEmbedding(model_name='mistral-embed', api_key=mistral_key))
query_engine = index.as_query_engine(similarity_top_k=2)

# Define LLM and embedding model
Settings.llm = MistralAI(model="mistral-small", api_key=mistral_key)
Settings.embed_model = MistralAIEmbedding(model_name='mistral-embed', api_key="WC69QqfKgGpkKoyxjm1n3pOEDXE0m6pC")

################################################################################################################

# Set web page title, icon, and layout
st.set_page_config(
    page_title="RachelBot 💬 Kontiki",
    page_icon=":robot:",
    layout="wide"  # Set layout to wide for better organization
)

# Display title and description
st.markdown("<h1 style='color: #F9423A;'> Chatbot</h1>", unsafe_allow_html=True)
st.write("Welcome to the ESG Chatbot web app developed by WSP Digital Innovation Italy. "
         "This web app is designed to help engineers analyze environmental assessments, such as Climate Risk Assessments and Environmental Impact Assessments.")

# Create a text input box for the user to ask a question.
user_input = st.text_input("What would you like to know?")

if user_input:

    response = query_engine.query(user_input)
    
    # Display the response.
    st.write(response)
