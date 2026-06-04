from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def acc(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return acc


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> dict[str, Callable]:
    store_dict: dict = {}

    def store(key: str, value: Any) -> None:
        store_dict[key] = value

    def recall(key: str) -> Any:
        return store_dict.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == '__main__':
    print('Testing mage counter...')
    a = mage_counter()
    print('counter_a call 1:', a())
    print('counter_a call 2:', a())
    b = mage_counter()
    print('counter_b call 1:', b())
    print('Testing spell accumulator...')
    acc = spell_accumulator(100)
    print('Base 100, add 20:', acc(20))
    print('Base 100, add 30:', acc(30))
    print('Testing enchantment factory...')
    print(enchantment_factory('Flaming')('Sword'))
    print(enchantment_factory('Frozen')('Shield'))
    print('Testing memory vault...')
    mv = memory_vault()
    mv['store']('secret', 42)
    print("Store 'secret':", mv['recall']('secret'))
    print("Recall 'secret':", mv['recall']('secret'))
    print("Recall 'unknown':", mv['recall']('unknown'))
