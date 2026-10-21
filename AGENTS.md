# Repository Guidelines & Agent Instructions: py_intermediate

This document establishes the architectural, pedagogical, and coding rules for the `py_intermediate` repository. All AI agents (Gemini, Antigravity, Claude, Copilot, Cursor) and contributors must strictly adhere to these instructions.

---

## 1. Repository Purpose & Scope

`py_intermediate` is an educational, hands-on repository designed to guide developers from foundational Python knowledge toward intermediate and advanced mastery. It focuses on:
- Writing idiomatic, Pythonic code.
- Mastering core and advanced data structures.
- Functional programming, generators, and decorators.
- Software design, best practices (PEP 8, SOLID), and testing.
- Preparing for technical coding interviews (algorithms and data structure challenges).

---

## 2. Universal Language Rule: English Only in Code

> **CRITICAL RULE:** All code, comments, docstrings, variable names, function names, file names, exercise descriptions, and test assertions must be written in **ENGLISH**.
>
> - Regardless of the language used to chat with the agent (e.g., if the user prompts in Spanish, French, etc.), any code produced, edited, or added to files must be in **English**.
> - Conversational explanations in the chat may follow the user's language, but repository files must maintain 100% English consistency.

---

## 3. Directory Taxonomy by Level

The repository follows a two-digit ascending numeric prefix (`XX_`) to enforce pedagogical ordering:

| Directory | Level | Description |
| :--- | :---: | :--- |
| `01_basic_concepts/` | 1 | Control flow, integer methods, string methods, recursion, loops. |
| `02_data_structures/` | 2 | Built-in structures (`list`, `tuple`, `dict`, `set`) and `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`). |
| `03_functional_programming/` | 3 | List/dict comprehensions, lambdas, `map`, `filter`, `reduce`. |
| `04_advanced_concepts/` | 4 | Generators, closures, decorators, context managers, `sys`, `logging`. |
| `05_testing/` | 5 | Unit testing with `unittest` and `pytest`, test doubles, fixtures. |
| `06_integrations_and_scraping/` | 6 | HTTP requests (`requests`), JSON serialization/deserialization, web scraping (`BeautifulSoup`). |
| `07_best_practices/` | 7 | Clean code, PEP 8, type hints, SOLID principles, guard clauses. |
| `08_algorithms_and_interviews/` | 8 | LeetCode-style technical interview problems (arrays, hashing, two pointers). |
| `09_oop/` | 9 | Classes, instance vs class attributes, dunder methods (`__str__`, `__repr__`), inheritance, polymorphism. |
| `10_concurrency_and_async/` | 10 | Multithreading, multiprocessing, and `asyncio` fundamentals. |
| `11_design_patterns/` | 11 | Creational, structural, and behavioral design patterns in Python. |
| `12_performance_and_profiling/` | 12 | `cProfile`, memory profiling, `timeit`, optimization techniques. |

---

## 4. Exercise Standard: The 3-Phase Template

Every notebook or script that contains coding challenges or practice problems—**regardless of whether it is named `<topic>.ipynb`, `<topic>_example.ipynb`, or `<topic>_exercises.ipynb`**—must strictly follow this mandatory 3-phase structure:

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
- *(Required for refactored files)* Provide a collapsible hint and official solution using:
  ```html
  <details><summary>💡 Hint</summary>...</details>
  <details><summary>🔍 Solution</summary>...</details>
  ```

> [!CAUTION]
> **No Raw Code Dumps**: Notebooks must NEVER contain raw, uncaptioned code cells without Markdown context, type hints, or test cases. When auditing or refactoring a level, agents must inspect **all** `.ipynb` files in that directory, not just those ending in `_exercises.ipynb`.

---

## 5. Development Environment & Conventions

- **Python Version**: Python 3.8+ (managed via `pyenv` and `.python-version`).
- **Virtual Environment**: `.venv` in the repository root. Always assume `.venv/bin/python` or `.venv/bin/pytest` when running tools.
- **Naming Conventions**:
  - Folders: `XX_snake_case` (e.g., `04_advanced_concepts`).
  - Python scripts: `snake_case.py`.
  - Concept notebooks: `<topic>.ipynb` (e.g., `for_loops.ipynb`, `range_enumerate.ipynb`, `recursion.ipynb`). No spelling errors!
  - Exercise notebooks: `<topic>_exercises.ipynb` or `<topic>_challenges.ipynb`.
  - Functions & variables: `snake_case`.
  - Classes: `PascalCase`.
- **Type Annotations**: Always include modern type hints (`def func(items: list[str]) -> dict[str, int]:`).
