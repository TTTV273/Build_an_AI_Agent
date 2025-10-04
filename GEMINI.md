# Project Overview

This is a Boot.dev course project for building an AI Agent - a toy version of Claude Code using Google's Gemini API. The project teaches how agentic AI tools work under the hood by creating a CLI agent that can perform coding tasks through function calling.

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

## User Learning Preferences

- **Learning Method**: Socratic method preferred - act as a guide with questions to help arrive at solutions, rather than implementing directly
- **Language**: Vietnamese preferred for communication
- **Interaction Pattern**: Iterative workflow with frequent validation after each small change
- **Effective Techniques**: Guided questions, analogies, breaking down complex problems into smaller concrete steps
- **Challenge Areas**: Structuring control flow (if/else logic) and combining multiple logical steps may require detailed guidance

## AI Collaboration Strategy

This project leverages **TWO AI assistants** for optimal development:

### Gemini CLI (You - Large Context Specialist!)
- **Context**: 1M tokens (5x larger than Claude!)
- **Best for**: Large codebase analysis, complex reasoning, multi-file processing, architectural insights
- **Strengths**: Massive context window allows analyzing entire project at once

### Claude Code (Structured Workflow Specialist)
- **Context**: 200K tokens
- **Best for**: File operations, Git workflows, MCP/Neo4j integration, slash commands
- **Strengths**: Superior tool integration, structured task execution

### Collaboration Pattern:
1. **Gemini**: Analyzes large context, provides insights (via `gemini -p "{prompt}"`)
2. **Claude**: Executes structured workflows based on Gemini's analysis

**Full Guide**: See `.claude/docs/ai-collaboration-guide.md` for detailed patterns and examples.

---

### 📝 Lesson Summary: CH3-L3: More Declarations - Expanding AI Agent Toolkit

- **Lesson Focus**: FunctionDeclaration Scaling: Extending AI agent capabilities from single function to multiple function toolkit through consistent schema patterns, Schema Type System: Mastering types.Type.STRING for simple parameters and types.Type.ARRAY with items declaration for list parameters, Security by Design: Systematic hiding of working_directory parameter across all function schemas to maintain sandbox boundary control, Optional Parameter Communication: Using description conventions ('If not provided...') to indicate optional parameters without explicit required field in Gemini API, LLM Function Selection: Understanding how LLM uses function descriptions and parameter schemas to autonomously choose appropriate function based on natural language user intent
- **Applied Programming Patterns**: Pattern Replication: Consistent FunctionDeclaration structure (name, description, parameters.properties) applied across all 4 schemas for maintainability, Module Organization: Separate schema definitions co-located with function implementations in individual module files (get_file_content.py, run_python_file.py, write_file.py), Tool Registry Pattern: Centralized types.Tool with function_declarations list enabling plugin-like architecture for function registration, System Instruction Layer: Separation of API documentation (schemas) from behavioral guidance (system_prompt) following separation of concerns principle, Professional API Documentation Style: Concise, passive-voice descriptions focusing on 'what' (functionality) not 'why' (implementation rationale), Type Safety: Explicit type declarations (STRING, ARRAY) with nested items schema for array element types ensuring type-safe LLM parameter generation
- **Key Insight**: Building effective AI agents requires clear separation between LLM decision-making (through comprehensive function schemas) and Python execution control (through hidden security parameters). The quality of schema descriptions directly determines LLM's ability to autonomously select correct functions - professional, concise documentation is not just good practice but functional requirement for agent intelligence.
- **Skill Progression**: From single-function LLM integration (L2) to complete multi-function AI agent toolkit with CRUD operations. Successfully applied schema type system (STRING vs ARRAY with items), pattern replication across multiple function declarations, and professional API documentation standards. Can now think in security-first design patterns by consistently hiding sensitive parameters across all schemas.

### 📝 Lesson Summary: CH3-L2: Function Declaration

- **Lesson Focus**: Function Calling architecture, FunctionDeclaration schema creation, Tool container configuration, LLM reasoning vs execution separation
- **Implementation Approach**: Created `schema_get_files_info` using `types.FunctionDeclaration` to describe the function interface to the LLM. Configured `types.Tool` with function declarations and passed to `GenerateContentConfig`. Implemented conditional response handling to check `response.function_calls` vs `response.text`.
- **Testing Results**: Successfully demonstrated LLM function call generation with test queries about file listing in different directories.

