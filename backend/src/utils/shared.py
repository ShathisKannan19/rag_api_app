import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings
# Load the model
embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")