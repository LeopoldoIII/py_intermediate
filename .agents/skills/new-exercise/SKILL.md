---
name: new-exercise
description: >-
  Use this skill whenever the user asks to generate, scaffold, or format new exercises,
  challenges, or practice notebooks, OR to add/insert a new practice challenge or section
  into an existing notebook in this repository. Enforces English code, objective markdown,
  code samples, and unanswered practice challenges with automated assert validations.
---

# New Exercise Generator & Challenge Insertion Skill

This skill enforces the official pedagogical standard for generating Python exercises and inserting new challenges into existing notebooks in `py_intermediate`.

---

## Instructions for the Agent

Always adhere to the repository standards:
1. **Language**: Write all code, comments, docstrings, prompts, and markdown explanations strictly in **English**.
2. **Structure**: Follow the 3-phase layout:
   - **Phase 1 (Objective)**: Markdown header with `### 🎯 Objective`.
   - **Phase 2 (Sample)**: `### 📖 1. Code Sample` containing runnable demonstration code.
   - **Phase 3 (Challenge)**: `### 💻 Practice Challenge (Your Turn)` containing an uncompleted function with `# YOUR CODE HERE` and automated `assert` validation statements.
   - **Pistas y Solución**: Collapsible `<details><summary>💡 Hint</summary>` and `<details><summary>🔍 Solution</summary>`.
3. **Type Hints**: Include modern type annotations on function parameters and return types.
4. **Auto-validation**: Provide at least 3 distinct test assertions, including at least one edge case (e.g., empty collection, zero, negative number).

---

## Operating Modes

### Mode 1: Creating a New Notebook / Topic
When the user requests a new notebook or exercise file:
- Create the `.ipynb` with the standard notebook structure (Title $\rightarrow$ Objective $\rightarrow$ Code Sample $\rightarrow$ Practice Challenge with asserts $\rightarrow$ Collapsible Hint & Solution).

### Mode 2: Adding / Inserting a Challenge into an Existing Notebook
When the user asks to add an extra practice challenge to an existing section or notebook:
1. **Inspect Existing Cells**: Read the destination `.ipynb` JSON and locate the target section.
2. **Preserve Existing Content**: Do not overwrite or delete previous cells.
3. **Insert Challenge Cells**: Insert the 3-cell challenge block directly after the previous challenge's solution:
   - Cell 1 (Markdown): `### 💻 Practice Challenge N: [Title] (Your Turn)` with instructions and constraints.
   - Cell 2 (Code): Function boilerplate with type hints, `# YOUR CODE HERE`, and automated `assert` test cases.
   - Cell 3 (Markdown): Collapsible `<details><summary>💡 Hint</summary>` and `<details><summary>🔍 Solution</summary>`.
4. **Validate**: Run the test assertions of both previous and new challenges using `.venv/bin/python` to ensure zero regressions.

---

## Exercise Template Reference

````markdown
### 💻 Practice Challenge: [Title] (Your Turn)

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

<details>
<summary>🔍 Solution</summary>

```python
def solve_problem(param1: int, param2: list[str]) -> bool:
    # Official reference implementation
    ...
```
</details>
````