### Pattern Recognition Progress:

- **New Patterns**: Command Pattern (LLM as Client, Python as Invoker), Schema-driven Development, Security by Design (parameter hiding)
- **Pattern Connections**: Similar to OpenAPI/Swagger documentation (machine-readable API specs), Plugin architecture (extensible function library), Separation of concerns (reasoning vs execution)
- **Confidence Level**: High - production-ready function declaration implementation

### Knowledge Integration:

- **Previous Lesson Connections**: Builds on CH3-L1 system prompts by adding actionable capabilities. Integrates CH2 file operations (get_files_info) with AI reasoning layer. Demonstrates progression: System instruction → Function calling → Agent actions
- **Vocabulary Expansion**: `FunctionDeclaration`, `types.Schema`, `types.Type.OBJECT`, `types.Tool`, `response.function_calls`, Command Pattern
- **Application Insights**: LLMs don't execute code - they generate structured requests. The application maintains full control and security. This architecture scales through plugin patterns as more functions are added.

### Areas for Future Focus:

- **Reinforcement Needed**: Understanding function call loops and multi-step reasoning chains
- **Advanced Applications**: Multiple function declarations, function call error handling, iterative agent loops
- **Practice Opportunities**: Add more function declarations (get_file_content, write_file), implement function execution logic, build complete agent loop

### 📝 Lesson Summary: L4-Write_File

- **Lesson Focus**: Secure File Writing, Filesystem Security, Path Validation
- **Implementation Approach**: Created a `write_file` function that validates the file path against a working directory before writing content. It uses `os.path.abspath` to prevent directory traversal attacks and `os.makedirs` to create directories if they don't exist.
- **Testing Results**: All tests passed, including the security test that attempted to write to `/tmp/temp.txt`.

### Pattern Recognition Progress:

- **New Patterns**: Secure File I/O Wrapper, Defensive Programming
- **Pattern Connections**: This lesson builds on the concept of creating safe tool functions for the agent, similar to the read-only functions from previous lessons, but with the added responsibility of modifying the filesystem.
- **Confidence Level**: High

### Knowledge Integration:

- **Previous Lesson Connections**: Connects to `get_files_info` and `get_file_content` by expanding the agent's interaction with the filesystem from read-only to read-write.
- **Vocabulary Expansion**: `os.makedirs`, `os.path.dirname`, `os.path.abspath`
- **Application Insights**: Writing files is a powerful but dangerous capability for an AI agent. Strong security measures, like restricting writes to a specific directory, are crucial.

### Areas for Future Focus:

- **Reinforcement Needed**: None at the moment.
- **Advanced Applications**: Appending to files, creating temporary files, and handling binary data.
- **Practice Opportunities**: Create a function to log agent activities to a file.

### 📝 Lesson Summary: L1-Build_an_AI_Agent

- **Lesson Focus**: Agentic AI: Building AI systems that can iteratively execute functions to complete complex tasks, Function Calling: Using LLMs with predefined functions to interact with external systems, CLI Agent Architecture: Creating command-line tools that accept natural language tasks, LLM Integration: Using Google Gemini API for AI-powered task processing, Iterative Problem Solving: Agents that can make multiple function calls in sequence to solve problems
- **Applied Programming Patterns**: Environment Configuration: Using dotenv for API key management and secure credential handling, Command-Line Interface Pattern: Argument parsing with sys.argv and error handling for missing inputs, Client-Server Architecture: Initializing and using external API clients (Google Gemini) with proper error handling, Verbose Mode Implementation: Conditional output based on command-line flags for debugging and monitoring, Token Usage Tracking: Monitoring API consumption through response metadata analysis, Security-First Function Design: Path validation, working directory constraints, and input sanitization in agent functions, Defensive Programming: Comprehensive error handling with try-catch blocks and early returns for invalid states
- **Key Insight**: This lesson demonstrates that building effective AI agents isn't about training models, but about creating secure, modular function interfaces that allow pre-trained LLMs to interact safely with external systems through iterative function calling.
- **Skill Progression**: From basic Python CLI applications to building secure, modular AI agent architectures with external API integration and defensive programming practices.
