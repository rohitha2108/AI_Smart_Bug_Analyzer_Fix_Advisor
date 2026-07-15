# AI Smart Bug Analyzer & Fix Advisor

## Project Overview

AI Smart Bug Analyzer & Fix Advisor is an AI-powered project developed as part of the Infosys Springboard Internship. The project analyzes software bug reports using Retrieval-Augmented Generation (RAG) and a multi-agent architecture. It retrieves similar historical bug reports, classifies bug severity and priority, analyzes stack traces, and stores structured outputs for downstream AI agents.

---

## Milestone 1 Completed

- Studied defect analysis workflows and bug report structures.
- Designed the system architecture.
- Developed the Bug Submission Module.
- Integrated Mozilla Bug Dataset.
- Performed data cleaning and preprocessing.
- Implemented text chunking using LangChain.
- Generated embeddings using Sentence Transformers.
- Created a FAISS vector database.
- Implemented semantic similarity search using RAG.

---

## Milestone 2 Completed

### Triage Agent
- Predicts Bug Severity (Critical/High/Medium/Low)
- Predicts Priority
- Identifies Affected Component
- Generates Confidence Score
- Provides Reasoning

### Log Analysis Agent
- Detects Exception Type
- Identifies Failure Point
- Extracts Affected Code Path

### Multi-Agent Orchestration
- Runs Triage Agent and Log Analysis Agent automatically after bug submission.
- Combines outputs into a structured JSON format.
- Stores the output for future milestones.

### Validation
- Tested using different bug report formats and stack traces.
- Verified Triage Agent and Log Analysis Agent outputs.

---

## Features

- Bug Submission Module
- File Upload Support (.txt, .log, .pdf)
- Historical Bug Retrieval
- RAG Pipeline
- Similar Bug Search
- Triage Agent
- Log Analysis Agent
- Multi-Agent Orchestration
- JSON Output Generation

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- LangChain Text Splitter
- Sentence Transformers (all-MiniLM-L6-v2)
- FAISS
- Git
- GitHub
- VS Code

---

## Project Structure

```text
AI_Smart_Bug_Analyzer_Fix_Advisor/
│
├── app.py
├── rag_pipeline.py
├── search_bug.py
├── triage_agent.py
├── log_analysis_agent.py
├── orchestrator.py
├── datasets/
├── uploads/
├── outputs/
├── bug_index.faiss
├── embeddings.npy
├── requirements.txt
└── README.md
```

---

## Workflow

1. User submits a bug report or uploads an error log.
2. Similar historical bugs are retrieved using FAISS.
3. Triage Agent predicts severity, priority, affected component, confidence score, and reasoning.
4. Log Analysis Agent extracts exception details, failure point, and affected code path.
5. Orchestrator combines both agent outputs.
6. Results are saved in JSON format for future milestones.

---

## Deliverables Completed

### Milestone 1
- Defect Analysis Study
- RAG Architecture
- Bug Submission Module
- Historical Defect Knowledge Base
- Data Cleaning
- Chunking
- Embedding Generation
- FAISS Index Creation
- Basic RAG Search

### Milestone 2
- Triage Agent
- Log Analysis Agent
- Multi-Agent Orchestration
- JSON Output Generation
- Validation

---

## Future Scope

The following modules will be implemented in upcoming milestones:

- Root Cause Analysis Agent
- Duplicate Detection Agent
- Remediation Agent
- Intelligent Fix Recommendation
- Defect Pattern Analytics

---

## Current Status

✅ Milestone 1 Completed

✅ Milestone 2 Completed
