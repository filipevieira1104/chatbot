from langchain.text_splitter import (
    CharacterTextSplitter,
)
from langchain_core.documents.base import Document
from langchain_community.document_loaders import (
    DirectoryLoader,
)
from langchain_community.vectorstores import chroma

async def load_documents(db: chroma):
    text_splitter = CharacterTextSplitter(
        chunk_size = 100, chunk_overlap =0
    )
    raw_documents = DirectoryLoader(
        "docs", "*.txt"
    ).load()
    chunks = text_splitter.split_documents(
        raw_documents
    )
    await db.aadd_documents(chunks)

def get_context(
        user_query: str, db: chroma
) -> str:
    docs = db.similarity_search(user_query)

    context = " ".join(doc.page_content.replace('\n', '')for doc in docs)
    return context