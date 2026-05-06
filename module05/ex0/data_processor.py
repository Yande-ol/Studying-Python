from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._next_rank: int = 0
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError()

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")
        rank, value = self._storage.pop(0)
        return rank, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
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


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._next_rank, item))
                self._next_rank += 1
                self.total_processed += 1
        else:
            self._storage.append((self._next_rank, data))
            self._next_rank += 1
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_entry(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if isinstance(data, dict):
            return valid_entry(data)
        if isinstance(data, list):
            return all(valid_entry(x) for x in data)
        return False

    def ingest(self, data: Union[dict, List[dict]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_entry(d: dict) -> str:
            # Expecting keys like 'log_level' and 'log_message'
            level: str = d.get('log_level', '')
            message: str = d.get('log_message', '')
            return f"{level}: {message}"

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._next_rank, format_entry(item)))
                self._next_rank += 1
                self.total_processed += 1
        else:
            self._storage.append((self._next_rank, format_entry(data)))
            self._next_rank += 1
            self.total_processed += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest('foo')  # type: ignore[arg-type]
    except Exception as exc:  # pragma: no cover - demonstration
        print(f"Got exception: {exc}")
    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        r, v = np.output()
        print(f"Numeric value {i}: {v}")
    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    r, v = tp.output()
    print(f"Text value 0: {v}")
    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ]
    print(f"Processing data: {logs}")
    lp.ingest(logs)
    print("Extracting 2 values...")
    for i in range(2):
        r, v = lp.output()
        print(f"Log entry {i}: {v}")
