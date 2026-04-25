def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        # ValueError
        int("abc")
    elif operation_number == 1:
        # ZeroDivisionError
        _ = 1 / 0
    elif operation_number == 2:
        # FileNotFoundError
        open("/non/existent/file", "r")
    elif operation_number == 3:
        # TypeError (int + str) — use exec so mypy doesn't flag the operator
        exec('_ = "text" + 5')
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
