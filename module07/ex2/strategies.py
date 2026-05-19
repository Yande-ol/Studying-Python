from __future__ import annotations
from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.healing import IHeal
from ex1.transforming import ITransform


class ABattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(ABattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(ABattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, ITransform)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise TypeError(
                "Invalid Creature '"
                + f"{creature.name}"
                + "' for this aggressive strategy"
            )
        tr = cast(ITransform, creature)
        print(tr.transform())
        print(f"{tr.name} performs a boosted strike!")
        print(tr.revert())


class DefensiveStrategy(ABattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, IHeal)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise TypeError(
                "Invalid Creature '"
                + f"{creature.name}"
                + "' for this defensive strategy"
            )
        h = cast(IHeal, creature)
        print(h.attack())
        print(h.heal())
