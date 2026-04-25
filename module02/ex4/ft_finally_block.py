from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ex3.ft_custom_errors import PlantError  # type: ignore
else:
    try:
        from ex3.ft_custom_errors import PlantError  # type: ignore
    except Exception:
        class PlantError(Exception):
            def __init__(self, message: Optional[str] = None) -> None:
                if message is None:
                    message = "Invalid plant name"
                super().__init__(message)


def water_plant(plant_name: str) -> None:
    """Tenta regar a planta; exige que o nome esteja capitalizado.

    Levanta PlantError se o nome não estiver capitalizado.
    """
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water:'{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
