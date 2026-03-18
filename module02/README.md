# 🌿 Garden Guardian: Data Engineering for Smart Agriculture
### Module 02 — Resilient Data Pipelines & Exception Handling

## 📖 Overview
In **Module 02**, the focus shifts from building objects (Module 01) to **system survival**. In a real-world Smart Farming scenario, sensors fail, connections drop, and data arrives corrupted. This module explores the **Python Exception System** to build security barriers that prevent system crashes and ensure data integrity even under "stormy" conditions.



---

## 🏗️ Safety Architecture: The Fire Control Panel Analogy
To master this module, we visualize the system as a **Hotel Fire Alarm Central**:

1.  **The Sensor (The `raise`):** Located in a specific room (function), it detects something wrong and triggers the signal.
2.  **The Sector Panel (`GardenError`):** Groups the alarms. If a smoke sensor trips, the central alerts the "Garden" sector, allowing for a focused response.
3.  **The Emergency Protocol (`finally`):** No matter what happens (fire or false alarm), the emergency doors **must** be unlocked at the end. This is our "resource cleaner."

---

## Core Engineering Concepts

### 1. Exception Hierarchy (Inheritance)
We use inheritance to organize errors. Creating a class that inherits from `Exception` allows us to decide the level of detail for our "shield" (`except`).
* **Specific Catch:** Handles only one error (e.g., `WaterError`).
* **Generic Catch:** Handles any error from that sector (e.g., `GardenError`).



### 2. The `finally` Block (Determinism)
Unlike C, where a `free()` can be forgotten if an error occurs, Python's `finally` guarantees the execution of cleanup code. It is essential for closing irrigation valves and database connections, preventing **Resource Leaks**.



### 3. Active Validation with `raise`
We don't wait for Python to break. We anticipate the failure. If a moisture sensor returns an impossible value, the engineer uses `raise` to stop the flow before "rotten" data contaminates the database.

---

## 📂 Module Contents

| Exercise | Component | Engineering Goal |
| :--- | :--- | :--- |
| **ex0** | `ft_first_exception` | Initial sensor data filtering (Input Validation). |
| **ex1** | `ft_different_errors` | Identifying native "crimes": `KeyError`, `ValueError`, `ZeroDivision`. |
| **ex2** | `ft_custom_errors` | Building the family tree of custom agricultural alarms. |
| **ex3** | `ft_finally_block` | Implementing unbreakable safety protocols (Cleanup). |
| **ex4** | `ft_raise_errors` | Creating rigorous quality filters for plant health. |
| **ex5** | `ft_garden_management` | **The Final Boss:** Full integration into a Resilient Management System. |

---

## How to Run
Each exercise demonstrates a layer of protection. To see the Garden Manager in action with all protocols active:

```bash
python3 ex5/ft_garden_management.py