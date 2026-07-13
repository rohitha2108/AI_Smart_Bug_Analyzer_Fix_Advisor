import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load Dataset
df = pd.read_csv("datasets/sev.csv")
df = df[["Description", "Severity", "Label"]]

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = []

for text in df["Description"]:
    if pd.notna(text):
        chunks.extend(text_splitter.split_text(str(text)))

chunks = chunks[:5000]

# Load Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS Index
index = faiss.read_index("bug_index.faiss")


def search_similar_bugs(query):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(query_embedding, 3)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results