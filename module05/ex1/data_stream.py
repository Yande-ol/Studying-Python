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
            return all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())

        if isinstance(data, dict):
            return valid_entry(data)
        if isinstance(data, list):
            return all(valid_entry(x) for x in data)
        return False

    def ingest(self, data: Union[dict, List[dict]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        def format_entry(d: dict) -> str:
            level = d.get('log_level', '')
            message = d.get('log_message', '')
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


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                try:
                    if proc.validate(element):
                        proc.ingest(element)  # type: ignore[arg-type]
                        handled = True
                        break
                except Exception:
                    # If a processor raises during ingest, do not stop whole stream
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            remaining = len(getattr(proc, '_storage', []))
            name = proc.__class__.__name__.replace('Processor', ' Processor')
            print(f"{name}: total {proc.total_processed} items processed, remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    np = NumericProcessor()
    ds.register_processor(np)
    print("Send first batch of data on stream: ", end="")
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]
    print(batch)
    ds.process_stream(batch)
    ds.print_processors_stats()
    print("\nRegistering other data processors")
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    # consume
    for _ in range(3):
        try:
            np.output()
        except Exception:
            break
    for _ in range(2):
        try:
            tp.output()
        except Exception:
            break
    for _ in range(1):
        try:
            lp.output()
        except Exception:
            break
    ds.print_processors_stats()
