from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    air = create_air()
    strength = strength_potion()
    fire = "Fire element created"
    return (
        "Recipe transmuting Lead to Gold: brew'"
        + air
        + "' and '"
        + strength
        + "' mixed with '"
        + fire
        + "'"
    )
