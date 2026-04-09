class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = float(height)
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for p in plants:
        print(f"Created: {p.show()}")


if __name__ == "__main__":
    ft_plant_factory()
