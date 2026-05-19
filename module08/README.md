# The Matrix — module08

## 📚 Index
1. [Summary](#summary)
2. [Overall architecture](#overall-architecture)
3. [Exercise 0 — Construct (ex0)](#exercise-0---construct-ex0)
4. [Exercise 1 — Loading & dependencies (ex1)](#exercise-1---loading--dependencies-ex1)
5. [Exercise 2 — Oracle & configuration (ex2)](#exercise-2---oracle--configuration-ex2)
6. [How to run and check](#how-to-run-and-check)
7. [Design decisions](#design-decisions)

---

## 🎯 Summary

This module explores practical topics: virtual environments, dependency
management and secure configuration loading via `.env`. Each exercise is
self-contained and includes execution instructions inside its folder.

---

## 🏗️ Overall architecture

- `module08/ex0`: utility to detect whether the program runs inside a virtual
  environment and display relevant paths.
- `module08/ex1`: example of data loading/analysis using `numpy` and, when
  available, `pandas`/`matplotlib`; includes `requirements.txt` and
  `pyproject.toml`.
- `module08/ex2`: demonstrates loading environment variables with
  `python-dotenv`, basic configuration validation and security checks; includes
  `.env.example`.

---

## Exercise 0 — Construct (ex0)

### 🎯 Goal

Detect whether the code runs inside a virtual environment and provide useful
information (Python executable, environment path, estimated site-packages) and
instructions for creating/activating a virtual environment.

### 🔧 Implemented

- `ex0/construct.py`: functions `in_virtualenv()`, `site_packages_path()` and
  user-friendly output routines that clearly differentiate global vs virtual
  environments.

### 🧭 Usage

```bash
python module08/ex0/construct.py
```

---

## Exercise 1 — Loading & dependencies (ex1)

### 🎯 Goal

Simulate a data loading and analysis flow that runs without failing when some
dependencies are missing, and display installation instructions for `pip` and
`poetry`.

### 🔧 Implemented

- `ex1/loading.py`: runtime dependency checks, data simulation with `numpy`, a
  `DataFrame` when `pandas` is present, and a generated plot when `matplotlib`
  is available.
- `ex1/requirements.txt` and `ex1/pyproject.toml`: files documenting the
  dependencies.

### 🧭 Usage

```bash
python module08/ex1/loading.py
# if some dependency is missing:
pip install -r module08/ex1/requirements.txt
```

---

## Exercise 2 — Oracle & configuration (ex2)

### 🎯 Goal

Demonstrate reading sensitive configuration via environment variables and from
a `.env` file, show differing behavior for `development` vs `production` modes,
and warn about safe practices (do not commit `.env`).

### 🔧 Implemented

- `ex2/oracle.py`: loads `.env` when `python-dotenv` is installed, reads the
  variables `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL` and
  `ZION_ENDPOINT`, and prints a summary with basic security checks.
- `.env.example` and `.gitignore` included to help safe usage.

### 🧭 Usage

```bash
# copy and edit the example file
cp module08/ex2/.env.example module08/ex2/.env
python module08/ex2/oracle.py
```

---

## How to run and check

1. Install checking tools (optional):

```bash
python3 -m pip install --user flake8 mypy
```

2. Static checks (from repository root):

```bash
mypy module08
flake8 module08 --max-line-length=79
```

3. Run examples:

```bash
python3 module08/ex0/construct.py
python3 module08/ex1/loading.py
python3 module08/ex2/oracle.py
```

---

## Design decisions

- Runtime dependency checks in `ex1` allow the exercise to run in restricted
  environments without requiring immediate installation.
- Conditional typing (`TYPE_CHECKING`) is used for optional imports (for
  example `pandas`) that are only needed for annotations, keeping `mypy`
  satisfied.
- `.env` should be listed in `.gitignore`; an `.env.example` file is provided to
  instruct users not to commit credentials.
