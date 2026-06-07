# 🤖 AI Code Analyzer Agent

## 📌 Project Overview

AI Code Analyzer Agent is an AI-powered system that automatically analyzes source code to detect bugs, evaluate complexity, assign severity, and generate fixes.  

The system combines:
- Static code analysis (AST-based parsing + rule-based detection)
- Language detection for multiple programming languages
- AI-based reasoning using Groq LLM API
- Automated fix generation

The main goal of this project is to assist developers in identifying code issues and improving code quality using an intelligent multi-step analysis pipeline.

---

## 🏗️ System Architecture / Design

The system follows a modular pipeline architecture:


User Input Code
↓
Language Detection Module
↓
AST Parser Module
↓
Complexity Analysis Module
↓
Bug Detection Module
↓
Severity Scoring Module
↓
Groq LLM Analysis Module
↓
Fix Generator Module
↓
Streamlit UI Output


### 📦 Modules Description

- **agent.py** → Main coordinator that manages workflow
- **tools/language_detector.py** → Detects programming language
- **tools/ast_parser.py** → Parses code into AST structure
- **tools/complexity_tool.py** → Computes complexity metrics
- **tools/bug_detector.py** → Detects bugs using rules + AST
- **tools/severitytool.py** → Calculates severity score
- **tools/llm_tool.py** → Uses Groq API for AI reasoning
- **tools/fix_generator.py** → Generates corrected code
- **app.py** → Streamlit frontend interface

---

## ⚙️ Setup and Installation Instructions

### 1. Clone Repository
```bash
git clone https://github.com/D-Shehnaz/ai-code-analyzer.git
cd ai-code-analyzer
2. Create Virtual Environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in root directory:

GROQ_API_KEY=your_api_key_here
5. Run the Application
streamlit run app.py
🚀 Usage Guidelines
Open the Streamlit web interface in browser
Paste or write your source code in the input box
Click Analyze
The system will display:
📊 Static Analysis
Detected programming language
AST structure
Complexity score
🚨 Bug Detection
Critical issues
Warnings
🧠 AI Review
Code explanation
Bug analysis
Suggestions for improvement
🔧 Fixed Code
Automatically generated corrected version (if applicable)
