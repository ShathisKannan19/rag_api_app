from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain.schema import Document
import os
import shutil
from langchain_community.vectorstores import Chroma
from src.utils.shared import embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_PATH = "src/data"

class UploadService:
    def __init__(self, USER):
        self.DATA_PATH = f"src/data/{USER}"
        self.CHROMA_PATH = f"src/chroma/{USER}"

    def load_documents(self):
        """
        Load PDF documents from the specified directory using PyPDFDirectoryLoader.
        Returns:
        List of Document objects: Loaded PDF documents represented as Langchain
                                                                Document objects.
        """
        # Initialize PDF loader with specified directory
        document_loader = PyPDFDirectoryLoader(self.DATA_PATH)
        print(self.DATA_PATH)
        # Load PDF documents and return them as a list of Document objects
        return document_loader.load()

    def split_text(self,documents: list[Document]):
        """
        Split the text content of the given list of Document objects into smaller chunks.
        Args:
            documents (list[Document]): List of Document objects containing text content to split.
        Returns:
            list[Document]: List of Document objects representing the split text chunks.
        """
        # Initialize text splitter with specified parameters
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1250, # Size of each chunk in characters
            chunk_overlap=200, # Overlap between consecutive chunks
            length_function=len, # Function to compute the length of the text
            add_start_index=True, # Flag to add start index to each chunk
        )

        # Split documents into smaller chunks using text splitter
        chunks = text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

        return chunks

        # Print example of page content and metadata for a chunk
        # if chunks != []:
        #     document = chunks[0]
        #     print(document.page_content)
        #     print(document.metadata)

    # Path to the directory to save Chroma database
    def save_to_chroma(self,chunks: list[Document]):
        """
        Save the given list of Document objects to a Chroma database.
        Args:
        chunks (list[Document]): List of Document objects representing text chunks to save.
        Returns:
        None
        """

        # Clear out the existing database directory if it exists
        if os.path.exists(self.CHROMA_PATH):
            shutil.rmtree(self.CHROMA_PATH)

        # Create a new Chroma database from the documents using OpenAI embeddings
        db = Chroma.from_documents(
            chunks,
            embeddings,
            # OpenAIEmbeddings(),
            persist_directory=self.CHROMA_PATH
        )

        # Persist the database to disk
        db.persist()
        print(f"Saved {len(chunks)} chunks to {self.CHROMA_PATH}.")

def load_the_docs(USER):
    """
    Load the PDF documents from the specified directory, split the text content into smaller chunks,
    and save the chunks to a Chroma database.

    Args:
        USER (str): The user for whom the documents are being loaded.
        
    Returns:
        None"""
    # Initialize the UploadService
    print("Loading the documents...")

    upload_service = UploadService(USER)

    # Load PDF documents from the specified directory
    documents = upload_service.load_documents()

    # Split the text content of the loaded documents into smaller chunks
    chunks = upload_service.split_text(documents)

    # Save the split text chunks to a Chroma database
    upload_service.save_to_chroma(chunks)

    print("Sucessfully Completed ✅")