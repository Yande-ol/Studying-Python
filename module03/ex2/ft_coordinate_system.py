import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_value: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = raw_value.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        x_text: str = parts[0].strip()
        y_text: str = parts[1].strip()
        z_text: str = parts[2].strip()

        try:
            x_value: float = float(x_text)
            y_value: float = float(y_text)
            z_value: float = float(z_text)
        except ValueError as err:
            bad_value: str = ""
            for value_text in (x_text, y_text, z_text):
                try:
                    float(value_text)
                except ValueError:
                    bad_value = value_text
                    break
            print(f"Error on parameter '{bad_value}': {err}")
            continue

        return (x_value, y_value, z_value)


def track_position() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first_pos: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(
        f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}"
    )

    center_distance: float = math.sqrt(
        first_pos[0] ** 2 + first_pos[1] ** 2 + first_pos[2] ** 2
    )
    print(f"Distance to center: {center_distance:.4f}")

    print("Get a second set of coordinates")
    second_pos: tuple[float, float, float] = get_player_pos()

    between_distance: float = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{between_distance:.4f}"
    )


if __name__ == "__main__":
    track_position()
