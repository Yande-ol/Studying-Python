import elements as root_elements
from .elements import create_earth, create_air


def strength_potion() -> str:
    fire = root_elements.create_fire()
    water = root_elements.create_water()
    return (
        "Strength potion brewed with '" + fire + "' and '" + water + "'"
    )


def healing_potion() -> str:
    earth = create_earth()
    air = create_air()
    return "Healing potion brewed with '" + earth + "' and '" + air + "'"


# alias exposed by package
def heal() -> str:
    return healing_potion()
