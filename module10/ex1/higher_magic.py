from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapped(*args: Any, **kwargs: Any) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return wrapped


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return sequence


if __name__ == '__main__':
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    print('Testing spell combiner...')
    combined = spell_combiner(fireball, heal)
    print('Combined spell result:', combined('Dragon', 10))
    print('Testing power amplifier...')
    mega = power_amplifier(fireball, 3)
    print('Original: 10, Amplified:', mega('Orc', 10))
