def garden_operations() -> None:

    print("Testing ValueError...")
    try:
        int("corrompido")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        calculo = 10 / 0
        return calculo
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        open("fake_file.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing KeyError...")
    try:
        estoque = {"tomate": 10}
        item = estoque["alface"]
        return item
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("Testing multiple errors together...")
    try:
        int("erro_novo")
    except (ValueError, ZeroDivisionError, KeyError) as e:
        print(f"Caught an error ({type(e).__name__}), but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Typoes Demo ===")
    garden_operations()
    print("All error tupes tested sucessfully!")


if __name__ == "__main__":
    test_error_types()
