class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_system() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        check_water_system()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        check_plant_health()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water_system()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
