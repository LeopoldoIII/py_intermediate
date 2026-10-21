# Code Style & Quality Standards

## 0. Mandatory Language Standard
- **ALL Code in English**: All source code, class names, function names, variable names, constants, docstrings, inline comments, log messages, and error messages MUST be written strictly in **English**.
- **Exercise Descriptions & Asserts in English**: All markdown instructions, task descriptions, and test assertions in notebooks MUST be written in **English**.
- **User Prompt Independence**: Even when user instructions, requests, or questions are in Spanish (or any other language), **all generated or modified code and documentation in the repository must be strictly in English**. Explanations in the chat can be in the user's preferred language, but project files must remain 100% English.

## Python Conventions

1. **Naming Conventions**:
   - **Functions & Variables**: `snake_case` (e.g., `calculate_min_bits`, `total_seconds`).
   - **Classes**: `PascalCase` (e.g., `EmployeeManager`, `DataProcessor`).
   - **Constants**: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_BUFFER_SIZE`).
   - **Files**: `snake_case.py` or `snake_case.ipynb`.

2. **Type Annotations**:
   - Always include modern Python 3.8+ type hints on function signatures:
     ```python
     def filter_even_numbers(items: list[int]) -> list[int]:
     ```
   - Use built-in generics (`list[str]`, `dict[str, int]`, `tuple[int, ...]`) or `typing.Union`, `typing.Optional` where needed.

3. **Clean Code & Idiomatic Python**:
   - Follow PEP 8 guidelines.
   - Prefer comprehensions and generator expressions over manual loop accumulators where readability allows.
   - Avoid antipatterns like `for i in range(len(items)):`; use `for index, item in enumerate(items):`.
   - Use guard clauses to exit early and reduce nesting depth.
