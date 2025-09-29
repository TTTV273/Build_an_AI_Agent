# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Boot.dev course project for building an AI Agent - a toy version of Claude Code using Google's Gemini API. The project teaches how agentic AI tools work under the hood by creating a CLI agent that can perform coding tasks through function calling.

## Project Structure

- `CH1-LLMs/L1-Build_an_AI_Agent/` - Course lesson materials
  - `Lesson.md` - Main lesson content explaining the AI agent project

## Technologies

- Python 3.10+
- Google Gemini API (free tier)
- uv package manager
- Function calling for agent capabilities

## Agent Capabilities

The AI agent being built will have these core functions:
- Scan files in directories
- Read file contents
- Write/overwrite files
- Execute Python files
- Iterative task completion through function calls

## Development Commands

This project uses `uv` as the package manager. Common commands will be:
- `uv run main.py "task description"` - Run the agent with a task
- Boot.dev CLI tests for submission

## Course Context

This is part of Boot.dev's LLM course (Chapter 1, Lesson 1) focusing on building practical AI agents rather than training LLMs from scratch.

### 📝 Lesson Summary: L1-Build_an_AI_Agent

- **Lesson Focus**: Agentic AI: Building AI systems that can iteratively execute functions to complete complex tasks, Function Calling: Using LLMs with predefined functions to interact with external systems, CLI Agent Architecture: Creating command-line tools that accept natural language tasks, LLM Integration: Using Google Gemini API for AI-powered task processing, Iterative Problem Solving: Agents that can make multiple function calls in sequence to solve problems
- **Applied Programming Patterns**: Environment Configuration: Using dotenv for API key management and secure credential handling, Command-Line Interface Pattern: Argument parsing with sys.argv and error handling for missing inputs, Client-Server Architecture: Initializing and using external API clients (Google Gemini) with proper error handling, Verbose Mode Implementation: Conditional output based on command-line flags for debugging and monitoring, Token Usage Tracking: Monitoring API consumption through response metadata analysis, Security-First Function Design: Path validation, working directory constraints, and input sanitization in agent functions, Defensive Programming: Comprehensive error handling with try-catch blocks and early returns for invalid states
- **Key Insight**: This lesson demonstrates that building effective AI agents isn't about training models, but about creating secure, modular function interfaces that allow pre-trained LLMs to interact safely with external systems through iterative function calling.
- **Skill Progression**: From basic Python CLI applications to building secure, modular AI agent architectures with external API integration and defensive programming practices.

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
