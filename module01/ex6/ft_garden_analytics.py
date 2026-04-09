from typing import Any


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            msg = (
                f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                f"{self.show_calls} show"
            )
            print(msg)

    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name.capitalize()
        self.height = float(height)
        self._age = int(age)
        self._stats = Plant._Stats()

    def grow(self, cm: float) -> None:
        self.height += float(cm)
        self._stats.grow_calls += 1

    def age(self, days: int) -> None:
        self._age += int(days)
        self._stats.age_calls += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")
        self._stats.show_calls += 1

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        # simple heuristic to determine seeds after bloom
        self.seeds = int((self.height + self._age) // 3)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self.shade_calls = 0

    def produce_shade(self) -> None:
        self.shade_calls += 1
        length = self.height
        width = self.trunk_diameter
        msg = (
            f"Tree {self.name} now produces a shade of {length:.1f}cm long "
            f"and {width:.1f}cm wide."
        )
        print(msg)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


def display_stats(obj: Any) -> None:
    print(f"[statistics for {obj.name}]")
    # Attempt to display nested stats if present
    stats = getattr(obj, "_stats", None)
    if stats is not None:
        stats.display()
    # Tree-specific shade counter
    if isinstance(obj, Tree):
        print(f"{getattr(obj, 'shade_calls', 0)} shade")


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    # Flower/Seed example
    rose = Seed("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)

    # Tree example
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    # Seed example
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    display_stats(sunflower)
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    # Anonymous
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)


if __name__ == "__main__":
    ft_garden_analytics()
