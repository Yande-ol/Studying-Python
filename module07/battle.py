from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    print("\nTesting factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(f1, f2) -> None:
    print("\nTesting battle")
    a = f1.create_base()
    b = f2.create_base()
    print(a.describe())
    print("vs.")
    print(b.describe())
    print("fight!")
    print(a.attack())
    print(b.attack())


if __name__ == "__main__":
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    battle(FlameFactory(), AquaFactory())
