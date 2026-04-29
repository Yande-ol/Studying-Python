import sys
from typing import IO


def recover_ancient_text() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        vault_file: IO[str] = open(filename, "r")
        print("---")
        content: str = vault_file.read()
        print(content, end="")
        print("---")
        vault_file.close()
        print(f"File '{filename}' closed.")
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file '{filename}': {err}")


if __name__ == "__main__":
    recover_ancient_text()
