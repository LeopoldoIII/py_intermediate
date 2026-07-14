# Python Intermediate Course

Just examples taken from [here](https://www.youtube.com/watch?v=HGOBQPFzWKo).

## Repository Structure

The repository is organized by topics and logical concepts to facilitate studying algorithms and preparing for interviews:

* **[01_basic_concepts](file:///Users/usermini/Local/projects/py_intermediate/01_basic_concepts/):** Control flow, recursion, loops (`for`, `range`, `enumerate`).
* **[02_data_structures](file:///Users/usermini/Local/projects/py_intermediate/02_data_structures/):** Built-in data structures (`lists`, `tuples`, `dictionaries`, `sets`, `strings`) and the `collections` module.
* **[03_functional_programming](file:///Users/usermini/Local/projects/py_intermediate/03_functional_programming/):** Lambda expressions, list comprehensions, and functional programming functions (`map`, `filter`, `reduce`).
* **[04_advanced_concepts](file:///Users/usermini/Local/projects/py_intermediate/04_advanced_concepts/):** Advanced concepts such as `closures`, `properties`, `sys` module, and `logging`.
* **[05_testing](file:///Users/usermini/Local/projects/py_intermediate/05_testing/):** Unit testing with the standard `unittest` module.
* **[06_integrations_and_scraping](file:///Users/usermini/Local/projects/py_intermediate/06_integrations_and_scraping/):** Working with JSON, HTTP requests using `requests`, and web scraping using `beautifulsoup4`.
* **[07_best_practices](file:///Users/usermini/Local/projects/py_intermediate/07_best_practices/):** Coding best practices and common bad habits to avoid in Python.
* **[08_algorithms_and_interviews](file:///Users/usermini/Local/projects/py_intermediate/08_algorithms_and_interviews/):** Practical exercises commonly found in developer interviews (duplicate search, missing numbers, word counts, target sum pairs, etc.).
* **[scripts](file:///Users/usermini/Local/projects/py_intermediate/scripts/):** Repository external utility scripts.

## Environment Setup

### 1. Install pyenv and dependencies
Ensure you have `pyenv` and library dependencies (like `xz` to avoid missing compression libraries when compiling Python) installed:

```bash
brew install pyenv xz
```

### 2. Configure your shell (Zsh)
To ensure `pyenv` is loaded automatically by your shell, run the following commands to configure Zsh (the default macOS shell):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Restart your terminal or run `source ~/.zshrc` to apply the changes.

### 3. Install Python Version
Install the Python version specified in `.python-version` (3.8.10):

```bash
pyenv install 3.8.10
```

### 4. Create and Activate Virtual Environment

Create the virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
source venv/bin/activate
```

### 5. Install Dependencies
Install the required packages using the simplified requirements file:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Troubleshooting

### Issue: Missing `_lzma` module during `pyenv install`
If you see an error warning that the `lzma` extension was not compiled:

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import lzma
  File "/Users/xxxxx/.pyenv/versions/3.14.0/lib/python3.14/lzma.py", line 28, in <module>
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'
WARNING: The Python lzma extension was not compiled. Missing the lzma lib?
```

**Fix:**
Install `xz` via Homebrew, then force reinstall the python version:

```bash
brew install xz
pyenv install <python_version> --force
```

