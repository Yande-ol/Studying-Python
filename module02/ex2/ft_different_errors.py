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
        # TypeError
        raise TypeError("intencional para causar TypeError")
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
    # Demonstrate catching multiple error types with a single except
    print("Testing grouped exception handling...")
    try:
        # this will raise ValueError (int("abc"))
        garden_operations(0)
        # this would raise TypeError, but the previous call already raises
        garden_operations(3)
    except (ValueError, TypeError) as e:
        print(f"Caught ValueError or TypeError: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
