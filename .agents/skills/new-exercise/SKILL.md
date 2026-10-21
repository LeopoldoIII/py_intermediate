---
name: new-exercise
description: >-
  Use this skill whenever the user asks to generate, scaffold, or format new exercises,
  challenges, or practice notebooks in this repository. Enforces English code, objective markdown,
  code samples, and unanswered practice challenges with automated assert validations.
---

# New Exercise Generator Skill

This skill enforces the official pedagogical standard for generating Python exercises in `py_intermediate`.

## Instructions for the Agent

When generating any new exercise or practice notebook, always follow these rules:

1. **Language**: Write all code, comments, docstrings, prompts, and markdown explanations strictly in **English**.
2. **Structure**: Follow the 3-phase layout:
   - **Phase 1 (Objective)**: Markdown header with `### 🎯 Objective`.
   - **Phase 2 (Sample)**: `### 📖 1. Code Sample` containing runnable demonstration code.
   - **Phase 3 (Challenge)**: `### 💻 2. Practice Challenge (Your Turn)` containing an uncompleted function with `# YOUR CODE HERE` and automated `assert` validation statements.
3. **Type Hints**: Include modern type annotations on function parameters and return types.
4. **Auto-validation**: Provide at least 3 distinct test assertions, including at least one edge case (e.g., empty collection, zero, negative number).

---

## Exercise Template Reference

````markdown
# [Topic Name]: [Exercise Title]

### 🎯 Objective
A concise 2-4 sentence overview in English explaining the concept being practiced and its significance in Python software engineering.

---

### 📖 1. Code Sample (Demonstration)
```python
# Demonstrates how the concept/method works
from typing import Any

# Example code here
```

---

### 💻 2. Practice Challenge (Your Turn)

**Instructions:**
Detailed problem statement with inputs, expected output, and edge case expectations.

```python
def solve_problem(param1: int, param2: list[str]) -> bool:
    """
    Brief docstring describing expected behavior.
    """
    # ==========================================
    # YOUR CODE HERE
    # ==========================================
    pass


# 🧪 Automated Test Cases
assert solve_problem(...) == ...
assert solve_problem(...) == ...
assert solve_problem(...) == ...
print("✅ All test cases passed successfully!")
```

<details>
<summary>💡 Hint</summary>
A brief clue to help the learner without giving away the direct solution.
</details>
````

---

## Notebook (.ipynb) Generation Notes
When creating `.ipynb` files:
- Cell 1: Markdown (Title + Objective)
- Cell 2: Markdown (Code Sample header)
- Cell 3: Code (Runnable demonstration)
- Cell 4: Markdown (Practice Challenge header + instructions)
- Cell 5: Code (Unanswered exercise boilerplate + assert tests)
- Cell 6: Markdown (Collapsible hint)
