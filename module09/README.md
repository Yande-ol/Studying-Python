# Module 09: Orbital Systems — Composition & Concurrency

## 📚 Index
1. [Core Concepts](#core-concepts)
2. [Exercise 0 - Space Station](#exercise-0---space-station)
3. [Exercise 1 - Alien Contact](#exercise-1---alien-contact)
4. [Exercise 2 - Space Crew](#exercise-2---space-crew)
5. [How to Use This Module](#how-to-use-this-module)

---

## 🎯 Core Concepts

This module focuses on designing robust, composable systems that model components of a space program. You will practice:

- Composition: building complex behavior by combining smaller objects and functions.
- Concurrency-safe patterns: coordinating actors (crew, systems) that operate in parallel.
- Clear data modeling: using classes and type hints to express domain intent.

Key ideas:

- Single Responsibility: each class or function should do one thing well.
- Message-passing / event-driven flow: simulate interactions between systems via method calls or lightweight messages.
- Deterministic tests: design code so unit tests are reliable and easy to reason about.

---

## 🚀 Exercise 0 - Space Station

### 🎯 Goal
Model a `SpaceStation` composed of multiple `Module` instances. Each `Module` exposes a status and resource levels (power, oxygen, storage). The station can report aggregated metrics and perform a simple resource redistribution.

### 📋 Structure

```
SpaceStation
├─ Module: Habitat
├─ Module: Lab
├─ Module: PowerCore
└─ Module: Cargo

Operations:
- report_status() -> dict
- redistribute_resource(resource: str, amount: int) -> None
```

### 🔍 Notes

- Implement `Module` as a small class with properties: `name`, `power`, `oxygen`, `capacity`.
- `SpaceStation.report_status()` should return totals and per-module summaries.
- `redistribute_resource()` finds modules that need or can spare the resource and transfers units until amount exhausted or no more moves possible.

---

## 👽 Exercise 1 - Alien Contact

### 🎯 Goal
Create a small protocol for handling incoming signals. Build an `AlienSignal` type and a `ContactHandler` that attempts to decode messages and classifies them (Friendly, Unknown, Hostile).

### 📋 Flow

```
SignalReceiver -> ContactHandler -> Action

ContactHandler:
- decode(signal) -> Optional[dict]
- classify(payload) -> str
- react(classification) -> str
```

### 🔍 Notes

- Keep decoding simple and testable (e.g., base64 or simple substitution). Return `None` when decoding fails.
- `classify()` uses heuristics: presence of the word "greeting" → `Friendly`; repeated patterns → `Unknown`; explicit threats → `Hostile`.
- `react()` returns a short instruction string (e.g., `"respond_with_beacon"`, `"log_and_monitor"`, `"raise_alert"`).

---

## 🧑‍🚀 Exercise 2 - Space Crew

### 🎯 Goal
Design a `Crew` system where crew members have roles and can perform tasks concurrently. Provide utilities to schedule tasks, query availability, and simulate simple duty rotations.

### 📋 Components

```
CrewMember
- name: str
- role: str
- stamina: int
Task
- name: str
- required_role: str
Crew
- assign(task: Task) -> bool
- rotate() -> None
```

### 🔍 Notes

- `assign()` finds an available member with matching role and sufficient stamina, then reduces stamina.
- `rotate()` simulates the passage of time: restores stamina partially and rotates duty assignments.
- Keep concurrency conceptual: use sequential function calls in exercises, but design with thread-safe patterns in mind (no globals, clear interfaces).

---

## 🧭 How to Use This Module

### Prerequisites

- Python 3.10+ recommended.
- Install runtime dependencies listed in `module09/requirements.txt`:

```bash
python3 -m pip install -r module09/requirements.txt
```

### Running the Example Scripts

Each exercise provides a script entrypoint. Run them directly to see small demo scenarios:

```bash
python3 module09/ex0/space_station.py
python3 module09/ex1/alien_contact.py
python3 module09/ex2/space_crew.py
```

If a script lacks a demo, import the classes or functions interactively:

```bash
python3 -c "from module09.ex0.space_station import SpaceStation; print(SpaceStation().report_status())"
```

### Tests

This project does not include a test suite by default. If you want to add tests, we recommend `pytest`, but it is optional — the current repository uses direct script demos and simple importable modules for manual verification.

