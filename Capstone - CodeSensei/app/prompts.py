"""
CodeSensei — Prompt Templates
==============================
Define the LangChain PromptTemplates used by each agent.

Concepts used:
- LangChain PromptTemplate (Lecture 3 & 4)
- Prompt engineering best practices
- Input variables and template formatting

YOUR TASKS:
  TODO 1: Create the Bug Detector prompt template
  TODO 2: Create the Coordinator prompt template
"""

from langchain.prompts import PromptTemplate


# ──────────────────────────────────────────────
# TODO 1: Bug Detector Prompt Template
# ──────────────────────────────────────────────
# The Bug Detector agent analyzes code to find bugs.
# Your prompt should instruct the LLM to:
#
#   1. Analyze the provided code for bugs
#   2. For EACH bug found, output in this EXACT format:
#      BUG: <description of the bug>
#      SEVERITY: <critical|high|medium|low>
#      LINE: <line number or "unknown">
#      SUGGESTION: <how to fix it>
#      ---
#   3. If no bugs found, output: NO_BUGS_FOUND
#
# Input variables (these will be filled in at runtime):
#   - {code}      → The source code to analyze
#   - {language}  → The programming language
#
# Tips for a good prompt:
#   - Be specific about the output format (the parser depends on it!)
#   - Ask it to check for: logic errors, syntax issues, edge cases,
#     off-by-one errors, null/None handling, type mismatches
#   - Tell it to be thorough but not nitpicky
#
# Example:
#   BUG_DETECTOR_PROMPT = PromptTemplate(
#       input_variables=["code", "language"],
#       template="""You are a ... 
#       
#       Code ({language}):
#       ```
#       {code}
#       ```
#       
#       ... your instructions ...
#       """
#   )

BUG_DETECTOR_PROMPT = None  # TODO: Replace None with your PromptTemplate


# ──────────────────────────────────────────────
# TODO 2: Coordinator Prompt Template
# ──────────────────────────────────────────────
# The Coordinator agent takes the raw bug detector output
# and creates a final, student-friendly review summary.
#
# Your prompt should instruct the LLM to:
#   1. Summarize the bugs found in a helpful, educational tone
#   2. Give an overall code quality score from 0-100
#   3. Output in this EXACT format:
#      SUMMARY: <a 2-3 sentence summary of the review>
#      SCORE: <number from 0-100>
#
# Input variables:
#   - {code}              → The original source code
#   - {language}          → The programming language
#   - {bug_report}        → Output from the Bug Detector agent
#   - {context}           → Additional context from the student (may be empty)
#
# Tips:
#   - Be encouraging but honest
#   - Score guide: 90-100 = excellent, 70-89 = good, 50-69 = needs work, <50 = significant issues
#   - The summary should help the student LEARN, not just list errors
#
# Example:
#   COORDINATOR_PROMPT = PromptTemplate(
#       input_variables=["code", "language", "bug_report", "context"],
#       template="""You are a ...
#       
#       ... your instructions ...
#       """
#   )

COORDINATOR_PROMPT = None  # TODO: Replace None with your PromptTemplate
