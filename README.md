# Zecpath AI System

This repository contains the modular AI services for the Zecpath hiring platform.

## Folder Structure
- data/ : Datasets and sample files
- parsers/ : Resume parsing logic
- ats_engine/ : ATS scoring and ranking
- screening_ai/ : Voice screening modules
- interview_ai/ : Interview intelligence modules
- scoring/ : Final scoring and decision logic
- utils/ : Utilities (logging, config)
- tests/ : Test scripts
- logs/ : Application logs

## Setup
1. Create and activate venv
2. Install requirements: pip install -r requirements.txt
3. Run: python main.py

# Day 5 – Resume Text Extraction Engine
## Objective
The objective of this task is to build a base text extraction engine that converts resumes
(PDF/DOCX) into clean, structured, and usable AI-ready text for further processing.

---

## Project Structure

zecpath-ai-system/
│
├── main.py
├── README.md
├── parsers/
│   ├── __init__.py
│   ├── pdf_reader.py
│   ├── docx_reader.py
│
├── utils/
│   ├── __init__.py
│   ├── cleaner.py
│
├── tests/
│   └── test_extractor.py
│
├── logs/
│
└── requirements.txt

---

## Features Implemented

- PDF resume text extraction
- DOCX resume text extraction
- Removal of unwanted symbols and noise
- Normalization of bullet points and spacing
- Clean and readable text output
- Automated testing for extraction validation

---

## How It Works

1. The resume file path is provided as input.
2. The system detects file type (PDF or DOCX).
3. Raw text is extracted using appropriate parser.
4. Extracted text is cleaned and normalized.
5. Clean text is returned for further AI processing.

---

## How to Run the Project

### Step 1: Activate virtual environment
```bash
venv\Scripts\activate

Day 6 – Job Description Parsing System

Objective

The objective of this task is to build a system that converts job descriptions into structured, AI-readable job requirement data.

This involves extracting key information such as role name, required skills, experience, and education from unstructured JD data and converting it into a clean and usable format (JSON) for further processing.