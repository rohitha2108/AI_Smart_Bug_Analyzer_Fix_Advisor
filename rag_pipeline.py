import pandas as pd
import numpy as np
import faiss

from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# -----------------------------
# Read Dataset
# -----------------------------
df = pd.read_csv("datasets/sev.csv")

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

# -----------------------------
# Data Cleaning
# -----------------------------
df = df[["Description", "Severity", "Label"]]

print("\nAfter Cleaning:")
print(df.head())

print("\nNew Shape:")
print(df.shape)

# -----------------------------
# Chunking
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = []

for text in df["Description"]:
    if pd.notna(text):
        chunks.extend(text_splitter.split_text(str(text)))

print("\nTotal Chunks Created:")
print(len(chunks))

print("\nFirst Chunk:")
print(chunks[0])

# -----------------------------
# TEST MODE (First 5000 Chunks)
# -----------------------------
chunks = chunks[:5000]

print("\nUsing Chunks:")
print(len(chunks))

# -----------------------------
# Embedding Generation
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    chunks,
    batch_size=32,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("\nTotal Embeddings Generated:")
print(len(embeddings))

print("\nEmbedding Dimension:")
print(embeddings.shape[1])
# -----------------------------
# Save Embeddings
# -----------------------------
np.save("embeddings.npy", embeddings)

print("\nEmbeddings Saved Successfully")

# -----------------------------
# FAISS Index
# -----------------------------
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("\nFAISS Index Created Successfully")
print("Total Vectors Indexed:")
print(index.ntotal)

# Save FAISS Index
faiss.write_index(index, "bug_index.faiss")

print("\nFAISS Index Saved Successfully")
# -----------------------------
# Basic RAG Search
# -----------------------------

query = "Application crashes during login"

# Convert query into embedding
query_embedding = model.encode(
    [query],
    convert_to_numpy=True
)

# Search top 5 similar chunks
k = 5
distances, indices = index.search(query_embedding, k)

print("\nSearch Query:")
print(query)

print("\nTop 5 Similar Bug Reports:\n")

for i, idx in enumerate(indices[0]):
    print(f"Result {i+1}:")
    print(chunks[idx])
    print("-" * 80)