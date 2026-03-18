def check_temperature(temp_str: str) -> int | None:
    try:
        temp: int = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plant (min 0°C)")
            return None
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plant (max 40°C)")
            return None
        print(f"Temperature {temp}°C is perfect for plant!")
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:

    print("=== Garden Temperature Checker ===")
    test_cases: list[str] = ["25", "abc", "100", "-50"]
    for case in test_cases:
        print(f"Testing temperature: {case}")
        check_temperature(case)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
