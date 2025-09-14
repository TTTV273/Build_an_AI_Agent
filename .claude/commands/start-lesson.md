Start a new functional programming lesson: $ARGUMENTS.

Execute systematic lesson preparation for optimal learning outcomes:

## 1. LEARNING CONTEXT ASSESSMENT
Read `CLAUDE.md` to understand:
- **Current chapter progress**: Which lessons completed, current skill level
- **Recent learning insights**: Key takeaways from previous lessons  
- **Challenge areas**: Concepts that needed extra attention
- **Learning momentum**: Recent completion rate and confidence trends

## 2. OPTIMIZED MEMORY CONTEXT RETRIEVAL
Query Neo4j memory for current learning state:

### A. Programming Skills Assessment:
```cypher
MATCH (n) WHERE n.name IN [
  'Python_Skills', 'Functional_Programming', 'Recursion_Mastery', 
  'Boot_Dev_Course'
] RETURN n.observations, n.level, n.status
```

### B. Learning Environment Context:
```cypher
MATCH (n) WHERE n.name IN [
  'Developer_Productivity', 'Linux_Environment', 'Development_Tools',
  'Progress_Tracker'
] RETURN n.observations, n.status
```

### C. Recent Learning Sessions:
```cypher
MATCH (n:Learning_Session) 
WHERE n.created_date >= date().minusDays(7)
RETURN n ORDER BY n.created_date DESC LIMIT 3
```

## 3. LESSON PREPARATION ANALYSIS
Examine target lesson materials:

### A. Lesson.md Deep Analysis:
- **Core concepts**: Primary functional programming principles
- **Learning objectives**: Specific skills to master
- **Vietnamese terminology**: Technical terms with explanations
- **Prerequisite concepts**: Required knowledge from previous lessons
- **Practical applications**: Real-world coding scenarios
- **Difficulty indicators**: Complexity markers and potential challenges

### B. Implementation Requirements Analysis:
- **main.py structure**: Expected function signatures and logic flow
- **main_test.py examination**: Test cases and success criteria
- **Function complexity**: Algorithm requirements and optimization needs
- **Input/output patterns**: Data transformation expectations

## 4. PREREQUISITE VALIDATION
Verify readiness for lesson:
```python
def validate_prerequisites(lesson_number, current_skills):
    prerequisites = {
        "L14": ["higher_order_functions", "lambda_composition"],
        "L15": ["recursion_basics", "base_case_patterns"],  
        "L16": ["debugging_techniques", "test_interpretation"]
    }
    
    required = prerequisites.get(f"L{lesson_number}", [])
    missing = [skill for skill in required if skill not in current_skills]
    
    if missing:
        return f"⚠️  Review needed: {missing}"
    return "✅ Prerequisites satisfied"
```

## 5. PERSONALIZED LEARNING STRATEGY
Create tailored approach based on:

### A. Learning Style Optimization:
- **Socratic Method**: Step-by-step guided discovery preferred
- **Vietnamese Explanations**: Complex concepts in native language
- **Iterative Learning**: Learn through repeated problem-solving
- **Test-First Flow**: Understand requirements before implementation

### B. Strengths Leveraging:
- **Logical Thinking**: Use pattern recognition abilities
- **Active Learning**: Encourage questions and exploration
- **Persistence**: Build on iterative improvement mindset

### C. Challenge Area Support:
- **Syntax Fluency**: Extra attention to code structure
- **Data Flow**: Clear explanation of function pipelines
- **Return Statement Logic**: Explicit output handling

## 6. STRUCTURED LESSON INITIALIZATION

### A. Set Learning Objectives:
```markdown
## Lesson ${LESSON_NUMBER}: ${LESSON_NAME}

### 🎯 Learning Objectives:
1. **Primary**: ${MAIN_CONCEPT}
2. **Secondary**: ${SUPPORTING_CONCEPTS}
3. **Application**: ${PRACTICAL_USAGE}

### 🔧 Implementation Goals:
- [ ] Pass all test cases (${TEST_COUNT} tests)
- [ ] Apply ${KEY_PATTERN} pattern correctly
- [ ] Demonstrate understanding through code comments
- [ ] Connect to previous lesson concepts

### 🇻🇳 Vietnamese Concept Notes:
- **${TECHNICAL_TERM}**: ${VIETNAMESE_EXPLANATION}
- **Key Pattern**: ${PATTERN_EXPLANATION_VN}
```

### B. Test-Driven Development Setup:
```python
# Step 1: Run main_test.py to understand requirements
print("📋 Test Analysis:")
print("- Test cases to satisfy: ${TEST_DESCRIPTIONS}")
print("- Expected behavior: ${EXPECTED_OUTCOMES}")
print("- Input patterns: ${INPUT_TYPES}")
print("- Output requirements: ${OUTPUT_SPECIFICATIONS}")

# Step 2: Create implementation skeleton
def create_skeleton():
    """Generate function template based on test requirements"""
    return """
    def ${FUNCTION_NAME}(${PARAMETERS}):
        '''
        Vietnamese: ${FUNCTION_PURPOSE_VN}
        English: ${FUNCTION_PURPOSE_EN}
        
        Pattern: ${PATTERN_TYPE}
        Approach: ${SOLUTION_STRATEGY}
        '''
        # TODO: Implement using ${APPROACH}
        pass
    """
```

