# /tools/analyze-lesson-concepts.md
Deeply analyze a completed lesson and extract core concepts.

**Input**: `$ARGUMENTS` - The name or number of the lesson (e.g., "L15_Debugging_Functions").

## ⚠️ CRITICAL: Assessment Guidelines

**BEFORE analyzing, review**: `.claude/commands/tools/assessment-guidelines.md`

**Key Rules**:
- ❌ NEVER use: "mastery", "expert", "advanced mastery"
- ✅ ALWAYS use: "completed successfully", "can apply", "solid understanding"
- Focus on EVIDENCE: test scores, working code, demonstrated capabilities
- Learner is LEARNING, not an expert professional

## Analysis Process

1.  **Lesson Analysis (Reinforcement)**:
    -   Thoroughly read the specified lesson's `Lesson.md` file.
    -   Identify the core **programming concepts** introduced in the lesson.
    -   Note the Vietnamese explanations and practical examples.

2.  **Source Code Analysis (Implementation Patterns)**:
    -   Analyze the corresponding `main.py` file.
    -   Identify applied **programming patterns and principles** (e.g., design patterns, algorithms, data structures, language features, architectural styles like OOP or Functional).
    -   Evaluate code structure, readability, and adherence to clean code principles.

3.  **Concept Connection Mapping**:
    -   Connect the lesson's concepts to previously learned knowledge.
    -   Identify related design patterns or broader software development principles.
    -   Note new insights regarding performance, maintainability, or scalability.

## Output Format

The agent must return a single JSON object, with no additional explanation, following this structure:

```json
{
  "lesson_name": "Lesson Name",
  "key_concepts": [
    "Concept 1: Brief explanation",
    "Concept 2: Brief explanation"
  ],
  "implementation_patterns": [
    "Pattern 1: Description of its application in the code",
    "Pattern 2: Description of its application in the code"
  ],
  "concept_connections": [
    "Connection 1: Link to a previous lesson/concept",
    "Connection 2: Relation to Design Pattern X"
  ],
  "main_learning_insight": "The most important insight gained from this lesson.",
  "skill_progression": "Brief description of skill progression using APPROVED terminology."
}
```

## ✅ Example Output (CORRECT Terminology):

```json
{
  "lesson_name": "CH3-L3: More Declarations",
  "key_concepts": [
    "FunctionDeclaration Scaling: Extending from single to multiple function toolkit",
    "Schema Type System: Understanding types.Type.STRING and types.Type.ARRAY"
  ],
  "implementation_patterns": [
    "Pattern Replication: Consistently applying FunctionDeclaration structure across 4 schemas",
    "Module Organization: Co-locating schema definitions with implementations"
  ],
  "concept_connections": [
    "Builds on CH3-L2 single FunctionDeclaration pattern",
    "Connects to OpenAPI/Swagger documentation patterns"
  ],
  "main_learning_insight": "Successfully built complete AI agent toolkit by replicating schema patterns. Quality of descriptions directly affects LLM function selection accuracy.",
  "skill_progression": "From single-function LLM integration (L2) to successfully implementing multi-function toolkit with CRUD operations. Can now apply schema patterns consistently across multiple functions."
}
```

## ❌ Example Output (WRONG Terminology - DO NOT USE):

```json
{
  "skill_progression": "From basic to advanced mastery of FunctionDeclaration. Achieved expert-level schema expertise."
}
```