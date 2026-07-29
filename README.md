# AI Smart Bug Analyzer & Fix Advisor

## Project Overview

AI Smart Bug Analyzer & Fix Advisor is an AI-powered project developed as part of the Infosys Springboard Internship. The project analyzes software bug reports using Retrieval-Augmented Generation (RAG) and a multi-agent architecture. It retrieves similar historical bug reports, classifies bug severity and priority, analyzes stack traces, identifies root causes, detects duplicate bugs, recommends fixes, and displays structured outputs for downstream AI agents.

---

## Milestone 1 Completed

Studied defect analysis workflows and bug report structures.
Designed the system architecture.
Developed the Bug Submission Module.
Integrated Mozilla Bug Dataset.
Performed data cleaning and preprocessing.
Implemented text chunking using LangChain.
Generated embeddings using Sentence Transformers.
Created a FAISS vector database.
Implemented semantic similarity search using RAG.

---

## Milestone 2 Completed

### Triage Agent

Predicts Bug Severity (Critical/High/Medium/Low).
Predicts Priority.
Identifies Affected Component.
Generates Confidence Score.
Provides Reasoning.

### Log Analysis Agent

Detects Exception Type.
Identifies Failure Point.
Extracts Affected Code Path.

### Multi-Agent Orchestration

Runs Triage Agent and Log Analysis Agent automatically after bug submission.
Combines outputs into a structured JSON format.
Stores the output for future milestones.

### Validation

Tested using different bug report formats and stack traces.
Verified Triage Agent and Log Analysis Agent outputs.

---

## Milestone 3 Completed

### Root Cause Agent

Built the Root Cause Agent.
Performed root cause analysis using Retrieval-Augmented Generation (RAG).
Generated probable root cause hypotheses.
Generated confidence scores.
Retrieved supporting historical evidence from the knowledge base.

### Duplicate Detection Agent

Built the Duplicate Detection Agent.
Performed semantic similarity search over historical bug reports.
Retrieved top matching duplicate bug reports.
Displayed similarity scores.
Generated historical bug resolution summaries.

### Remediation Agent

Built the Remediation Agent.
Generated AI-based fix recommendations.
Suggested best practice guidelines.
Generated confidence scores for recommendations.

### Structured Findings Display

Developed a clean Streamlit dashboard.
Displayed Bug Severity.
Displayed Priority.
Displayed Affected Component.
Displayed Log Analysis.
Displayed Root Cause Hypothesis.
Displayed Duplicate Matches.
Displayed Recommended Fix.
Displayed Confidence Scores.
Displayed Supporting Historical Evidence.
Generated a Structured Findings Summary for every bug submission.

---

## Features

Bug Submission Module.
File Upload Support (.txt, .log, .pdf).
Historical Bug Retrieval.
RAG Pipeline.
Similar Bug Search.
Triage Agent.
Log Analysis Agent.
Root Cause Agent.
Duplicate Detection Agent.
Remediation Agent.
Multi-Agent Orchestration.
Structured Findings Dashboard.
JSON Output Generation.

---

## Technologies Used

Python.
Streamlit.
Pandas.
NumPy.
LangChain Text Splitter.
Sentence Transformers (all-MiniLM-L6-v2).
FAISS.
Git.
GitHub.
VS Code.

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

## Workflow

User submits a bug report or uploads an error log.

Similar historical bugs are retrieved using FAISS.

Triage Agent predicts severity, priority, affected component, confidence score, and reasoning.

Log Analysis Agent extracts exception details, failure point, and affected code path.

Root Cause Agent predicts the probable root cause using historical bug reports.

Duplicate Detection Agent retrieves similar historical bug reports and similarity scores.

Remediation Agent generates fix recommendations and best practices.

Structured Findings Dashboard displays all agent outputs in a clean interface.

Results are saved in JSON format for future analysis.

---

## Deliverables Completed

### Milestone 1

Defect Analysis Study.
RAG Architecture.
Bug Submission Module.
Historical Defect Knowledge Base.
Data Cleaning.
Chunking.
Embedding Generation.
FAISS Index Creation.
Basic RAG Search.

### Milestone 2

Triage Agent.
Log Analysis Agent.
Multi-Agent Orchestration.
JSON Output Generation.
Validation.

### Milestone 3

Root Cause Agent.
Duplicate Detection Agent.
Remediation Agent.
Structured Findings Display.
Enhanced Streamlit Dashboard.

---

## Future Scope

AI-powered Automatic Code Fix Generation.
LLM-based Bug Explanation.
GitHub Issue Integration.
Jira Integration.
Bug Trend Analytics Dashboard.
Real-time Bug Monitoring.
Multi-language Bug Analysis.

---

## Current Status

✅ Milestone 1 Completed

✅ Milestone 2 Completed

✅ Milestone 3 Completed
