# 🤖 AI Smart Bug Analyzer & Fix Advisor
---

# 📌 Project Overview

AI Smart Bug Analyzer & Fix Advisor is an AI-powered project developed as part of the **Infosys Springboard Internship**.

The system analyzes software bug reports using **Retrieval-Augmented Generation (RAG)** and a **Multi-Agent Architecture**. It retrieves similar historical bugs, classifies severity and priority, analyzes stack traces, predicts root causes, detects duplicate bugs, recommends fixes, and displays structured findings in an interactive Streamlit dashboard.

---

# 🚀 Milestone 1 Completed

### ✅ Knowledge Base & RAG Pipeline

- Studied defect analysis workflows
- Designed system architecture
- Developed Bug Submission Module
- Integrated Mozilla Bug Dataset
- Data cleaning & preprocessing
- Text chunking using LangChain
- Generated embeddings using Sentence Transformers
- Created FAISS Vector Database
- Implemented Semantic Similarity Search (RAG)

---

# 🚀 Milestone 2 Completed

## 🤖 Triage Agent

- Predicts Bug Severity
- Predicts Priority
- Detects Affected Component
- Generates Confidence Score
- Provides AI Reasoning

## 📄 Log Analysis Agent

- Detects Exception Type
- Identifies Failure Point
- Extracts Affected Code Path

## 🔄 Multi-Agent Orchestration

- Executes agents automatically
- Combines outputs
- Stores structured JSON results

## ✅ Validation

- Tested on multiple bug reports
- Verified Triage and Log Analysis accuracy

---

# 🚀 Milestone 3 Completed

## 🧠 Root Cause Agent

- Predicts probable root cause
- Uses RAG-based historical evidence
- Generates confidence score
- Displays supporting historical bug

## 🔍 Duplicate Detection Agent

- Finds duplicate bug reports
- Semantic similarity search using FAISS
- Displays similarity score
- Shows historical resolution summary

## 🛠️ Remediation Agent

- Generates fix recommendations
- Suggests best practices
- Provides confidence score

## 📊 Structured Findings Dashboard

Displays:

- 🔥 Severity
- ⚡ Priority
- 🧩 Component
- 📄 Log Analysis
- 🧠 Root Cause
- 🔍 Duplicate Bugs
- 🛠️ Recommended Fix
- 📚 Historical Evidence
- 🎯 Confidence Scores

---

# ✨ Features

- 📄 Bug Submission Module
- 📁 File Upload (.txt, .log, .pdf)
- 🔎 Historical Bug Retrieval
- 🧠 RAG Pipeline
- 🤖 Triage Agent
- 📄 Log Analysis Agent
- 🧠 Root Cause Agent
- 🔍 Duplicate Detection Agent
- 🛠️ Remediation Agent
- 📊 Structured Findings Dashboard
- 📦 JSON Output Generation

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Frontend |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| LangChain | Text Chunking |
| Sentence Transformers | Embeddings |
| FAISS | Vector Database |
| Git | Version Control |
| GitHub | Repository |
| VS Code | Development |

---

# 📁 Project Structure

```text
AI_Smart_Bug_Analyzer_Fix_Advisor/
│
├── app.py
├── rag_pipeline.py
├── search_bug.py
├── triage_agent.py
├── log_analysis_agent.py
├── root_cause_agent.py
├── duplicate_detection_agent.py
├── remediation_agent.py
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

# 🔄 Workflow

1. User submits a bug report.
2. RAG retrieves similar historical bugs.
3. Triage Agent predicts severity and priority.
4. Log Analysis Agent analyzes stack traces.
5. Root Cause Agent predicts the probable cause.
6. Duplicate Detection Agent finds similar bugs.
7. Remediation Agent recommends fixes.
8. Structured Findings Dashboard displays all results.
9. Results are saved in JSON format.

---

# 📦 Deliverables

## ✅ Milestone 1
- RAG Architecture
- Bug Submission Module
- Knowledge Base
- FAISS Index
- Embeddings
- Semantic Search

## ✅ Milestone 2
- Triage Agent
- Log Analysis Agent
- Multi-Agent Orchestration
- JSON Output
- Validation

## ✅ Milestone 3
- Root Cause Agent
- Duplicate Detection Agent
- Remediation Agent
- Structured Findings Dashboard
- Enhanced Streamlit UI

---

# 🔮 Future Scope

- 🤖 AI Code Fix Generation
- 🧠 LLM-based Bug Explanation
- 🔗 GitHub Issue Integration
- 📋 Jira Integration
- 📈 Bug Analytics Dashboard
- 📡 Real-time Bug Monitoring
- 🌍 Multi-language Bug Analysis

---

# 📌 Current Status

| Milestone | Status |
|-----------|--------|
| Milestone 1 | ✅ Completed |
| Milestone 2 | ✅ Completed |
| Milestone 3 | ✅ Completed |
