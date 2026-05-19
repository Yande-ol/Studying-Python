# DataDeck — module07: Abstract Card Architecture

## 📚 Índice
1. [Resumo](#resumo)
2. [Arquitetura geral](#arquitetura-geral)
3. [Exercise 0 — Creature Factory (ex0)](#exercise-0---creature-factory-ex0)
4. [Exercise 1 — Capabilities (ex1)](#exercise-1---capabilities-ex1)
5. [Exercise 2 — Abstract Strategy (ex2)](#exercise-2---abstract-strategy-ex2)
6. [Como rodar e checar](#como-rodar-e-checar)
7. [Decisões de design](#decisoes-de-design)
8. [Erros comuns e soluções](#erros-comuns-e-solucoes)
9. [Próximos passos sugeridos](#proximos-passos-sugeridos)

---

## 🎯 Summary

This module applies Python programming patterns to model a card system (Creatures) that supports families,
evolution, extra capabilities and battle strategies. The code follows separation of concerns and is written with
static typing (`mypy`) and a `flake8`-compatible style.

---

## 🏗️ Overall Architecture

- `module07/ex0`: creature construction and factories (Abstract Factory).
- `module07/ex1`: independent capabilities (Healing, Transform) and factories that combine Creature+Capability.
- `module07/ex2`: battle strategies (Strategy pattern) with validation and abstract execution.
- Demonstration scripts: `module07/battle.py`, `module07/capacitor.py`, `module07/tournament.py`.

The goal is to keep classes small and composable: `Creature` provides the base, capabilities are separate
contracts, and strategies orchestrate different behaviors without coupling to concrete types.

---

## Exercise 0 — Creature Factory (ex0)

### 🎯 Goal
Implement an abstract `Creature`, concrete creature classes and an abstract `CreatureFactory` able to
produce the base form and the evolved form for a family.

### 🔧 What is implemented
- `Creature` (abstract): attributes `name`, `ctype`; abstract method `attack()`; concrete method `describe()`.
- Concrete creatures: `Flameling`, `Pyrodon`, `Aquabub`, `Torragon` — each with an appropriate `attack()`.
- `CreatureFactory` (abstract): `create_base()` and `create_evolved()`.
- Concrete factories: `FlameFactory` (Flameling → Pyrodon) and `AquaFactory` (Aquabub → Torragon).

### 🧭 Usage flow
```py
from ex0 import FlameFactory

f = FlameFactory()
base = f.create_base()      # Flameling
evo = f.create_evolved()    # Pyrodon
print(base.describe())
print(evo.attack())
```

---

## Exercise 1 — Capabilities (ex1)

### 🎯 Goal
Separate capabilities (healing, transforming) from the `Creature` model so that other entities could also
implement them. Provide factories that produce `Creature` instances with these capabilities.

### 🔧 What is implemented
- `IHeal` (Protocol) and `HealCapability` (ABC). Classes: `Sproutling`, `Bloomelle`. `HealingFactory` creates the family.
- `ITransform` (Protocol) and `TransformCapability` (ABC). Classes: `Shiftling`, `Morphagon`. `TransformFactory` creates the family.

### 🔍 Typing notes
- Protocols (`ICreature`, `IHeal`, `ITransform`) are `runtime_checkable` to allow `isinstance` at runtime and to
  make these contracts visible to `mypy`.
- Calls to capability-specific methods are preceded by `is_valid` (in strategies) and `cast` to inform the type
  checker that the object indeed implements the capability.

---

## Exercise 2 — Abstract Strategy (ex2)

### 🎯 Goal
Create a flexible battle architecture where each `Creature` is paired with a `BattleStrategy` that defines how it
acts in the tournament.

### 🔧 What is implemented
- `ABattleStrategy` (abstract): `is_valid(creature)` and `act(creature)`.
- `NormalStrategy`: valid for any `Creature`; calls `attack()`.
- `AggressiveStrategy`: valid for `ITransform`; performs `transform()`, a boosted attack, and `revert()`.
- `DefensiveStrategy`: valid for `IHeal`; performs `attack()` and `heal()`.

### 🧩 Tournament
- `module07/tournament.py` defines a function that accepts a list of opponents as `(Factory, Strategy)` tuples and
  organizes rounds where each opponent fights every other. Compatibility errors abort the tournament with a clear
  message.

---

## How to run and check

1. Install (optional):
```bash
python3 -m pip install --user flake8 mypy
```

2. Run static checks (from the repository root):
```bash
mypy module07
flake8 module07 --max-line-length=79
```

3. Run the demo scripts:
```bash
python3 module07/battle.py
python3 module07/capacitor.py
python3 module07/tournament.py
```

