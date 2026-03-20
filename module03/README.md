# 🕹️ Data Quest: Mastering Python Collections
### Module 03 — Data Engineering in the Pixel Dimension

## 📖 Overview
In **Module 03**, we move beyond basic logic and dive into the core of Data Engineering: **Data Structures**. The goal was to build the "PixelMetrics 3000," an analytics platform for games. We learned how to choose the right tool—List, Tuple, Set, or Dict—for different types of information, ensuring efficiency, security, and performance.



---

## 🏗️ Data Architecture: The RPG Inventory Analogy
To master collections, we visualized the system as a **Data RPG**:

1.  **The Backpack (List):** Where we store items in a specific order. We can add, remove, and change them. Perfect for scores and histories.
2.  **The Map (Tuple):** 3D coordinates "carved in stone." Once created, they are immutable. Maximum security for locations.
3.  **The Achievement Album (Set):** A place where duplicates are not allowed. Ideal for ensuring each trophy is unique.
4.  **The Organized Shelf (Dict):** Where we find any information instantly using a label (Key).

---

## 🛠️ Key Engineering Concepts

### 1. Immutability vs. Mutability
We learned that using a **Tuple** for 3D coordinates is not just a style choice; it is a design decision to prevent memory bugs and ensure that sensitive data isn't accidentally altered by other parts of the program.



### 2. Memory & Efficiency (Generators)
We implemented the **Stream Wizard** using `yield`. Instead of loading 1 million events into a "bucket" (List), we opened a "tap" (Generator) that processes one piece of data at a time, keeping RAM usage constant and low.



### 3. Data Alchemy (Comprehensions)
We mastered the art of transforming entire collections in a single line. Using List, Dict, and Set Comprehensions, we filtered "active players" and "high scores" elegantly and performantly.



---

## 📂 Module Contents

| Exercise | Component | Data Superpower |
| :--- | :--- | :--- |
| **ex0** | `Command Quest` | CLI Communication via `sys.argv`. |
| **ex1** | `Score Cruncher` | Dynamic manipulation using **Lists**. |
| **ex2** | `Position Tracker` | 3D Geometry and Immutability with **Tuples**. |
| **ex3** | `Achievement Hunter` | Set operations and deduplication with **Sets**. |
| **ex4** | `Inventory Master` | Complex mapping and nested **Dictionaries**. |
| **ex5** | `Stream Wizard` | Infinite flow processing with **Generators**. |
| **ex6** | `Data Alchemist` | One-line data transformation via **Comprehensions**. |

---

## 🚀 How to Run
To run the complete Analytics Dashboard:

```bash
python3 ex6/ft_analytics_dashboard.py