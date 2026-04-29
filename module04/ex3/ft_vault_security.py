def secure_archive(
    filename: str, action: str, content: str | None = None
) -> tuple[bool, str]:
    """
    Secure file operations using context manager (with statement).

    Args:
        filename: Name of the file to access.
        action: Either 'read' or 'write'.
        content: Content to write (required if action is 'write').

    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        if action == "read":
            with open(filename, "r") as vault_file:
                data: str = vault_file.read()
            return (True, data)
        elif action == "write":
            if content is None:
                return (False, "Content required for write operation")
            with open(filename, "w") as vault_file:
                vault_file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Unknown action: {action}")
    except FileNotFoundError as err:
        return (False, str(err))
    except PermissionError as err:
        return (False, str(err))
    except Exception as err:
        return (False, str(err))


def test_vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result: tuple[bool, str] = secure_archive("/not/existing/file", "read")
    print(result)

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd", "read")
    print(result)

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        write_result: tuple[bool, str] = secure_archive(
            "new_archive.txt", "write", result[1]
        )
        print(write_result)


if __name__ == "__main__":
    test_vault_security()
