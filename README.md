# 🤖 Creation of Intelligent Bug Diagnosis Platform with Fix Recommendation Assistance – Group 2

## 📌 Project Overview

Creation of Intelligent Bug Diagnosis Platform with Fix Recommendation Assistance – Group 2 is an AI-powered software debugging platform developed as part of the Infosys Springboard Internship 7.0.

The system analyzes software bug reports using Retrieval-Augmented Generation (RAG) and a Multi-Agent Architecture. It retrieves similar historical bugs, classifies severity and priority, analyzes stack traces, identifies probable root causes, detects duplicate bugs, recommends fixes, and displays structured findings through an interactive Streamlit dashboard.

## 🎯 Project Objectives

- Analyze submitted software bug reports.
- Classify bug severity and priority.
- Analyze error logs and stack traces.
- Identify affected components and possible root causes.
- Retrieve similar historical defects.
- Detect duplicate or similar bug reports.
- Recommend suitable fixes and best practices.
- Maintain a growing historical defect knowledge base.
- Identify recurring defect patterns.
- Validate the complete bug-analysis pipeline.

## 🚀 Milestone 1 – Bug Submission & Historical Knowledge Base

### Completed

- Bug Submission Module using Streamlit.
- Bug description and error-log input.
- TXT, LOG and PDF file upload.
- Historical Mozilla Bug Dataset integration.
- Data cleaning and preprocessing.
- Text chunking using LangChain.
- Sentence Transformer embeddings.
- FAISS vector database.
- Semantic similarity search.

## 🚀 Milestone 2 – Triage, Log Analysis & Multi-Agent Orchestration

### Triage Agent

- Predicts Bug Severity.
- Predicts Priority.
- Detects Affected Component.
- Generates Confidence Score.
- Provides AI Reasoning.

### Log Analysis Agent

- Detects Exception Type.
- Identifies Failure Point.
- Extracts Affected Code Path.

### Multi-Agent Orchestration

- Coordinates different agents.
- Passes outputs between analysis stages.
- Generates structured JSON results.

## 🚀 Milestone 3 – Intelligent Bug Diagnosis & Fix Recommendation

### Root Cause Agent

- Predicts the probable root cause.
- Uses historical bug information as supporting evidence.
- Provides confidence information.

### Duplicate Detection Agent

- Detects similar or duplicate bug reports.
- Uses FAISS-based semantic similarity search.
- Provides similarity information.
- Displays historical resolution information.

### Remediation Agent

- Generates fix recommendations.
- Suggests best practices.
- Provides confidence information.

### Structured Findings Dashboard

Displays:

- Severity
- Priority
- Affected Component
- Log Analysis
- Root Cause
- Duplicate Bugs
- Recommended Fix
- Historical Evidence
- Confidence Scores

## 🚀 Milestone 4 – Defect Analytics, Knowledge Base Growth & Testing

### Defect Pattern Analytics

The system analyzes stored bug history to identify:

- Total bugs analyzed.
- Severity distribution.
- Frequently affected components.
- Common exceptions.
- Common root causes.
- Recurring defect patterns.

### Knowledge Base Growth

Confirmed resolved bugs can be added to the knowledge base with:

- Bug description.
- Exception.
- Root cause.
- Recommended fix.
- Best practice.
- Confirmation status.

### End-to-End Testing

The complete pipeline was tested using five distinct bug categories:

1. UI Error
2. Login / Authentication Error
3. Database Connection Error
4. File Upload Error
5. Payment / Transaction Error

**Final Status: END-TO-END TESTING PASSED**

## ✨ Features

- Bug Submission Module
- File Upload (.txt, .log, .pdf)
- Historical Bug Retrieval
- RAG Pipeline
- Triage Agent
- Log Analysis Agent
- Root Cause Agent
- Duplicate Detection Agent
- Remediation Agent
- Defect Pattern Analytics
- Knowledge Base Growth
- Structured Findings Dashboard
- JSON Output Generation
- End-to-End Testing

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini
- Pandas
- NumPy
- LangChain
- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS
- JSON
- Git
- GitHub
- VS Code

## 📁 Project Structure

```text
AI_SMART_BUG_ANALYZER_FIX_ADVISOR/
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
├── defect_analytics.py
├── knowledge_base_growth.py
├── testing_validation.py
├── gemini_client.py
│
├── datasets/
├── uploads/
├── outputs/
│
├── bug_index.faiss
├── embeddings.npy
├── requirements.txt
├── TECHNICAL_DOCUMENTATION.md
└── README.md

```
## 🔄 Complete Bug Analysis Workflow

1. User submits a bug report through the Streamlit interface.
2. The Orchestrator receives the bug information.
3. Triage Agent analyzes severity, priority, and affected component.
4. Log Analysis Agent analyzes the error log or stack trace.
5. Root Cause Agent identifies the probable root cause.
6. Duplicate Detection Agent searches for similar historical bugs.
7. Remediation Agent generates fix recommendations.
8. The system displays the complete structured diagnosis.
9. Confirmed resolved bugs can be added to the knowledge base.
10. Defect Pattern Analytics analyzes accumulated bug history.

## 🧪 Testing Results

The system was validated using five distinct bug categories.

| Test Case | Bug Type | Status |
|---|---|---|
| 1 | UI Error | PASS ✅ |
| 2 | Login / Authentication Error | PASS ✅ |
| 3 | Database Connection Error | PASS ✅ |
| 4 | File Upload Error | PASS ✅ |
| 5 | Payment / Transaction Error | PASS ✅ |

### Agent Validation

- Triage Agent – PASS ✅
- Log Analysis Agent – PASS ✅
- Root Cause Agent – PASS ✅
- Duplicate Detection Agent – PASS ✅
- Remediation Agent – PASS ✅

### Final Testing Result

**🎉 END-TO-END TESTING PASSED**

## 📊 Results

The completed platform successfully supports:

- Intelligent bug diagnosis.
- Historical bug retrieval.
- Severity and priority classification.
- Log and stack-trace analysis.
- Root-cause identification.
- Duplicate bug detection.
- Fix recommendation.
- Defect pattern analytics.
- Knowledge base growth.
- End-to-end validation.

## 🔮 Future Scope

- AI-based code fix generation.
- Advanced LLM-based bug explanation.
- GitHub issue integration.
- Jira integration.
- Advanced bug analytics dashboard.
- Real-time bug monitoring.
- Multi-language bug analysis.
- CI/CD pipeline integration.
- Cloud-based deployment.
- Predictive defect analytics.

## 📚 Documentation

Detailed technical information is available in:

`TECHNICAL_DOCUMENTATION.md`

The documentation covers the project architecture, technologies, milestone implementation, testing, results, and future scope.


## 📌 Current Status

- Milestone 1 – ✅ Completed
- Milestone 2 – ✅ Completed
- Milestone 3 – ✅ Completed
- Milestone 4 – ✅ Completed

**🎉 PROJECT COMPLETED SUCCESSFULLY**
