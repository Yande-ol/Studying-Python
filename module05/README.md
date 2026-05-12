# Module 05: Code Nexus - Polymorphism in Data Flows

## 📚 Index
1. [Core Concepts](#core-concepts)
2. [Exercise 0 - Data Processor](#exercise-0---data-processor)
3. [Exercise 1 - Data Stream](#exercise-1---data-stream)
4. [Exercise 2 - Data Pipeline](#exercise-2---data-pipeline)
5. [How to Explain in the Defense](#how-to-explain-in-the-defense)

---

## 🎯 Core Concepts

### What is Polymorphism?
Polymorphism means "many forms." In object-oriented programming, it allows **different objects to respond to the same command in different ways**.

**Simple example:**
```
Command: "Make sound!"
- A dog responds: "Woof!"
- A cat responds: "Meow!"
- A bird responds: "Tweet!"
```

### What is an Abstract Class (ABC)?
An abstract class is a **template** that defines the interface (the contract) that all subclasses must follow.

```python
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass  # Declares the method but does not implement it
```

**Rule:** You cannot instantiate an abstract class. You MUST create subclasses that implement the abstract methods.

---

## 💾 Exercise 0 - Data Processor

### 🎯 Goal
Create a base architecture with:
- An abstract class `DataProcessor` (template)
- Three specialized subclasses (`NumericProcessor`, `TextProcessor`, `LogProcessor`)
- Each one processes a different type of data

### 📋 Visual Structure

```
┌─────────────────────────────────────────────────────┐
│            DataProcessor (ABSTRACT)                 │
│─────────────────────────────────────────────────────│
│  Abstract methods (MUST implement):                │
│  • validate(data: Any) -> bool                      │
│  • ingest(data: Any) -> None                        │
│                                                     │
│  Concrete method (SAME for all):                    │
│  • output() -> tuple[int, str]                      │
└─────────────────────────────────────────────────────┘
           ↗              ↓              ↖
    NumericProcessor  TextProcessor  LogProcessor
    (int, float)      (str)        (dict[str,str])
```

### 🔍 Detailed Explanation

#### 1. **Abstract Class DataProcessor**

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._next_rank: int = 0
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if the data is valid for this processor"""
        raise NotImplementedError()

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process and store the data"""
        raise NotImplementedError()

    def output(self) -> Tuple[int, str]:
        """Pop the first stored item"""
        if not self._storage:
            raise IndexError("No data to output")
        rank, value = self._storage.pop(0)
        return rank, value
```

What each field does:
- `@abstractmethod`: marks methods as REQUIRED in subclasses
- `_storage`: queue (list) of stored items
- `_next_rank`: counter of how many items have been processed
- `total_processed`: total number of items processed by this processor

#### 2. **NumericProcessor**

```python
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Accepts int, float or lists of them"""
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        """If a list, process each item; if single, process it"""
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._next_rank, str(item)))
                self._next_rank += 1
                self.total_processed += 1
        else:
            self._storage.append((self._next_rank, str(data)))
            self._next_rank += 1
            self.total_processed += 1
```

Example flow:
```
np = NumericProcessor()
np.ingest([1, 2, 3])

# _storage now contains:
[
  (0, "1"),
  (1, "2"),
  (2, "3"),
]
total_processed = 3
_next_rank = 3
```

#### 3. **TextProcessor and LogProcessor**

Same logic with different types:

- **TextProcessor:** `validate()` accepts `str` or `list[str]`
- **LogProcessor:** `validate()` accepts `dict[str, str]` or `list[dict[str, str]]`
  - Formats logs like: `"NOTICE: Connection to server"`

### 🎬 How the Example Works

```python
np = NumericProcessor()
print(np.validate(42))        # True
print(np.validate("Hello")) # False

np.ingest([1, 2, 3, 4, 5])
rank1, val1 = np.output()     # (0, "1")
rank2, val2 = np.output()     # (1, "2")
```

Expected output:
```
Numeric value 0: 1
Numeric value 1: 2
Numeric value 2: 3
```

---

## 📡 Exercise 1 - Data Stream

### 🎯 Goal
Use **polymorphism** to route different data types automatically to the correct processor.

### 📋 Visual Flow

```
┌──────────────────────────────────────────────────────────┐
│              DataStream (Orchestrator)                   │
│──────────────────────────────────────────────────────────│
│  • register_processor(proc): add a processor              │
│  • process_stream(stream): route data                    │
│  • print_processors_stats(): show statistics             │
└──────────────────────────────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    NumericProcessor TextProcessor LogProcessor
```

### 🔍 Detailed Explanation

#### 1. **DataStream Class**

```python
class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Add a new processor to the system"""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Route each element of the stream to the appropriate processor"""
        for element in stream:
            handled = False
            for proc in self._processors:
                try:
                    if proc.validate(element):
                        proc.ingest(element)  # type: ignore[arg-type]
                        handled = True
                        break
                except Exception:
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        """Show how many items each processor has"""
        print("== DataStream statistics ==")
        for proc in self._processors:
            remaining = len(getattr(proc, '_storage', []))
            name = proc.__class__.__name__.replace('Processor', ' Processor')
            print(f"{name}: total {proc.total_processed} items processed, remaining {remaining} on processor")
```

### 🎬 How Polymorphism Works

```python
ds = DataStream()
np = NumericProcessor()
tp = TextProcessor()
ds.register_processor(np)
ds.register_processor(tp)

# Now send a mixed stream
stream = [42, "Hello", [1, 2, 3], "World", [100, 200]]

ds.process_stream(stream)
```

Step-by-step behavior:
```
Element 1: 42
├─ NumericProcessor.validate(42) → True ✓
├─ NumericProcessor.ingest(42)
└─ Goes to NumericProcessor

Element 2: "Hello"
├─ NumericProcessor.validate("Hello") → False ✗
├─ TextProcessor.validate("Hello") → True ✓
├─ TextProcessor.ingest("Hello")
└─ Goes to TextProcessor

Element 3: [1, 2, 3]
├─ NumericProcessor.validate([1, 2, 3]) → True ✓
├─ NumericProcessor.ingest([1, 2, 3])
└─ Goes to NumericProcessor

Element 4: "World"
├─ NumericProcessor.validate("World") → False ✗
├─ TextProcessor.validate("World") → True ✓
├─ TextProcessor.ingest("World")
└─ Goes to TextProcessor
```

Why is this polymorphism?
- Same code (`for proc in self._processors: proc.validate()`)
- Different behavior (each class implements `validate()` in its own way)
- The decision which method to call happens at runtime (dynamic polymorphism)

---

## 🔌 Exercise 2 - Data Pipeline

### 🎯 Goal
Add a plugin system to export data in different formats (CSV, JSON).

It uses Duck Typing with `Protocol`: "If it looks like a duck and quacks like a duck, it's a duck."

### 📋 Architecture

```
DataStream + Processors
        │
        ├─→ output_pipeline(nb, plugin)
        │
        ├─→ CSVExportPlugin (CSV format)
        │
        └─→ JSONExportPlugin (JSON format)
```

### 🔍 Detailed Explanation

#### 1. **ExportPlugin Protocol**

```python
from typing import Protocol

class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Any class that implements this method is an ExportPlugin"""
        ...
```

What is a Protocol?
- Defines an interface without mandatory inheritance
- It's a contract: "If you have this method, you're compatible"
- No need to inherit, just provide the same method

#### 2. **CSVExportPlugin**

```python
class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Export as CSV (Comma-Separated Values)"""
        if not data:
            return
        values = [v for _, v in data]
        print("CSV Output:")
        print(",".join(values))
```

Example:
```python
data = [(0, "3.14"), (1, "-1"), (2, "2.71")]
csv_plugin.process_output(data)

# Output:
# CSV Output:
# 3.14,-1,2.71
```

#### 3. **JSONExportPlugin**

```python
class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Export as JSON (key-value pairs)"""
        if not data:
            return
        items = sorted(data, key=lambda x: x[0])
        parts: List[str] = []
        for rank, val in items:
            escaped = val.replace('"', '\\"').replace('\n', '\\n')
            parts.append(f'"item_{rank}": "{escaped}"')
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")
```

Example:
```python
data = [(3, "42"), (4, "21"), (5, "32")]
json_plugin.process_output(data)

# Output:
# JSON Output:
# {"item_3": "42", "item_4": "21", "item_5": "32"}
```

#### 4. **DataStream.output_pipeline()**

```python
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    """Consume nb items from each processor and export via plugin"""
    for proc in self._processors:
        collected: List[Tuple[int, str]] = []
        for _ in range(nb):
            try:
                item = proc.output()
                collected.append(item)
            except Exception:
                break
        if collected:
            plugin.process_output(collected)
```

### 🎬 How It Works

```python
ds = DataStream()
# ... register and process data ...

csv_plugin = CSVExportPlugin()
json_plugin = JSONExportPlugin()

# Extract 3 items from each processor and export as CSV
ds.output_pipeline(3, csv_plugin)

# Extract 5 items from each processor and export as JSON
ds.output_pipeline(5, json_plugin)
```

Visual flow:
```
Processor has: [(0, "val0"), (1, "val1"), (2, "val2"), (3, "val3"), ...]

output_pipeline(3, csv_plugin):
├─ Extract 3 items: [(0, "val0"), (1, "val1"), (2, "val2")]
├─ Calls csv_plugin.process_output(...)
└─ Line output comes from the CSVExportPlugin

output_pipeline(3, json_plugin):
├─ Extract 3 items: [(3, "val3"), (4, "val4"), (5, "val5")]
├─ Calls json_plugin.process_output(...)
└─ Line output comes from the JSONExportPlugin
```

### 🤔 Why is Protocol useful?

```python
# Without Protocol, we would need to do:
class DataStream:
    def output_pipeline(self, nb: int, plugin: CSVExportPlugin | JSONExportPlugin):
        # Would have to enumerate all possible types...
        pass

# With Protocol, simply:
class DataStream:
    def output_pipeline(self, nb: int, plugin: ExportPlugin):
        # Any object with process_output() works!
        # Easy to add new export types later
        pass
```

**Duck Typing:** "If it has the method I need, I don't care about its type!"

---

## 🔗 Technical Summary

| Concept | Where It Appears | Purpose |
|---------|------------------|---------|
| **ABC (Abstract Base Class)** | Exercise 0 | Ensure subclasses implement required methods |
| **Inheritance** | Ex0, Ex1, Ex2 | Reuse base code and provide specializations |
| **Polymorphism (Method Overriding)** | Exercise 1 | Different implementations of validate/ingest |
| **Type Hints** | All exercises | Document expected types |
| **Protocol (Duck Typing)** | Exercise 2 | Interface without mandatory inheritance |
| **List[Tuple[int, str]]** | All exercises | Store rank + processed value |

