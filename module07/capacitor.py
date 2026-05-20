from typing import cast
from ex1.healing import HealingFactory, IHeal
from ex1.transforming import TransformFactory, ITransform


def test_healing() -> None:
    print("Testing Creature with healing capability")
    f = HealingFactory()
    base = cast(IHeal, f.create_base())
    evo = cast(IHeal, f.create_evolved())
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evo.describe())
    print(evo.attack())
    print(evo.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    f = TransformFactory()
    base = cast(ITransform, f.create_base())
    evo = cast(ITransform, f.create_evolved())
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(f"{base.name} performs a boosted strike!")
    print(base.revert())
    print(" evolved:")
    print(evo.describe())
    print(evo.attack())
    print(evo.transform())
    print(f"{evo.name} unleashes a devastating morph strike!")
    print(evo.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
