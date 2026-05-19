# Module 06: Alchemy Suite — Abstract Patterns and Composition

## 📚 Index
1. [Summary](#summary)
2. [Repository Structure](#repository-structure)
3. [Core Components](#core-components)
4. [How to Run](#how-to-run)
5. [Static Checks](#static-checks)
6. [Design Decisions](#design-decisions)
7. [Common Issues & Fixes](#common-issues--fixes)
8. [Next Steps](#next-steps)

---

## 🎯 Summary

Module 06 (Alchemic Suite) demonstrates composition, modular design and clear separation of concerns across
several small tools: element definitions, potion recipes, transmutation and other helper scripts. The codebase
is organized to be readable, type annotated, and compatible with static analysis tools (`mypy`, `flake8`).

---

## 🗂️ Repository Structure (high level)

```
module06/
  elements.py
  ft_alembic_0.py
  ft_alembic_1.py
  ft_alembic_2.py
  ft_alembic_3.py
  ft_alembic_4.py
  ft_alembic_5.py
  ft_distillation_0.py
  ft_distillation_1.py
  ft_kaboom_0.py
  ft_kaboom_1.py
  ft_transmutation_0.py
  ft_transmutation_1.py
  ft_transmutation_2.py
  alchemy/
    __init__.py
    elements.py
    potions.py
    grimoire/
      __init__.py
      dark_spellbook.py
      dark_validator.py
      light_spellbook.py
      light_validator.py
    transmutation/
      __init__.py
      recipes.py
```

The `alchemy` package contains core domain logic: element constants, potion definitions and recipe collections.
Top-level scripts (`ft_*`) are exercise examples or feature demos used for teaching/validation.

---

## ⚙️ Core Components

- `module06/elements.py` — central element definitions used by multiple scripts.
- `module06/alchemy/elements.py` — package-scoped element utilities and mappings.
- `module06/alchemy/potions.py` — potion classes and behaviors.
- `module06/alchemy/transmutation/recipes.py` — transmutation recipes and helpers.
- `module06/alchemy/grimoire/*` — spellbooks and validators demonstrating modular validation patterns.

Standalone scripts `ft_alembic_*`, `ft_transmutation_*`, `ft_distillation_*` implement small exercises
that consume package logic to show examples and can be executed directly for quick validation.

---

## ▶️ How to Run

Examples (from repository root):

```bash
python3 module06/ft_alembic_0.py

# run test/demonstration scripts
python3 module06/ft_transmutation_0.py
python3 module06/ft_distillation_1.py
```

Each `ft_*.py` script is short and prints the example behavior — run them to inspect outputs and validate
logical behavior quickly.

---

## 🔍 Static Checks

Recommended local checks (optional but encouraged):

```bash
python3 -m pip install --user flake8 mypy
mypy module06
flake8 module06 --max-line-length=79
```

Run these commands from the repository root to ensure import resolution is consistent and to avoid
``Source file found twice under different module names`` errors.

---


