import os
import chromadb
from chromadb.config import Settings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from typing import List

class RAGStore:
    def __init__(self, persist_directory: str = "./data/chroma_db"):
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Ensure directory exists
        os.makedirs(persist_directory, exist_ok=True)
        
        self.vector_store = Chroma(
            collection_name="personal_assistant",
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory,
        )

    def add_documents(self, documents: List[Document]):
        """Add documents to the vector store."""
        self.vector_store.add_documents(documents)

    def search(self, query: str, k: int = 4) -> List[Document]:
        """Search for relevant documents."""
        return self.vector_store.similarity_search(query, k=k)

    def delete_collection(self):
        """Delete the collection (use with caution)."""
        self.vector_store.delete_collection()
