# AI Smart Bug Analyzer & Fix Advisor

## Project Overview

AI Smart Bug Analyzer & Fix Advisor is an AI-powered project developed as part of the Infosys Springboard Internship. The objective of this project is to analyze software bug reports using Retrieval-Augmented Generation (RAG) techniques by building a historical defect knowledge base and enabling semantic similarity search on bug reports.

---

## Milestone 1 Objectives

- Study defect analysis workflows and bug report structures.
- Understand RAG architecture and semantic similarity techniques.
- Design the overall system architecture and multi-agent workflow.
- Develop a Bug Submission Module supporting text input and file upload.
- Build a Historical Defect Knowledge Base using public bug datasets.
- Generate embeddings and create a FAISS vector database for semantic search.

---

## Features Implemented

- Bug Submission Module
  - Direct bug report input
  - Stack trace input
  - Error log input
  - File upload support (.txt, .log, .pdf)

- Historical Defect Knowledge Base
  - Mozilla Bug Dataset integration
  - Data preprocessing and cleaning
  - Text chunking using LangChain
  - Embedding generation using Sentence Transformers
  - FAISS vector database indexing

- Basic RAG Pipeline
  - Semantic similarity search
  - Retrieval of similar historical bug reports

---

## System Modules

1. Bug Submission Module
2. Historical Defect Knowledge Base
3. RAG Pipeline
4. FAISS Vector Database
5. Basic Similarity Search

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- LangChain Text Splitter
- Sentence Transformers (all-MiniLM-L6-v2)
- FAISS
- VS Code
- Git & GitHub

---

## Project Structure

```text
AI_Smart_Bug_Analyzer_Fix_Advisor/
│
├── app.py
├── rag_pipeline.py
├── datasets/
├── uploads/
├── bug_index.faiss
├── embeddings.npy
├── requirements.txt
└── README.md
```

---

## Workflow

1. User submits a bug report or uploads an error log.
2. Historical bug dataset is loaded.
3. Dataset is cleaned and preprocessed.
4. Bug descriptions are divided into chunks.
5. Embeddings are generated using Sentence Transformers.
6. Embeddings are stored in a FAISS vector database.
7. User query is converted into an embedding.
8. FAISS retrieves the most similar historical bug reports.

---

## Milestone 1 Deliverables Completed

- Research on RAG Architecture
- Study of Defect Analysis Workflow
- System Design
- Bug Submission Module
- Historical Defect Knowledge Base
- Data Cleaning
- Chunking
- Embedding Generation
- FAISS Index Creation
- Basic RAG Search
- GitHub Repository

---

## Future Scope

The following modules will be implemented in upcoming milestones:

- Multi-Agent Orchestration
  - Triage Agent
  - Log Analysis Agent
  - Root Cause Agent
  - Duplicate Agent
  - Remediation Agent

- Duplicate Detection
- Structured Resolution Generation
- Defect Pattern Analytics
- Intelligent Fix Recommendation
