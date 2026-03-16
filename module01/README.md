# 🏛️ Code Cultivation: Object-Oriented Garden Systems (Module 1)

This module marks my transition from procedural programming to **Object-Oriented Programming (OOP)**. I built a digital garden ecosystem to manage complex data structures and plant behaviors, focusing on scalability, code reuse, and data integrity.

## 🚀 Advanced Concepts Mastered

### 1. The Foundation of OOP
* **Classes vs. Objects:** Learned to design "blueprints" (Classes) and instantiate unique "entities" (Objects) with their own memory space.
* **`self` & `__init__`:** Mastered the use of the `self` keyword to access internal object data and the constructor method for automatic setup.

### 2. Encapsulation & Data Security
* **Data Protection:** Implemented the `_attribute` convention to signal private data.
* **Getters and Setters:** Developed validation logic (Porteiros) to ensure data integrity, preventing invalid states like negative heights or ages.

### 3. Inheritance & Polymorphism
* **Code Reuse:** Used class inheritance to avoid duplication. Subclasses like `Flower` and `Tree` inherit core traits from a base `Plant` class.
* **Multilevel Inheritance:** Built complex family trees: `Plant` -> `FloweringPlant` -> `PrizeFlower`.
* **Polymorphism:** Designed methods that work on any plant type, allowing the `GardenManager` to process diverse collections seamlessly.

### 4. Advanced Method Architecture
* **Instance Methods:** For behaviors unique to each object (e.g., `grow()`).
* **Static Methods (`@staticmethod`):** For utility functions that operate independently of object instances (e.g., `validate_height()`).
* **Class Variables:** Used global counters (e.g., `total_gardens`) shared across all instances of a class.

---

## 📂 Module Structure

| Exercise | Concept | Key File |
| :--- | :--- | :--- |
| **ex0** | Program Structure | `ft_garden_intro.py` |
| **ex1** | Class Blueprints | `ft_garden_data.py` |
| **ex2** | Object Behavior | `ft_plant_growth.py` |
| **ex3** | Object Factory | `ft_plant_factory.py` |
| **ex4** | Data Encapsulation | `ft_garden_security.py` |
| **ex5** | Specialization (Inheritance) | `ft_plant_types.py` |
| **ex6** | System Integration & Analytics | `ft_garden_analytics.py` |

---

## 🛠️ Requirements & Standards
* **Python 3.10+**
* **PEP 8 Compliance:** All code follows the `flake8` linter standards.
* **Documentation:** Extensive use of `docstrings` and `type hints` for professional-grade readability.

---

### 📝 Final Reflection
Building this garden ecosystem taught me that well-structured code is like healthy soil—it provides the foundation for sustainable growth. By moving away from scattered variables to organized objects, I can now build systems that are much easier to maintain and expand.