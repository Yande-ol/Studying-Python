
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def ft_garden_data() -> None:
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")

    for p in (p1, p2, p3):
        p.show()


if __name__ == "__main__":
    ft_garden_data()