## 7. MEMORY INITIALIZATION FOR LESSON
Update Neo4j with lesson start data:

### A. Create Lesson Session Entity:
```json
{
  "name": "Learning_Session_L${LESSON_NUMBER}_$(date +%Y_%m_%d)",
  "type": "Learning_Session", 
  "lesson_focus": "${LESSON_NAME}",
  "status": "started",
  "start_date": "$(date +%Y-%m-%d)",
  "objectives": ["${LEARNING_OBJECTIVES}"],
  "challenges_expected": ["${POTENTIAL_DIFFICULTIES}"],
  "strategies_planned": ["${LEARNING_APPROACHES}"]
}
```

### B. Update Boot_Dev_Course Progress:
```json
{
  "entity": "Boot_Dev_Course",
  "add_observations": [
    "L${LESSON_NUMBER} ${LESSON_NAME}: Started $(date +%Y-%m-%d)",
    "Prerequisites validated: ${PREREQUISITE_STATUS}",
    "Learning strategy: ${PERSONALIZED_APPROACH}",
    "Expected challenges: ${CHALLENGE_AREAS}"
  ]
}
```

### C. Update Progress_Tracker:
```json
{
  "entity": "Progress_Tracker", 
  "add_observations": [
    "Lesson L${LESSON_NUMBER} initiated: $(date +%Y-%m-%d)",
    "Learning objectives set: ${OBJECTIVE_COUNT}",
    "Prerequisite gaps: ${GAPS_IDENTIFIED}",
    "Strategy customization: ${PERSONALIZATION_APPLIED}"
  ]
}
```

## 8. INTERACTIVE LEARNING KICKOFF

### A. Concept Introduction Session:
```python
def introduce_concepts():
    print("🎓 LESSON INTRODUCTION:")
    print(f"Today: {LESSON_NAME}")
    print(f"Core Concept: {MAIN_CONCEPT}")
    print(f"🇻🇳 Khái niệm chính: {CONCEPT_VIETNAMESE}")
    
    print("\n🔗 CONNECTION TO PREVIOUS LESSONS:")
    for connection in CONCEPT_CONNECTIONS:
        print(f"- {connection}")
    
    print(f"\n🎯 SUCCESS CRITERIA:")
    print(f"- All {TEST_COUNT} tests passing")
    print(f"- Pattern {KEY_PATTERN} correctly applied")
    print(f"- Code demonstrates understanding")
```

### B. Implementation Strategy Planning:
```python
def plan_implementation():
    steps = [
        "1. 📖 Analyze test requirements thoroughly",
        "2. 🔍 Identify core algorithm/pattern needed", 
        "3. 📝 Write function signature and docstring",
        "4. 🧩 Implement step-by-step with comments",
        "5. ✅ Test incrementally with main_test.py",
        "6. 🔧 Refine and optimize implementation",
        "7. 📚 Document learning insights"
    ]
    
    for step in steps:
        print(step)
```

## 9. PROGRESS DOCUMENTATION SETUP
Update `CLAUDE.md` with lesson start:
```markdown
## 📚 Lesson L${LESSON_NUMBER}: ${LESSON_NAME}
**Started**: $(date +%Y-%m-%d %H:%M)
**Status**: 🟡 In Progress

### Learning Focus:
- **Primary Concept**: ${MAIN_CONCEPT}
- **Implementation Pattern**: ${PATTERN_TYPE}
- **Vietnamese Key Terms**: ${VN_TERMINOLOGY}

### Prerequisites Validated:
- ✅ ${SATISFIED_PREREQS}
- ⚠️ ${ATTENTION_AREAS}

### Success Metrics:
- [ ] ${TEST_COUNT} tests passing
- [ ] Pattern implementation correct
- [ ] Concept connection documented
- [ ] Learning insights recorded

### Learning Strategy:
${PERSONALIZED_APPROACH_DESCRIPTION}
```

## 10. LEARNING SESSION ACTIVATION
```bash
echo "🚀 LESSON L${LESSON_NUMBER} ACTIVATED"
echo "📝 Implementation approach: ${LEARNING_STRATEGY}"  
echo "🎯 Primary objective: ${MAIN_LEARNING_GOAL}"
echo "🇻🇳 Vietnamese support: ${VN_EXPLANATION_READY}"
echo "📊 Progress tracking: INITIALIZED"
echo "💡 Ready for test-driven development!"
echo ""
echo "Next: Run 'python main_test.py' to see requirements"
```

## SUCCESS INDICATORS:
- ✅ Learning context fully assessed
- ✅ Prerequisites validated and gaps identified  
- ✅ Personalized learning strategy created
- ✅ Memory initialized with lesson start data
- ✅ Test-driven development ready
- ✅ Vietnamese explanations prepared
- ✅ Progress tracking activated

## USAGE EXAMPLES:
```bash
/start-lesson L14_Recursion_Practice
/start-lesson L15_Debugging_Functions
/start-lesson L16_Date_Sorting
```
