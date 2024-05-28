from typing import List

from langchain_community.document_loaders.text import TextLoader
from langchain_core.documents import Document
from langchain_postgres import PGVector
from langchain_text_splitters import CharacterTextSplitter

from methods.database_methods import DB_CONNECTION_STRING


def load_txt_file(file_path: str) -> List[Document]:
    loader = TextLoader(file_path)
    text_splitter = CharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=0,
        separator="\n",
    )
    return loader.load_and_split(text_splitter)

def load_documents_to_db(collection_name: str, embeddings, documents: List[Document]):
    PGVector.from_documents(
        embedding=embeddings,
        documents=documents,
        pre_delete_collection=True,
        collection_name=collection_name,
        connection=DB_CONNECTION_STRING
    )

