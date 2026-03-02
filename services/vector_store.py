import os
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def build_vector_store(spec_path: str, openai_key: str):
    docs = []

    for root, _, files in os.walk(spec_path):
        for file in files:
            if file.endswith(".md") or file.endswith(".txt"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    docs.append(
                        Document(
                            page_content=f.read(),
                            metadata={"source": file}
                        )
                    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    split_docs = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(api_key=openai_key)

    return FAISS.from_documents(split_docs, embeddings)
