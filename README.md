# Getting Structured LLM Output Examples

Code examples demonstrating structured outputs with Large Language Models (LLMs) and Pydantic.

These examples are based on the [Getting Structured LLM Output](https://learn.deeplearning.ai/courses/getting-structured-llm-output) course from [DeepLearning.AI](https://www.deeplearning.ai/).

---

## Overview

Structured outputs allow LLMs to return responses guaranteed to conform to developer-defined schemas (such as [Pydantic](https://docs.pydantic.dev/) models or JSON Schemas). This repository demonstrates practical patterns for:
- Guaranteeing typed data formats (`int`, `str`, `bool`, `Optional`, `Literal`, `List`).
- Information extraction and classification from messy, real-world text (sentiment, product identification).
- Conditional business logic driven by LLMs (determining whether a customer inquiry needs a response or support ticket creation).
- Dynamic tone/persona customization.
- Batch processing and exporting structured results to Pandas DataFrames and CSV files.

---

## Repository Structure

- **`user_example.py`**: Introductory example showing how to define a Pydantic `User` model and parse structured outputs using `client.beta.chat.completions.parse`.
- **`socialmedia_example.py`**: Information extraction from social media posts into a structured `Mention` object with fields for product category, sentiment, automated responses, and support tickets.
- **`socialmedia_example_1.py`**: Advanced workflow showing synthetic customer post generation (`UserPost`, `UserPostWithExtras`), multi-stage analysis, batch iteration, and conversion into a Pandas DataFrame.
- **`helper.py`**: Helper utilities for loading environment variables and formatting/printing processed mentions.
- **`mentions-processed.csv`**: Sample CSV output containing processed social media mentions.
- **`requirements.txt`**: Python package dependencies.

---

## Setup & Installation

### 1. Prerequisites
- Python 3.10+ recommended.

### 2. Clone and Setup Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (cmd):
.\venv\Scripts\activate.bat
# On Linux / macOS:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

These examples connect to OpenAI via [AICredits](https://aicredits.in/). AICredits allows you to preload credits and use them as required, making it ideal and convenient for learning and experimentation purposes.

> **Note:** The scripts read `AI_CREDIT_KEY` and `AI_CREDIT_URL` directly from the **Windows Environment Variables** layer using `os.getenv()`.

You can configure these variables in your Windows environment:

**PowerShell (Current Session):**
```powershell
$env:AI_CREDIT_KEY = "your-aicredits-api-key"
$env:AI_CREDIT_URL = "https://api.aicredits.in/v1"
```

**Command Prompt (Current Session):**
```cmd
set AI_CREDIT_KEY=your-aicredits-api-key
set AI_CREDIT_URL=https://api.aicredits.in/v1
```

**Persistent (User / System Level):**
You can set them permanently through Windows Settings (*System Properties* -> *Environment Variables*) or via `setx`:
```cmd
setx AI_CREDIT_KEY "your-aicredits-api-key"
setx AI_CREDIT_URL "https://api.aicredits.in/v1"
```

---

## Running the Examples

### 1. Basic User Model
Demonstrates basic schema extraction:
```bash
python user_example.py
```

### 2. Social Media Mention Analysis
Extracts sentiment, product, and generates customer responses:
```bash
python socialmedia_example.py
```

### 3. Synthetic Generation & Batch Pipeline
Generates synthetic posts, analyzes mentions, and aggregates into a DataFrame:
```bash
python socialmedia_example_1.py
```

---

## References & Acknowledgments

- Course: [Getting Structured LLM Output - DeepLearning.AI](https://learn.deeplearning.ai/courses/getting-structured-llm-output)
- API Access: [AICredits](https://aicredits.in/) - Preloaded credit service for LLM experimentation
- OpenAI Documentation: [Structured Outputs Guide](https://platform.openai.com/docs/guides/structured-outputs)
- Pydantic Documentation: [pydantic.dev](https://docs.pydantic.dev/)
