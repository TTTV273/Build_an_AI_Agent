# Project Overview

This is a Boot.dev course project for building an AI Agent - a toy version of Claude Code using Google's Gemini API. The project teaches how agentic AI tools work under the hood by creating a CLI agent that can perform coding tasks through function calling. This project is a Python-based AI agent that leverages the Gemini API to create a conversational AI experience in the terminal. The agent is designed to be extensible with various tools and functions.

## Core Components

*   **`main.py`**: The entry point of the application. This script handles command-line arguments, interacts with the Gemini API, and displays the AI's response. It supports a `--verbose` mode for displaying token usage.
*   **`pyproject.toml`**: Defines the project's dependencies, which include `google-genai` for Gemini API interaction and `python-dotenv` for managing environment variables.
*   **`functions/`**: This directory contains utility functions that can be used as tools by the AI agent.
    *   `get_files_info.py`: A function to list files and directories with their sizes.
    *   `get_file_content.py`: A function to read the content of a file with a character limit.
*   **`calculator/`**: A command-line calculator tool that can evaluate arithmetic expressions.
    *   `main.py`: The entry point for the calculator.
    *   `pkg/calculator.py`: Contains the core logic for parsing and evaluating expressions.

## Agent Capabilities

The AI agent being built will have these core functions:
- Scan files in directories
- Read file contents
- Write/overwrite files
- Execute Python files
- Iterative task completion through function calls

## Building and Running

### Prerequisites

*   Python >=3.10
*   An environment variable named `GEMINI_API_KEY` with a valid Gemini API key.
*   `uv` package manager

### Installation

1.  Install the dependencies using `uv`:
    ```bash
    uv pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is not present, but can be generated from `pyproject.toml`)*

### Running the Agent

To run the AI agent, execute the `main.py` script with a prompt:

```bash
python main.py "Your prompt here"
```

Alternatively, you can use `uv`:

```bash
uv run main.py "Your prompt here"
```

For more detailed output, use the `--verbose` flag:

```bash
python main.py "Your prompt here" --verbose
```

### Running the Calculator

To use the calculator tool, run its `main.py` script with an expression:

```bash
python calculator/main.py "3 + 5"
```

### Running Tests

To run the test suite:

```bash
uv run tests.py
```

## Development Conventions

*   The project follows a modular structure, with tools and functionalities separated into their own directories.
*   The calculator tool demonstrates the use of a simple package structure within the project.
*   The `functions` directory suggests a pattern for adding new tools to the AI agent.

## Course Context

This is part of Boot.dev's LLM course (Chapter 1, Lesson 1) focusing on building practical AI agents rather than training LLMs from scratch.

---

## User Preferences

*   **Learning Method:** The user prefers to learn using the Socratic method. I should act as a guide, asking questions to help them arrive at the solution, rather than implementing it directly. (2025-09-25)
*   **Socratic Method Feedback:** This method is highly effective. The user responds well to guided questions, analogies, and breaking down complex problems into smaller, concrete steps. (2025-09-25)
*   **Interaction Pattern:** The user prefers an iterative workflow with frequent validation (e.g., "check my code") after each small change. (2025-09-25)
*   **Key Challenge Area:** Structuring control flow (`if/else` logic) and combining multiple logical steps into a cohesive whole can be challenging and may require more detailed guidance. (2025-09-25)
