# /tools/update-learning-memory.md
Update the Neo4j knowledge graph with structured learning data.

**Input**: `$ARGUMENTS` - A JSON string containing the analyzed data from a lesson.

## ⚠️ CRITICAL: Assessment Guidelines

**BEFORE updating memory, review**: `.claude/commands/tools/assessment-guidelines.md`

**Key Rules for Memory Updates**:
- ❌ NEVER add observations with: "mastery", "expert", "advanced mastery"
- ✅ ALWAYS use: "completed successfully", "can apply", "solid understanding", "successfully implemented"
- All observations must be EVIDENCE-BASED (test scores, working code)
- Reflect LEARNING STAGE, not professional expertise

## Update Process

1.  **Parse Input**:
    -   Parse the input JSON string to extract information: `lesson_name`, `key_concepts`, etc.

2.  **Attempt Update with Duplication Check**:
    -   First, **try to use** the `read_neo4j_cypher` tool to check if a `Lesson` node with the same `lesson_name` already exists.
        -   **Query Example**: `MATCH (lesson:Lesson {name: $lesson_name}) RETURN lesson`
    -   **If the query succeeds and returns a result**: Stop the process and report that this lesson has already been updated.
    -   **If the query succeeds and returns no results**: Proceed to generate and execute the update queries using `write_neo4j_cypher`. After execution, verify the update and report success.

3.  **Fallback on Tool Failure**:
    -   **If any Neo4j tool call fails** (e.g., `read_neo4j_cypher` or `write_neo4j_cypher` are not available):
        a.  Clearly state that the automatic memory update failed because the required tools are not in your environment.
        b.  **Do not stop.** Instead, generate the complete set of Cypher queries that *would* have been executed.
        c.  Present these queries to the user in a formatted code block as the final output.

## Example Input JSON
```json
{
  "lesson_name": "CH3-L3: More Declarations",
  "key_concepts": [
    "FunctionDeclaration Scaling: Extending from single to multiple function toolkit"
  ],
  "implementation_patterns": [
    "Pattern Replication: Consistently applying FunctionDeclaration structure"
  ],
  "concept_connections": [
    "Builds on CH3-L2 single FunctionDeclaration pattern"
  ],
  "main_learning_insight": "Successfully built complete AI agent toolkit by replicating schema patterns.",
  "skill_progression": "From single-function integration to successfully implementing multi-function toolkit."
}
```

## ✅ Example Memory Updates (CORRECT):

**Boot_Dev_Course observations:**
```
"CH3-L3 More Declarations: Completed successfully 2025-10-01 with 4/4 test scores"
"Successfully applied: FunctionDeclaration scaling, Schema type system (STRING vs ARRAY)"
```

**Progress_Tracker observations:**
```
"Lesson CH3-L3 completed: 2025-10-01"
"Pattern understanding: Can replicate schema patterns consistently across functions"
```

**Python_Skills observations:**
```
"FunctionDeclaration: Can create types.FunctionDeclaration with Schema patterns"
"Type safety: Successfully applies explicit type declarations"
```

## ❌ Example Memory Updates (WRONG - DO NOT USE):

```
"CH3-L3: MASTERED with perfect scores"
"Achieved FunctionDeclaration expertise"
"Expert-level schema mastery"
"Advanced pattern mastery confidence VERY HIGH"
```