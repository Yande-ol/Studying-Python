# Module 10: Lambda & Decorators — Functional Magic & Metaprogramming

## 📚 Index
1. [Core Concepts](#core-concepts)
2. [Exercise 0 - Lambda Spells](#exercise-0---lambda-spells)
3. [Exercise 1 - Spell Timer](#exercise-1---spell-timer)
4. [Exercise 2 - Retry Decorator](#exercise-2---retry-decorator)
5. [Exercise 3 - Functools Artifacts](#exercise-3---functools-artifacts)
6. [Exercise 4 - Decorator Mastery](#exercise-4---decorator-mastery)
7. [How to Use This Module](#how-to-use-this-module)

---

## 🎯 Core Concepts

This module focuses on functional programming patterns and advanced decorator techniques in Python. You will practice:

- **Lambda functions**: writing concise anonymous functions for simple transformations and filtering.
- **Higher-order functions**: using `map()`, `filter()`, and `reduce()` to process collections functionally.
- **Decorators**: wrapping functions to add behavior (logging, timing, validation, retry logic).
- **Functools utilities**: leveraging `wraps`, `partial`, `lru_cache`, and `singledispatch` for elegant code.
- **Metaprogramming**: modifying function signatures and behavior at runtime.

Key ideas:

- **Pure functions**: functions that avoid side effects and always return the same output for the same input.
- **Function composition**: building complex behavior by chaining simpler functions together.
- **Lazy evaluation**: using lambdas and generators to defer computation until needed.
- **Decorator patterns**: creating reusable wrappers for cross-cutting concerns (timing, validation, error handling).

---

## ✨ Exercise 0 - Lambda Spells

### 🎯 Goal
Master lambda functions and functional transformations using `map()`, `filter()`, and `reduce()`.

### 📋 Operations

```
spells = ['fireball', 'lightning', 'heal']

Transformations:
- uppercase_spells: map(lambda x: x.upper(), spells)
- long_spells: filter(lambda x: len(x) > 6, spells)
- concatenate_spells: reduce(lambda acc, x: acc + x, spells)
```

### 🔍 Notes

- Use lambda for simple, one-line transformations only.
- Combine `map()` and `filter()` to process sequences functionally.
- Use `functools.reduce()` to aggregate collections into a single value.
- Keep lambdas readable; if logic becomes complex, define named functions instead.

---

## ⏱️ Exercise 1 - Spell Timer

### 🎯 Goal
Create a `spell_timer` decorator that measures and reports execution time of any function.

### 📋 Decorator Pattern

```
@spell_timer
def fireball():
    # do work
    return 'Fireball cast!'

# Output:
# Casting fireball...
# Spell completed in 0.101 seconds
# Result: Fireball cast!
```

### 🔍 Notes

- Use `functools.wraps` to preserve the original function's metadata.
- Use `time.perf_counter()` for accurate timing measurements.
- Print timing info to `stdout` before returning the result.
- Support both positional and keyword arguments using `*args` and `**kwargs`.

---

## 🔄 Exercise 2 - Retry Decorator

### 🎯 Goal
Build a `retry_spell` decorator that automatically retries a function on failure up to a maximum number of attempts.

### 📋 Decorator Pattern

```
@retry_spell(max_attempts=3)
def flaky():
    raise RuntimeError('boom')

# Output:
# Spell failed, retrying... (attempt 1/3)
# Spell failed, retrying... (attempt 2/3)
# Spell casting failed after 3 attempts
```

### 🔍 Notes

- Accept `max_attempts` as a parameter to the decorator.
- Catch all exceptions raised by the function and retry.
- Print retry progress to `stdout` for each failed attempt.
- Return a failure message if all attempts are exhausted.
- Stop early if the function succeeds on any attempt.

---

## 🛠️ Exercise 3 - Functools Artifacts

### 🎯 Goal
Explore `functools` utilities: `partial`, `lru_cache`, `singledispatch`, and `reduce()` with various operators.

### 📋 Components

```
Operations:
- Partial application: create specialized functions from general ones
- Caching: memoize expensive computations with @lru_cache
- Single dispatch: define type-specific behavior with @singledispatch
- Reduce chains: apply operators (add, mul, max, min) over sequences
```

### 🔍 Notes

- `partial()` creates a new function with preset arguments; useful for callbacks.
- `@lru_cache(maxsize=128)` memoizes results; speeds up repeated calls with same args.
- `@singledispatch` allows function overloading based on the first argument's type.
- `reduce()` requires explicit operator import; be cautious with type mixing (int vs float).

---

## 🧙 Exercise 4 - Decorator Mastery

### 🎯 Goal
Combine multiple decorators to build a complete spell-casting system with validation, timing, and retry logic.

### 📋 Components

```
@spell_timer
def fireball():
    sleep(0.101)
    return 'Fireball cast!'

@retry_spell(max_attempts=3)
def flaky():
    raise RuntimeError('boom')

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        # Validate name constraints (length, characters)
        pass

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        # Cast spell only if power exceeds threshold
        pass
```

### 🔍 Notes

- Stack decorators to compose behavior; execution order is bottom-to-top.
- `power_validator` should check power level and return an error message if insufficient.
- `spell_timer` should wrap the function and measure execution time.
- All decorators must preserve the wrapped function's signature using `functools.wraps`.
- Static methods and instance methods can both be decorated; handle argument extraction carefully.

---

## 🧭 How to Use This Module

### Prerequisites

- Python 3.10+ recommended.
- No external dependencies required (uses only Python standard library).

### Running the Example Scripts

Each exercise provides a script entrypoint. Run them directly to see demo scenarios:

```bash
python3 module10/ex0/lambda_spells.py
python3 module10/ex1/spell_timer.py
python3 module10/ex2/retry_decorator.py
python3 module10/ex3/functools_artifacts.py
python3 module10/ex4/decorator_mastery.py
```

If a script lacks a demo, import the functions or classes interactively:

```bash
python3 -c "from module10.ex0.lambda_spells import uppercase_spells; print(uppercase_spells(['fireball', 'heal']))"
```

### Validation

This project uses `flake8` for style checking and `mypy` for type safety. Run validation from the workspace root:

```bash
flake8 module10
mypy module10
```

Expected output: no errors, all files passing checks.

