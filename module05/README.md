# Module 05: Code Nexus - Polimorfismo em Fluxos de Dados

## 📚 Índice
1. [Conceitos Base](#conceitos-base)
2. [Exercise 0 - Data Processor](#exercise-0---data-processor)
3. [Exercise 1 - Data Stream](#exercise-1---data-stream)
4. [Exercise 2 - Data Pipeline](#exercise-2---data-pipeline)
5. [Como Explicar na Defesa](#como-explicar-na-defesa)

---

## 🎯 Conceitos Base

### O que é Polimorfismo?
Polimorfismo significa "muitas formas". Na programação orientada a objetos, permite que **objetos diferentes respondam ao mesmo comando de formas diferentes**.

**Exemplo simples:**
```
Comando: "Faz som!"
- Um cachorro faz: "Au au!"
- Um gato faz: "Miau!"
- Um pássaro faz: "Piu piu!"
```

### O que é uma Abstract Class (ABC)?
Uma classe abstrata é um **modelo/template** que define a interface (o contrato) que todas as subclasses devem seguir.

```python
class Animal(ABC):
    @abstractmethod
    def fazer_som(self) -> str:
        pass  # Não implementa, apenas declara
```

**Regra:** Não é possível criar uma instância de uma classe abstrata. Você PRECISA criar subclasses que implementem os métodos abstratos.

---

## 💾 Exercise 0 - Data Processor

### 🎯 Objetivo
Criar uma arquitetura base com:
- Uma classe abstrata `DataProcessor` (template)
- Três subclasses especializadas (NumericProcessor, TextProcessor, LogProcessor)
- Cada uma processa um tipo diferente de dados

### 📋 Estrutura Visual

```
┌─────────────────────────────────────────────────────┐
│            DataProcessor (ABSTRATA)                  │
│─────────────────────────────────────────────────────│
│  Métodos abstratos (OBRIGATÓRIO implementar):       │
│  • validate(data: Any) -> bool                      │
│  • ingest(data: Any) -> None                        │
│                                                      │
│  Método concreto (IGUAL para todos):                │
│  • output() -> tuple[int, str]                      │
└─────────────────────────────────────────────────────┘
           ↗              ↓              ↖
    NumericProcessor  TextProcessor  LogProcessor
    (int, float)      (str)        (dict str:str)
```

### 🔍 Explicação Detalhada

#### 1. **Classe Abstrata DataProcessor**

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._next_rank: int = 0
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Verifica se o dado é válido para este processador"""
        raise NotImplementedError()

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Processa e armazena o dado"""
        raise NotImplementedError()

    def output(self) -> Tuple[int, str]:
        """Extrai o primeiro dado armazenado"""
        if not self._storage:
            raise IndexError("No data to output")
        rank, value = self._storage.pop(0)
        return rank, value
```

**O que cada coisa faz:**
- `@abstractmethod`: marca como "OBRIGATÓRIO" nas subclasses
- `_storage`: fila (lista) de dados armazenados
- `_next_rank`: contador de quantos itens já foram processados
- `total_processed`: total de itens que passaram por este processador

#### 2. **NumericProcessor**

```python
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Só aceita int, float ou listas deles"""
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        """Se for lista, processa cada item; se for único, processa só ele"""
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

**Fluxo de um exemplo:**
```
np = NumericProcessor()
np.ingest([1, 2, 3])

_storage agora tem:
[
  (0, "1"),   <- rank 0
  (1, "2"),   <- rank 1
  (2, "3")    <- rank 2
]
total_processed = 3
_next_rank = 3
```

#### 3. **TextProcessor e LogProcessor**

Mesma lógica, mas com tipos diferentes:

- **TextProcessor:** `validate()` aceita `str` ou `list[str]`
- **LogProcessor:** `validate()` aceita `dict[str, str]` ou `list[dict[str, str]]`
  - Formata como: `"NOTICE: Connection to server"`

### 🎬 Como Funciona o Exemplo

```python
np = NumericProcessor()
print(np.validate(42))              # True
print(np.validate("Hello"))         # False

np.ingest([1, 2, 3, 4, 5])
rank1, val1 = np.output()           # (0, "1")
rank2, val2 = np.output()           # (1, "2")
```

**Output esperado:**
```
Numeric value 0: 1
Numeric value 1: 2
Numeric value 2: 3
```

---

## 📡 Exercise 1 - Data Stream

### 🎯 Objetivo
Usar **polimorfismo** para rotear diferentes tipos de dados automaticamente para o processador correto.

### 📋 Fluxo Visual

```
┌──────────────────────────────────────────────────────────┐
│              DataStream (Orquestrador)                   │
│──────────────────────────────────────────────────────────│
│  • register_processor(proc): adiciona processador        │
│  • process_stream(stream): roteia dados                  │
│  • print_processors_stats(): mostra estatísticas         │
└──────────────────────────────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    NumericProcessor TextProcessor LogProcessor
```

### 🔍 Explicação Detalhada

#### 1. **Classe DataStream**

```python
class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Adiciona um novo processador ao sistema"""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Roteia cada elemento do stream para o processador apropriado"""
        for element in stream:
            handled = False
            for proc in self._processors:
                try:
                    if proc.validate(element):
                        proc.ingest(element)  # type: ignore[arg-type]
                        handled = True
                        break  # Para quando encontrar um processador compatível
                except Exception:
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        """Mostra quantos itens cada processador tem"""
        print("== DataStream statistics ==")
        for proc in self._processors:
            remaining = len(getattr(proc, '_storage', []))
            name = proc.__class__.__name__.replace('Processor', ' Processor')
            print(f"{name}: total {proc.total_processed} items processed, remaining {remaining} on processor")
```

### 🎬 Como Funciona o Polimorfismo

```python
ds = DataStream()
np = NumericProcessor()
tp = TextProcessor()
ds.register_processor(np)
ds.register_processor(tp)

# Agora vamos enviar um stream MISTOmix
stream = [42, "Hello", [1, 2, 3], "World", [100, 200]]

ds.process_stream(stream)
```

**O que acontece passo a passo:**
```
Elemento 1: 42
├─ NumericProcessor.validate(42) → True ✓
├─ NumericProcessor.ingest(42)
└─ Vai para NumericProcessor

Elemento 2: "Hello"
├─ NumericProcessor.validate("Hello") → False ✗
├─ TextProcessor.validate("Hello") → True ✓
├─ TextProcessor.ingest("Hello")
└─ Vai para TextProcessor

Elemento 3: [1, 2, 3]
├─ NumericProcessor.validate([1, 2, 3]) → True ✓
├─ NumericProcessor.ingest([1, 2, 3])
└─ Vai para NumericProcessor

Elemento 4: "World"
├─ NumericProcessor.validate("World") → False ✗
├─ TextProcessor.validate("World") → True ✓
├─ TextProcessor.ingest("World")
└─ Vai para TextProcessor
```

**Por que is isso polimorfismo?**
- Mesmo código (`for proc in self._processors: proc.validate()`)
- Comportamento diferente (cada classe implementa `validate()` à sua forma)
- A escolha de qual método chamar acontece em **tempo de execução** (polimorfismo dinâmico)

---

## 🔌 Exercise 2 - Data Pipeline

### 🎯 Objetivo
Adicionar um sistema de **plugins** para exportar dados em diferentes formatos (CSV, JSON).

Usa **Duck Typing com Protocol**: "Se parece com um pato, faz quack e caminha como um pato... é um pato!"

### 📋 Arquitetura

```
DataStream + Processadores
        │
        ├─→ output_pipeline(nb, plugin) 
        │
        ├─→ CSVExportPlugin (formato CSV)
        │
        └─→ JSONExportPlugin (formato JSON)
```

### 🔍 Explicação Detalhada

#### 1. **Protocol ExportPlugin**

```python
from typing import Protocol

class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Qualquer classe que tenha este método 'é' um ExportPlugin"""
        ...
```

**O que é Protocol?**
- Define uma "interface" sem herança necessária
- É como um contrato: "Se você tem este método, você é compatível"
- Não precisa herdar, apenas ter o mesmo método

#### 2. **CSVExportPlugin**

```python
class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Exporta como CSV (Comma-Separated Values)"""
        if not data:
            return
        values = [v for _, v in data]  # Extrai só os valores
        print("CSV Output:")
        print(",".join(values))
```

**Exemplo:**
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
        """Exporta como JSON (key-value pairs)"""
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

**Exemplo:**
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
    """Consome nb itens de cada processador e exporta via plugin"""
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

### 🎬 Como Funciona

```python
ds = DataStream()
# ... registrar e processar dados ...

csv_plugin = CSVExportPlugin()
json_plugin = JSONExportPlugin()

# Extrair 3 itens de cada processador e exportar em CSV
ds.output_pipeline(3, csv_plugin)

# Extrair 5 itens de cada processador e exportar em JSON
ds.output_pipeline(5, json_plugin)
```

**Fluxo visual:**
```
Processador tem: [(0, "val0"), (1, "val1"), (2, "val2"), (3, "val3"), ...]

output_pipeline(3, csv_plugin):
├─ Extrai 3 itens: [(0, "val0"), (1, "val1"), (2, "val2")]
├─ Chama csv_plugin.process_output(...)
└─ Output da linha vem do CSVExportPlugin

output_pipeline(3, json_plugin):
├─ Extrai 3 itens: [(3, "val3"), (4, "val4"), (5, "val5")]
├─ Chama json_plugin.process_output(...)
└─ Output da linha vem do JSONExportPlugin
```

### 🤔 Por que Protocol é útil?

```python
# Sem Protocol, teríamos que fazer:
class DataStream:
    def output_pipeline(self, nb: int, plugin: CSVExportPlugin | JSONExportPlugin):
        # Teria que listar todos os tipos possíveis...
        pass

# Com Protocol, simplesmente:
class DataStream:
    def output_pipeline(self, nb: int, plugin: ExportPlugin):
        # Qualquer objeto que tenha process_output() funciona!
        # Fácil adicionar novos tipos de exportação depois
        pass
```

**Duck Typing:** "Se tem o método que preciso, não me importo com o tipo!"

---

## 🔗 Resumo Técnico

| Conceito | Onde Aparece | Propósito |
|----------|--------------|----------|
| **ABC (Abstract Base Class)** | Exercise 0 | Garantir que subclasses implementem métodos |
| **Herança** | Ex0, Ex1, Ex2 | Reusar código base e especializações |
| **Polimorfismo (Method Overriding)** | Exercise 1 | Diferentes implementações do validate/ingest |
| **Type Hints** | Todos | Documentar tipos esperados |
| **Protocol (Duck Typing)** | Exercise 2 | Interface sem herança obrigatória |
| **List[Tuple[int, str]]** | Todos | Armazenar rank + valor processado |

