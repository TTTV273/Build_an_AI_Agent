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

## User Learning Preferences

- **Learning Method**: Socratic method preferred - act as a guide with questions to help arrive at solutions, rather than implementing directly
- **Language**: Vietnamese preferred for communication
- **Interaction Pattern**: Iterative workflow with frequent validation after each small change
- **Effective Techniques**: Guided questions, analogies, breaking down complex problems into smaller concrete steps
- **Challenge Areas**: Structuring control flow (if/else logic) and combining multiple logical steps may require detailed guidance

## AI Collaboration Strategy

This project uses **TWO AI assistants** for optimal workflow:

### Claude Code (Primary - You!)
- **Context**: 200K tokens
- **Best for**: File operations, Git workflows, structured tasks, MCP/Neo4j integration
- **Usage**: Default for all development tasks

### Gemini CLI (Secondary - Large Context)
- **Context**: 1M tokens (5x larger!)
- **Best for**: Large codebase analysis, complex reasoning, multi-file processing
- **Usage**: `gemini -p "{prompt}"`

### When to Delegate to Gemini:
1. **Context overflow**: When approaching 150K+ tokens
2. **Large analysis**: Need to analyze 20+ files simultaneously
3. **Deep reasoning**: Complex architectural decisions requiring massive context

### Example Delegation:
```bash
# Gemini analyzes large context
gemini -p "Analyze all Python files in CH1-CH3 and summarize patterns" > /tmp/analysis.txt

# Claude processes result
# Read /tmp/analysis.txt and continue with structured workflow
```

**Full Guide**: See `.claude/docs/ai-collaboration-guide.md` for detailed patterns and examples.

## Slash Commands Workflow

### Main Commands

#### `/start-lesson` - Initialize new lesson
```bash
/start-lesson CH3-Function_Calling/L4-Execute_Functions/Lesson.md
```
Use before starting to code. Analyzes requirements, test cases, and prepares implementation skeleton.

#### `/lesson-review` - Complete lesson (All-in-One) ⭐
```bash
/lesson-review CH3-L3_More_Declarations
```
Use after passing ALL tests. Automatically:
1. Analyzes lesson → Creates JSON
2. Updates CLAUDE.md with summary
3. Updates Neo4j memory
4. Creates git commit

### Individual Tools (Advanced)

For step-by-step control:
```bash
/tools:1-analyze-lesson-concepts {LESSON_NAME}
/tools:2-document-learning {JSON}
/tools:3-update-learning-memory {JSON}
/tools:4-commit-learning {JSON}
```

### Assessment Guidelines

**CRITICAL**: Read `.claude/commands/tools/assessment-guidelines.md` before using any command.

**Approved Terminology**:
- ✅ "Completed successfully", "Successfully implemented/applied"
- ✅ "Can apply/implement/create"
- ✅ "Solid understanding", "Good/strong grasp"

**Forbidden Terminology**:
- ❌ "Mastery/Mastered", "Expertise/Expert"
- ❌ "Advanced mastery", "Expert level"

**Philosophy**: Passing tests = Learning + Application, NOT Mastery. Mastery requires years of experience.

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

### 📝 Lesson Summary: CH3-L3: More Declarations - Expanding AI Agent Toolkit

- **Lesson Focus**: FunctionDeclaration Scaling: Extending AI agent capabilities from single function to multiple function toolkit through consistent schema patterns, Schema Type System: Mastering types.Type.STRING for simple parameters and types.Type.ARRAY with items declaration for list parameters, Security by Design: Systematic hiding of working_directory parameter across all function schemas to maintain sandbox boundary control, Optional Parameter Communication: Using description conventions ('If not provided...') to indicate optional parameters without explicit required field in Gemini API, LLM Function Selection: Understanding how LLM uses function descriptions and parameter schemas to autonomously choose appropriate function based on natural language user intent
- **Applied Programming Patterns**: Pattern Replication: Consistent FunctionDeclaration structure (name, description, parameters.properties) applied across all 4 schemas for maintainability, Module Organization: Separate schema definitions co-located with function implementations in individual module files (get_file_content.py, run_python_file.py, write_file.py), Tool Registry Pattern: Centralized types.Tool with function_declarations list enabling plugin-like architecture for function registration, System Instruction Layer: Separation of API documentation (schemas) from behavioral guidance (system_prompt) following separation of concerns principle, Professional API Documentation Style: Concise, passive-voice descriptions focusing on 'what' (functionality) not 'why' (implementation rationale), Type Safety: Explicit type declarations (STRING, ARRAY) with nested items schema for array element types ensuring type-safe LLM parameter generation
- **Key Insight**: Building effective AI agents requires clear separation between LLM decision-making (through comprehensive function schemas) and Python execution control (through hidden security parameters). The quality of schema descriptions directly determines LLM's ability to autonomously select correct functions - professional, concise documentation is not just good practice but functional requirement for agent intelligence.
- **Skill Progression**: From single-function LLM integration (L2) to complete multi-function AI agent toolkit with CRUD operations. Successfully applied schema type system (STRING vs ARRAY with items), pattern replication across multiple function declarations, and professional API documentation standards. Can now think in security-first design patterns by consistently hiding sensitive parameters across all schemas.