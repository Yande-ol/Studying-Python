from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Protocol, runtime_checkable
from ex0.creatures import Creature, CreatureFactory


class ICreature(Protocol):
    name: str

    def describe(self) -> str:  # pragma: no cover - simple protocol
        ...

    def attack(self) -> str:  # pragma: no cover - simple protocol
        ...


@runtime_checkable
class IHeal(ICreature, Protocol):
    # Protocol method: heal
    def heal(self, target: Optional[Creature] = None) -> str:
        ...


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional[Creature] = None) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[Creature] = None) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Optional[Creature] = None) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")
