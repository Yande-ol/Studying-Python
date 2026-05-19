from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingFactory, TransformFactory
from ex2.strategies import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    ABattleStrategy,
)


def battle(
    creature_a,
    strat_a: ABattleStrategy,
    creature_b,
    strat_b: ABattleStrategy,
) -> None:
    print("* Battle *")
    print(creature_a.describe())
    print("vs.")
    print(creature_b.describe())
    print("now fight!")
    try:
        if not strat_a.is_valid(creature_a):
            raise TypeError(
                "Invalid Creature '" + f"{creature_a.name}"
                + "' for this aggressive strategy"
            )
        strat_a.act(creature_a)
        if not strat_b.is_valid(creature_b):
            raise TypeError(
                "Invalid Creature '" + f"{creature_b.name}"
                + "' for this aggressive strategy"
            )
        strat_b.act(creature_b)
    except TypeError:
        raise


def run_tournament(opponents: List[Tuple]):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fac_i, strat_i = opponents[i]
            fac_j, strat_j = opponents[j]
            a = fac_i.create_base()
            b = fac_j.create_base()
            try:
                battle(a, strat_i, b, strat_j)
            except TypeError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingFactory(), DefensiveStrategy()),
    ]
    run_tournament(opponents)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingFactory(), DefensiveStrategy()),
    ]
    run_tournament(opponents)

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingFactory(), DefensiveStrategy()),
        (TransformFactory(), AggressiveStrategy()),
    ]
    run_tournament(opponents)
