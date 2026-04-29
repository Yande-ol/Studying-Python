import sys
from typing import IO


def recover_ancient_text(filename: str) -> str:
    """Read file and return content. Raises on error."""
    try:
        vault_file: IO[str] = open(filename, "r")
        content: str = vault_file.read()
        vault_file.close()
        return content
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file '{filename}': {err}")
        raise


def process_archive_creation() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        content: str = recover_ancient_text(filename)
        print("---")
        print(content, end="")
        print("---")
        print(f"File '{filename}' closed.")
    except (FileNotFoundError, PermissionError):
        return

    print("Transform data:")
    print("---")
    lines: list[str] = content.rstrip("\n").split("\n")
    transformed: list[str] = [line + "#" for line in lines]
    transformed_content: str = "\n".join(transformed)
    print(transformed_content)
    print("---")

    output_filename: str = input("Enter new file name (or empty): ").strip()

    if output_filename:
        try:
            output_file: IO[str] = open(output_filename, "w")
            output_file.write(transformed_content)
            output_file.close()
            print(f"Saving data to '{output_filename}'")
            print(f"Data saved in file '{output_filename}'.")
        except (FileNotFoundError, PermissionError) as err:
            print(f"Error opening file '{output_filename}': {err}")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    process_archive_creation()
