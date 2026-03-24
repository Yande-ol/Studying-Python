# 💾 Data Quest: Digital Preservation
### Module 04 — Data Archiving in the Cyber Era (2087)

## 📖 Overview
In **Module 04**, we took on the role of **Data Archivists** in the year 2087. The central focus was **Data Persistence**: how to read, write, and manage files securely and resiliently. We learned that in Data Engineering, a poorly closed file or an unhandled error can lead to the permanent loss of vital information.



---

## 🏗️ Preservation Architecture: The Security Protocol
To ensure the integrity of the archives, we implemented three fundamental pillars:

1.  **The Sacred Protocol (`with`):** We utilized Context Managers to guarantee that every "vault" (file) is sealed automatically, preventing memory leaks and data corruption.
2.  **Stream Management:** We learned to separate the standard data flow (`stdout`) from emergency alerts (`stderr`), allowing for professional system monitoring.
3.  **Crisis Resilience (`try/except`):** We implemented contingency systems to handle missing files or denied permissions without interrupting the core execution.

---

## 🛠️ Key Engineering Concepts

### 1. RAII & Context Managers
We explored the principle of *Resource Acquisition Is Initialization*. By using the `with` block, Python manages the lifecycle of the file (opening and closing) atomically, even if an exception occurs during processing.



### 2. Disk Access Modes
We differentiated between operation modes to prevent data disasters:
* **Read (`'r'`):** Passive access for retrieving historical data.
* **Write (`'w'`):** Active access for creating or completely replacing records.
* **Append (`'a'`):** Expanding records without destroying existing content.



### 3. Exception Hierarchy
We developed a **Crisis Response** system that identifies specific failures (`FileNotFoundError`, `PermissionError`) before resorting to generic handlers, ensuring accurate real-time diagnostics.



---

## 📂 Module Contents

| Exercise | Mission | Archivist Superpower |
| :--- | :--- | :--- |
| **ex0** | `Ancient Text Recovery` | Secure data retrieval via `'r'` mode. |
| **ex1** | `Archive Creation` | Inscribing new data via `'w'` mode. |
| **ex2** | `Stream Management` | Channel separation via `sys.stdout` and `sys.stderr`. |
| **ex3** | `Vault Security` | Atomic closing guarantee with the `with` protocol. |
| **ex4** | `Crisis Response` | Exception handling and system resilience. |

---

## 🚀 How to Run
To test the crisis response system:

```bash
python3 ex4/ft_crisis_response.py