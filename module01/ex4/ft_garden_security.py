class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0):
        self._name = name.capitalize()
        # protected attributes
        self._height = float(0.0)
        self._age = int(0)

        # initialize with validation
        if height >= 0:
            self._height = float(height)
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Plant created with default height")
        if age >= 0:
            self._age = int(age)
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Plant created with default age")

    def get_name(self) -> str:
        return self._name

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(value)
            numeric_value = float(value)
            if numeric_value.is_integer():
                formatted_value = str(int(numeric_value))
            else:
                formatted_value = str(numeric_value)
            print(f"Height updated: {formatted_value}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(value)
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()

    # valid updates
    rose.set_height(25)
    rose.set_age(30)

    # invalid updates
    rose.set_height(-5)
    rose.set_age(-10)

    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
