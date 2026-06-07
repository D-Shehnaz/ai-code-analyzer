# 🤖 CODEANALYZERAGENT  
### AI-Based Code Analysis and Bug Detection System

---

## 📌 Project Overview

CODEANALYZERAGENT is an AI-powered code analysis system designed to automatically detect bugs, analyze code complexity, evaluate severity, and generate fixes.  

The system combines:
- Static code analysis (AST + rule-based detection)
- AI-based reasoning using Groq LLM API
- Modular pipeline architecture for scalability

It supports multiple programming languages such as:
- Python  
- JavaScript  
- Java  
- C/C++  
- SQL  
- PHP  

The goal of this project is to assist developers in identifying issues in code and improving code quality through automated AI-driven review.

---

## 🏗️ System Architecture / Design

The system follows a **modular pipeline architecture**:
User Input Code
↓
Language Detection Module
↓
AST Parsing Module
↓
Complexity Analysis Module
↓
Bug Detection Engine (Rule-based + AST)
↓
Severity Scoring Module
↓
Groq LLM Reasoning Engine
↓
Fix Generation Module
↓
Final Structured Report (Streamlit UI)


### 📦 Core Modules

- **agent.py** → Central coordinator
- **tools/language_detector.py** → Detects programming language
- **tools/ast_parser.py** → Parses code structure
- **tools/complexity_tool.py** → Calculates complexity
- **tools/bug_detector.py** → Finds bugs
- **tools/severitytool.py** → Assigns severity score
- **tools/llm_tool.py** → AI reasoning using Groq API
- **tools/fix_generator.py** → Generates fixed code
- **app.py** → Streamlit frontend UI


