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
*   **Language:** The user prefers to communicate in Vietnamese. (2025-09-30)

## 📚 Lesson Review: CH3-L1_System_Prompt
**Completed**: 2025-09-29
**Status**: ✅ Completed

### Learning Summary:
- **Lesson Focus**: Understanding and implementing a system prompt to control AI behavior.
- **Implementation Approach**: Added a `system_prompt` variable to `main.py` and passed it to the `generate_content` function's configuration.
- **Key Insight**: The system prompt provides a powerful way to give instructions and context to the LLM, overriding user input when necessary.

## 📚 Lesson: CH3-L2_Function_Declaration
**Started**: 2025-09-30
**Status**: 🟡 In Progress

### Learning Focus:
- **Primary Concept**: Declaring functions for the LLM to use.
- **Application**: Defining a schema for the `get_files_info` function and making it available to the model.

## 📚 Lesson Review: CH3-L2_Function_Declaration
**Completed**: 2025-09-30
**Status**: ✅ Completed

### Learning Summary:
- **Lesson Focus**: Function Calling, `FunctionDeclaration`, `Tool`.
- **Implementation Approach**: Defined a schema for `get_files_info` in its own file, created a `Tool` object in `main.py`, passed it to the `generate_content` API call, and updated the response handling logic to check for `function_calls` using an if/else block and a for loop.
- **Key Insight**: The LLM acts as a decision-making engine that outputs a structured request (`FunctionCall`), not as a direct code executor. Our application code is responsible for interpreting this request and executing the corresponding Python function.

### Knowledge Integration:
- **Previous Lesson Connections**: This lesson directly builds on CH3-L1 by adding the `tools` parameter to the `generate_content` call, alongside the `system_instruction`. It makes the functions from Chapter 2 usable by the agent.
- **Vocabulary Expansion**: `FunctionDeclaration` (the 'menu' for a function), `Schema` (defines parameters), `Tool` (a collection of functions for the LLM), `FunctionCall` (the LLM's request to run a function).
- **Application Insights**: This is the fundamental pattern for giving an LLM agent capabilities to interact with any external system, such as APIs, databases, or the local file system. It transforms the LLM from a simple chatbot into an active agent.