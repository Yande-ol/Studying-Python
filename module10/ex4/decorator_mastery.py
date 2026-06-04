from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        print(f'Casting {func.__name__}...')
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'Spell completed in {elapsed:.3f} seconds')
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if 'power' in kwargs:
                power = kwargs.get('power')
            else:
                if len(args) >= 2 and isinstance(args[1], int):
                    power = args[1]
                elif len(args) >= 3 and isinstance(args[2], int):
                    power = args[2]
                else:
                    power = None
            if power is None or power < min_power:
                return 'Insufficient power for this spell'
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    if attempts < max_attempts:
                        print(
                            f'Spell failed, retrying... '
                            f'(attempt {attempts}/{max_attempts})'
                        )
            return (
                f'Spell casting failed after {max_attempts} attempts'
            )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            isinstance(name, str)
            and len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


if __name__ == '__main__':
    print('Testing spell timer...')

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return 'Fireball cast!'
    print('Result:', fireball())

    print('Testing retrying spell...')

    @retry_spell(3)
    def flaky():
        raise RuntimeError('boom')
    print(flaky())

    @retry_spell(3)
    def waaaaagh():
        return 'Waaaaaaagh spelled !'
    print(waaaaagh())

    print('Testing MageGuild...')
    print(MageGuild.validate_mage_name('Gandalf'))
    print(MageGuild.validate_mage_name('Al'))

    g = MageGuild()
    print(g.cast_spell('Lightning', 15))
    print(g.cast_spell('TinySpark', 5))
