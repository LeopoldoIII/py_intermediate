# Exercise Standards & Template

Every notebook or script that contains coding challenges or practice problems—**regardless of whether it is named `<topic>.ipynb`, `<topic>_example.ipynb`, or `<topic>_exercises.ipynb`**—must strictly follow this mandatory 3-phase structure:

## 1. The 3-Phase Template

### Phase 1: Objective & Context (Markdown Header)
Explain clearly in English:
- What concept is being covered.
- Why it is useful in real-world / professional Python development.
- What the expected learning outcome is.

### Phase 2: Working Code Sample (Demonstration)
Provide a clear, self-contained, and runnable demonstration showing the idiomatic syntax or pattern in action.

### Phase 3: Practice Challenge (Unanswered with Validation)
- State the problem clearly with input/output constraints.
- Provide a boilerplate function with explicit Type Hints (`def func(param: int) -> str:`) and `# YOUR CODE HERE` or `pass`.
- **Must include automated test cases (`assert`)** at the bottom of the cell/script so the user receives immediate validation upon completing their implementation.
- Provide a collapsible hint and official solution using:
  ```html
  <details><summary>💡 Hint</summary>...</details>
  <details><summary>🔍 Solution</summary>...</details>
  ```

## 2. Quality Constraints

- **No Raw Code Dumps**: Notebooks must NEVER contain raw, uncaptioned code cells without Markdown context, type hints, or test cases.
- **Edge Cases in Tests**: Automated asserts must cover standard inputs and at least one boundary/edge case (e.g., empty collection `[]`, `0`, or negative value).
