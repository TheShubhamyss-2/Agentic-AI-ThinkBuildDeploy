# 🥋CodeSensei — AI-Powered Code Review & Learning Platform

> **Eval 2 Capstone Project** — Build a multi-agent AI system that reviews code, finds bugs, and helps students learn.

---

## What You're Building

CodeSensei is a **multi-agent AI system** that takes a student's code as input and returns:

1. **Bug Detection** — Identifies logic errors, syntax issues, and edge cases
2. **Fix Suggestions** — Explains how to fix each bug
3. **Quality Score** — Rates the code from 0-100
4. **Learning Summary** — Educational feedback to help the student improve

You'll build this using **LangChain** for agent orchestration and **FastAPI** for the REST API.

### System Overview

```
Student Code -> POST /review-code -> Coordinator Agent
                                        |
                                   Bug Detector Agent -> Gemini LLM
                                        |
                                   Parse Bugs -> Score + Summary
                                        |
                                   JSON Response <- ReviewResponse
```

> See [`docs/architecture.md`](docs/architecture.md) for the full architecture diagram.

---

## Concepts Used (Lecture Mapping)

| Lecture | Topic | Where It's Used |
|---------|-------|-----------------|
| L2 | Environment Mastery | Virtual env, `.env`, dependencies |
| L3 | RAG Revolution | LangChain, PromptTemplate, LLM chains |
| L4 | State & Memory | LangChain patterns, chain composition |
| L5 | Agentic AI Systems | Multi-agent design, autonomous agents |
| L6 | Agent Control Flow | Agent orchestration, sequential pipeline |
| L8 | Production Backend | FastAPI, REST endpoints, Pydantic validation |

---

## Project Structure

```
Capstone - CodeSensei/
├── README.md               <- You are here
├── requirements.txt        <- Python dependencies
├── .env.example            <- Template for API keys
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── config.py           <- PROVIDED — LLM connection & env setup
│   ├── schemas.py          <- TODO — Define Pydantic data models
│   ├── prompts.py          <- TODO — Write LangChain PromptTemplates
│   ├── agents.py           <- TODO — Implement agent logic & parsing
│   └── main.py             <- TODO — Build the FastAPI endpoint
│
├── tests/
│   ├── __init__.py
│   └── test_review.py      <- Tests to verify your implementations
│
└── docs/
    └── architecture.md     <- System architecture diagram
```

---

## Setup Instructions

### 1. Create a Virtual Environment

```bash
cd "Capstone - CodeSensei"
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key

```bash
cp .env.example .env
# Edit .env and add your Gemini API key
# Get one at: https://aistudio.google.com/apikey
```

### 4. Verify Setup

```bash
python -c "from app.config import llm; print('Setup complete!')"
```

You should see:
```
Gemini LLM initialized successfully!
Setup complete!
```

---

## Your TODO Checklist

Complete these in order — each step builds on the previous one.

### Step 1: Define the Data Models (`app/schemas.py`)

| TODO | What to Do | Hint |
|------|-----------|------|
| TODO 1 | Define `CodeReviewRequest` fields | `code: str`, `language: Language`, `context: Optional[str]` |
| TODO 2 | Define `BugReport` fields | `bug_description`, `severity`, `suggestion`, `line_number` |
| TODO 3 | Define `ReviewResponse` fields | `bugs: List[BugReport]`, `summary`, `score` (0-100) |

**Verify:** `pytest tests/test_review.py::test_code_review_request_valid -v`

### Step 2: Write the Prompt Templates (`app/prompts.py`)

| TODO | What to Do | Key Point |
|------|-----------|-----------|
| TODO 1 | Write `BUG_DETECTOR_PROMPT` | Must output in exact format: `BUG:`, `SEVERITY:`, `LINE:`, `SUGGESTION:`, `---` |
| TODO 2 | Write `COORDINATOR_PROMPT` | Must output: `SUMMARY:` and `SCORE:` |

**Key Concept:** The prompts define the *behavior* of each agent. The output format must be exact because the parser depends on it!

### Step 3: Implement the Agent Logic (`app/agents.py`)

| TODO | What to Do | Key Concept |
|------|-----------|------------|
| TODO 1 | Implement `parse_bug_report()` | String parsing into Pydantic objects |
| TODO 2 | Implement `run_bug_detector()` | Use `BUG_DETECTOR_PROMPT | llm` chain |
| TODO 3 | Implement `run_coordinator()` | Orchestrate: bug detector -> coordinator LLM -> response |

**Verify:** `pytest tests/test_review.py::test_parse_bug_report_single_bug -v`

### Step 4: Build the API Endpoint (`app/main.py`)

| TODO | What to Do | Key Concept |
|------|-----------|------------|
| TODO 1 | Implement `POST /review-code` | Call `run_coordinator()`, handle errors with `HTTPException` |

**Verify:** Start the server and test with curl (see below)

---

## Running the Application

### Start the Server

```bash
uvicorn app.main:app --reload --port 8000
```

### Test with curl

```bash
# Health check
curl http://localhost:8000/health

# Review code
curl -X POST http://localhost:8000/review-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def add(a, b):\n    return a - b",
    "language": "python",
    "context": "Simple addition function"
  }'
```

### Test with the Swagger UI

Open your browser to: **http://localhost:8000/docs**

FastAPI auto-generates an interactive API documentation page where you can test your endpoint directly!

### Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_review.py::test_code_review_request_valid -v
```

---

## Tips

1. **Work in order** — schemas -> prompts -> agents -> main. Each builds on the last.
2. **Read the comments** — Every TODO has step-by-step instructions and examples.
3. **Test frequently** — Run the relevant test after completing each TODO.
4. **Prompt engineering matters** — The quality of your prompts directly affects the quality of reviews. Experiment!
5. **Use the pipe operator** — `chain = prompt | llm` is LangChain's modern syntax for chaining.
6. **Handle edge cases** — What if the LLM returns unexpected output? Use try/except.

---

## Example Input/Output

**Input:**
```python
def find_max(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
```

**Expected Bugs Found:**
- `max_num` initialized to 0 — fails for negative numbers (Severity: HIGH)
- No check for empty list — will return 0 for `[]` (Severity: MEDIUM)

**Expected Response:**
```json
{
  "bugs": [
    {
      "bug_description": "Initial value of 0 fails for lists with only negative numbers",
      "severity": "high",
      "suggestion": "Initialize max_num to float('-inf') or numbers[0]",
      "line_number": 2
    },
    {
      "bug_description": "No handling for empty list input",
      "severity": "medium",
      "suggestion": "Add a check: if not numbers: return None",
      "line_number": 1
    }
  ],
  "summary": "Found 2 bugs. The main issue is the initialization of max_num to 0...",
  "score": 55,
  "language": "python"
}
```

---

## Resources

- [LangChain Docs](https://python.langchain.com/docs/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Google Gemini API](https://ai.google.dev/)

---

*Built for the "Build & Deploy AI Agents" course — Eval 2 Capstone Project*
