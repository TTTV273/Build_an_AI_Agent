# /tools/commit-learning.md
Automatically create a commit to save the learning progress.

**Input**: `$ARGUMENTS` - A JSON string containing the analyzed data from a lesson (to be used in the commit message).

## ⚠️ CRITICAL: Assessment Guidelines

**Review**: `.claude/commands/tools/assessment-guidelines.md` before creating commit messages.

**Key Rules**:
- ❌ NEVER use: "Mastered", "Expert", "Advanced mastery"
- ✅ ALWAYS use: "Completed", "Successfully applied", "Can now apply"

## Commit Process

1.  **Check Status**:
    -   Run the `git status` command to see the changed files (including the workflow, tool, and markdown documentation files just updated).

2.  **Stage Files**:
    -   Run the `git add .` command to add all changes to the staging area.

3.  **Create Commit Message**:
    -   Parse the input JSON string.
    -   Create a meaningful commit message in the Conventional Commits format, using the following template:

    ```
    📚 L[Lesson Number] Review: [Lesson Name]

    ✅ Completed: [Key Concepts]
    🔗 Connected: [Applied Programming Patterns]
    💡 Insight: [Key Insight]
    📈 Progress: [Skill Progression]

    Memory updated: Boot_Dev_Course, Progress_Tracker, [Skill_Domain]
    Next focus: [Next topics, if any]
    ```

## ✅ Example Commit Message (CORRECT):
```
📚 CH3-L3 Review: More Declarations

✅ Completed: FunctionDeclaration scaling with 4/4 test scores
🔗 Connected: Schema patterns, OpenAPI documentation
💡 Insight: Successfully built multi-function AI agent toolkit
📈 Progress: Can now apply schema patterns consistently

Memory updated: Boot_Dev_Course, Progress_Tracker, AI_Agent_Architecture
Next focus: Function execution logic, agent loops
```

## ❌ Example Commit Message (WRONG - DO NOT USE):
```
📚 CH3-L3 Review: More Declarations

✅ Mastered: FunctionDeclaration with expert-level precision
📈 Progress: Achieved advanced mastery
```

4.  **Execute Commit**:
    -   Run the `git commit -m "..."` command with the generated message.

5.  **Report**:
    -   Announce that the changes have been committed successfully.
    -   Display the output of `git log -n 1` for confirmation.