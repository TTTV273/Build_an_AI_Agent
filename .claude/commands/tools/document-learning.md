# /tools/document-learning.md
Update learning documentation files (e.g., CLAUDE.MD, GEMINI.MD) with a structured summary of a completed lesson.

**Input**: `$ARGUMENTS` - A JSON string containing the analyzed data from a lesson.

## Documentation Update Process

1.  **Parse Input**:
    -   Parse the input JSON string to extract the necessary information.

2.  **Format Summary**:
    -   Create a Markdown string from the JSON data, using the following format:

    ```markdown
    ### 📝 Lesson Summary: ${lesson_name}

    -   **Lesson Focus**: ${key_concepts}
    -   **Applied Programming Patterns**: ${implementation_patterns}
    -   **Key Insight**: ${main_learning_insight}
    -   **Skill Progression**: ${skill_progression}
    ```

3.  **Identify Target File**:
    -   Identify the main documentation file to update. Defaults to `CLAUDE.MD`.

4.  **Execute Update**:
    -   Use `read_file` to read the current content of the target file.
    -   Append the formatted Markdown string to the end of the file's content.
    -   Use `write_file` to write the entire updated content back to the file.
    -   **Important**: Ensure you only append to the file; do not overwrite or delete old content.

5.  **Report**:
    -   Announce that the documentation file has been updated successfully.