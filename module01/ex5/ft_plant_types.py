class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = float(height)
        self._age = int(age)

    def grow(self, cm: float) -> None:
        self.height += float(cm)

    def age(self, days: int) -> None:
        self._age += int(days)

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
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


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, cm: float) -> None:
        super().grow(cm)
        # growing may increase nutritional value slightly
        self.nutritional_value += int(cm // 1)

    def age(self, days: int) -> None:
        super().age(days)
        # aging increases readiness / nutritional value
        self.nutritional_value += int(days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    # Flower
    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    # Tree
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    # Vegetable
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
