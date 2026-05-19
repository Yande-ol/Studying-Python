from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from ex0.creatures import Creature, CreatureFactory


class ICreature(Protocol):
    name: str

    def describe(self) -> str:  # pragma: no cover - simple protocol
        ...

    def attack(self) -> str:  # pragma: no cover - simple protocol
        ...


@runtime_checkable
class ITransform(ICreature, Protocol):
    def transform(self) -> str:  # pragma: no cover - simple protocol
        ...

    def revert(self) -> str:  # pragma: no cover - simple protocol
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, ctype: str) -> None:
        super().__init__(name, ctype)
        self.transformed = False

    def attack(self) -> str:
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, ctype: str) -> None:
        super().__init__(name, ctype)
        self.transformed = False

    def attack(self) -> str:
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class TransformFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
