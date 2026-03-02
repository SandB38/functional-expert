import os
from services import vector_store
from langchain.docstore.document import Document


def test_build_vector_store(tmp_path, monkeypatch):
    # prepare some markdown and text files
    spec_dir = tmp_path / "spec"
    spec_dir.mkdir()
    (spec_dir / "a.md").write_text("hello world")
    (spec_dir / "sub").mkdir()
    (spec_dir / "sub" / "b.txt").write_text("another text")

    # dummy classes to avoid external dependencies
    class DummyEmbeddings:
        def __init__(self, api_key=None):
            self.api_key = api_key

    class DummyFAISS:
        @staticmethod
        def from_documents(docs, embeddings):
            # return a simple object capturing inputs
            return {"docs": docs, "embeddings": embeddings}

    # monkeypatch the real classes
    monkeypatch.setattr(vector_store, "OpenAIEmbeddings", DummyEmbeddings)
    monkeypatch.setattr(vector_store, "FAISS", DummyFAISS)

    store = vector_store.build_vector_store(str(spec_dir), openai_key="dummy")

    assert isinstance(store, dict)
    assert store["embeddings"].api_key == "dummy"

    docs = store["docs"]
    assert docs, "No documents were produced by the splitter"
    assert all(isinstance(d, Document) for d in docs)
    # metadata should include source filenames
    assert all("source" in d.metadata for d in docs)
