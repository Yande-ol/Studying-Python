class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        try:
            if not name:
                raise GardenError("Plant name cannot be empty!")
            self.plants.append(name)
            print(f"Added {name} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_all(self) -> None:
        print("\nOpening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water! Tank remains full.")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Watering Alert: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        try:
            print(f"Checking {name}...")
            if water > 10:
                raise GardenError(f"Water level {water} is too high (max 10)")
            print(f"{name}: healthy (water: {water}, sun: {sun})")
        except GardenError as e:
            print(f"Error checking {name}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    gm = GardenManager()

    print("Adding plants to garden...")
    gm.add_plant("tomato")
    gm.add_plant("lettuce")
    gm.add_plant("")

    print("\nWatering plants...")
    gm.water_all()

    print("\nChecking plant health...")
    gm.check_health("tomato", 5, 8)
    gm.check_health("lettuce", 15, 10)
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
