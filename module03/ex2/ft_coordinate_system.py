import math


def track_position() -> None:

    print("=== Game Coordinate System ===")

    start_pos: tuple[int, int, int] = (0, 0, 0)

    current_pos: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {current_pos}")

    dist = math.sqrt(
        (current_pos[0] - start_pos[0])**2 +
        (current_pos[1] - start_pos[1])**2 +
        (current_pos[2] - start_pos[2])**2
    )
    print(f"Distance between {start_pos} and {current_pos}: {dist:.2f}")

    coord_string = "3,4,0"
    print(f'Parsing coordinates: "{coord_string}"')

    try:
        parts = coord_string.split(",")
        parsed_pos = (int(parts[0]), int(parts[1]), int(parts[2]))
        print(f"Parsed position: {parsed_pos}")

        dist_new = math.sqrt(parsed_pos[0]**2
                             + parsed_pos[1]**2 + parsed_pos[2]**2)
        print(f"Distance between (0, 0, 0) and {parsed_pos}: {dist_new:.1f}")

    except (ValueError, IndexError) as e:
        print(f"Error parsing coordinates: {e}")
        return

    x, y, z = parsed_pos
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    track_position()
