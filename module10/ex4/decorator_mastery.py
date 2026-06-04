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
            # extract 'power' from kwargs or positional args
            if 'power' in kwargs:
                power = kwargs.get('power')
            else:
                # handle both standalone functions (target, power)
                # and methods (self, spell_name, power)
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
                        print(f'Spell failed, retrying... (attempt {attempts}/{max_attempts})')
            return f'Spell casting failed after {max_attempts} attempts'

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return isinstance(name, str) and len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


if __name__ == '__main__':
    @spell_timer
    def fireball():
        time.sleep(0.05)
        return 'Fireball cast!'

    print('Testing spell timer...')
    print('Result:', fireball())

    @retry_spell(3)
    def flaky():
        raise RuntimeError('boom')

    print('Testing retrying spell...')
    print(flaky())

    print('Testing MageGuild...')
    print(MageGuild.validate_mage_name('Al'))
    print(MageGuild.validate_mage_name('Gandalf'))
    g = MageGuild()
    print(g.cast_spell('Lightning', 15))
    print(g.cast_spell('TinySpark', 5))
