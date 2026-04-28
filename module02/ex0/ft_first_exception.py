def input_temperature(temp_str: str) -> int:
    """Converte a string de temperatura para inteiro.

    Levanta o erro de conversão se a string não for um número válido.
    """
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test_cases: list[str] = ["25", "abc"]
    for case in test_cases:
        print(f"Input data is '{case}'")
        try:
            temp = input_temperature(case)
            print(f"Temperature is now {temp}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
