from functools import reduce, partial, lru_cache, singledispatch
from typing import Any, Callable
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in {'add', 'multiply', 'max', 'min'}:
        raise ValueError('Unknown operation')
    if operation == 'max':
        return max(spells)
    if operation == 'min':
        return min(spells)
    if operation == 'add':
        return reduce(operator.add, spells)
    return reduce(operator.mul, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'enchanted_a': partial(base_enchantment, 50, 'fire'),
        'enchanted_b': partial(base_enchantment, 50, 'ice'),
        'enchanted_c': partial(base_enchantment, 50, 'arcane'),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('n must be non-negative')
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(x: Any) -> str:
        return 'Unknown spell type'

    @dispatch.register
    def _(x: int) -> str:  # damage spell
        return f'Damage spell: {x} damage'

    @dispatch.register
    def _(x: str) -> str:  # enchantment
        return f'Enchantment: {x}'

    @dispatch.register
    def _(x: list) -> str:  # multi-cast
        return f'Multi-cast: {len(x)} spells'

    return dispatch


if __name__ == '__main__':
    print('Testing spell reducer...')
    spells = [10, 20, 30, 40]
    print('Sum:', spell_reducer(spells, 'add'))
    print('Product:', spell_reducer(spells, 'multiply'))
    print('Max:', spell_reducer(spells, 'max'))
    print('Testing memoized fibonacci...')
    print('Fib(0):', memoized_fibonacci(0))
    print('Fib(1):', memoized_fibonacci(1))
    print('Fib(10):', memoized_fibonacci(10))
    print('Testing spell dispatcher...')
    disp = spell_dispatcher()
    print(disp(42))
    print(disp('fireball'))
    print(disp(['a', 'b', 'c']))
    print(disp(3.14))
