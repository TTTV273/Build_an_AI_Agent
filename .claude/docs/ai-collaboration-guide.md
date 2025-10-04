# AI Collaboration Guide: Claude Code + Gemini CLI

## 🎯 Overview

This project leverages TWO AI assistants for optimal development workflow:
- **Claude Code** (via Claude.ai/code)
- **Gemini CLI** (via `gemini -p "{prompt}"`)

## 📊 Comparison Matrix

| Feature | Claude Code | Gemini CLI |
|---------|-------------|------------|
| **Context Window** | 200K tokens | **1M tokens** (5x larger!) |
| **Tool Integration** | ✅ Excellent (MCP, Neo4j, Git, etc.) | ⚠️ Standard CLI tools |
| **File Operations** | ✅ Read, Write, Edit, Glob, Grep | ⚠️ Via bash commands |
| **Code Quality** | ✅ Production-ready implementations | ✅ Good code generation |
| **Memory System** | ✅ Neo4j MCP integration | ❌ No persistent memory |
| **Best For** | Structured tasks, workflows, commits | Large codebase analysis, complex reasoning |
| **Interface** | Web-based chat | CLI-based (`gemini -p "..."`) |
| **Learning Style** | ✅ Socratic method support | ✅ Educational responses |

## 🚀 Usage Patterns

### When to Use Claude Code (Default)

✅ **File Operations**:
- Reading/writing/editing files
- Complex file searches (Glob, Grep)
- Git operations (commit, push, PR)

✅ **Structured Workflows**:
- Slash commands execution
- Memory updates (Neo4j MCP)
- Multi-step task orchestration

✅ **Quality Control**:
- Code reviews
- Production-ready implementations
- Following project conventions

### When to Use Gemini CLI

✅ **Large Context Analysis**:
```bash
# Example: Analyze entire codebase (when context > 200K tokens)
gemini -p "Analyze the entire codebase in /path/to/project and identify architectural patterns"
```

✅ **Complex Reasoning**:
```bash
# Example: Deep architectural analysis
gemini -p "Compare the function calling patterns in main.py with industry best practices for AI agents"
```

✅ **Large File Processing**:
```bash
# Example: Process large log files
gemini -p "Analyze this 50K line log file and identify error patterns: $(cat large.log)"
```

## 💡 Collaboration Patterns

### Pattern 1: Context Overflow Delegation

**Scenario**: Claude Code hits context limit (approaching 200K tokens)

**Solution**:
```bash
# Claude delegates complex analysis to Gemini
gemini -p "Analyze all Python files in CH1-CH3 directories and summarize function calling patterns. Return a concise summary (<2000 tokens)."
```

**Then**: Claude processes Gemini's summary and continues workflow

### Pattern 2: Two-Stage Analysis

**Stage 1 (Gemini)**: Deep analysis with large context
```bash
gemini -p "Read all lesson files in CH3-Function_Calling/ and create a dependency graph of concepts. Output as JSON."
```

**Stage 2 (Claude)**: Structured action based on analysis
```
Claude reads Gemini's JSON output → Updates memory → Creates commits
```

### Pattern 3: Parallel Workflows

**Claude**: Handles immediate file operations
**Gemini (background)**: Performs deep analysis in parallel

```bash
# Gemini runs analysis in background
gemini -p "Analyze code quality across entire project and generate report" > /tmp/gemini-analysis.txt &

# Claude continues with current task
# Later, Claude reads /tmp/gemini-analysis.txt for insights
```

## 🔧 Gemini CLI Usage Examples

### Basic Interaction
```bash
gemini -p "Your prompt here"
```

### With File Context
```bash
gemini -p "Analyze this code: $(cat main.py)"
```

### With Multiple Files
```bash
gemini -p "Compare these implementations: File1: $(cat file1.py) File2: $(cat file2.py)"
```

### Complex Analysis
```bash
gemini -p "Given this codebase structure: $(tree -L 3), recommend an optimal testing strategy"
```

## ⚠️ Limitations & Considerations

### Gemini CLI Limitations:
- ❌ No persistent memory (each call is stateless)
- ❌ No MCP tool integration
- ❌ No direct file modification capabilities
- ❌ Slower for iterative file operations
- ⚠️ Output limited to terminal (need to capture manually)

### Claude Code Limitations:
- ❌ Smaller context window (200K vs 1M)
- ❌ Can struggle with very large codebases
- ⚠️ Token budget needs careful management

## 📝 Best Practices

### 1. Default to Claude Code
Start with Claude Code for all tasks. Only delegate to Gemini when:
- Context > 150K tokens
- Need to analyze 20+ files simultaneously
- Complex architectural reasoning required

### 2. Capture Gemini Output
Always save Gemini output to files for Claude to process:
```bash
gemini -p "Analysis prompt" > /tmp/gemini-output.txt
```

### 3. Use Gemini for Summarization
When approaching token limits:
```bash
# Gemini summarizes large context
gemini -p "Summarize this 100K token conversation in 5K tokens: ..."

# Claude continues with summary
```

### 4. Structured Prompts for Gemini
Request specific output formats:
```bash
gemini -p "Analyze codebase and output as JSON with structure: {patterns: [], insights: [], recommendations: []}"
```

## 🎯 Example Workflow: Large Lesson Review

### Scenario: Review all 20 lessons in CH1-CH4 (exceeds 200K tokens)

**Step 1 (Gemini)**: Analyze all lessons
```bash
gemini -p "Read all Lesson.md files in CH1-CH4. Create a JSON summary with: lesson_name, key_concepts, dependencies, difficulty_level. Output ONLY valid JSON." > /tmp/all-lessons.json
```

**Step 2 (Claude)**: Process and document
```
Claude reads /tmp/all-lessons.json
→ Updates CLAUDE.md with consolidated summary
→ Updates Neo4j memory
→ Creates git commit
```

## 📊 Performance Metrics

Based on usage patterns:

| Task Type | Claude Speed | Gemini Speed | Winner |
|-----------|--------------|--------------|--------|
| Single file edit | ⚡ Fast (2s) | 🐌 Slow (10s) | **Claude** |
| Read 50 files | ❌ Impossible (context limit) | ⚡ Fast (15s) | **Gemini** |
| Git commit | ⚡ Fast (5s) | ❌ Manual | **Claude** |
| Architectural analysis | ⚠️ Limited context | ⚡ Comprehensive | **Gemini** |
| Memory update | ⚡ MCP tools | ❌ No integration | **Claude** |

## 🔮 Future Enhancements

Potential improvements to collaboration:
- [ ] Create helper scripts: `./scripts/ask-gemini.sh`
- [ ] Automated context splitting (Claude → Gemini when > 150K)
- [ ] Gemini response caching system
- [ ] Hybrid analysis reports (Gemini insights + Claude formatting)

## 📚 Related Documentation

- `.claude/commands/` - Claude Code slash commands
- `.gemini/commands/` - Gemini workflow commands (TOML format)
- `CLAUDE.md` - Claude-specific learning documentation
- `GEMINI.md` - Gemini-specific project overview

---

**Philosophy**:
> "Use the right tool for the right job. Claude Code for structured workflows and file operations, Gemini for deep analysis with massive context."

**Created**: 2025-10-04
**Last Updated**: 2025-10-04
