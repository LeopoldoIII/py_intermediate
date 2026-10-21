# Repository Architecture & Hierarchy

## 1. Directory Taxonomy by Level
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

## 2. Naming Conventions
- Folders: `XX_snake_case` (e.g., `04_advanced_concepts`).
- Python scripts: `snake_case.py`.
- Concept notebooks: `<topic>.ipynb` (e.g., `for_loops.ipynb`, `range_enumerate.ipynb`, `recursion.ipynb`). No spelling errors!
- Exercise notebooks: `<topic>_exercises.ipynb` or `<topic>_challenges.ipynb`.

## 3. Environment & Tools
- Python 3.8+ managed via `pyenv`.
- Virtual environment in root `.venv/`. Always use `.venv/bin/python` or `.venv/bin/pytest`.
