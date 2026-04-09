class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = float(height)
        self._age = int(age)

    def grow(self, cm: float) -> None:
        self.height += float(cm)

    def age(self, days: int) -> None:
        self._age += int(days)

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self._age} days old"


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    print(rose.show())

    initial_height = rose.height
    daily_growth = 0.8
    for day in range(1, 8):
        rose.grow(daily_growth)
        rose.age(1)
        print(f"=== Day {day} ===")
        print(rose.show())

    growth = rose.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
