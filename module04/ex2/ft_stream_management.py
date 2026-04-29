import sys
from typing import IO


def recover_ancient_text(filename: str) -> str:
    """Read file and return content. Raises on error."""
    try:
        vault_file: IO[str] = open(filename, "r")
        content: str = vault_file.read()
        vault_file.close()
        return content
    except OSError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {err}\n")
        raise


def process_archive_creation() -> None:
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ft_stream_management.py <file>\n")
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
    except OSError:
        return

    print("Transform data:")
    print("---")
    lines: list[str] = content.rstrip("\n").split("\n")
    transformed: list[str] = [line + "#" for line in lines]
    transformed_content: str = "\n".join(transformed)
    print(transformed_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    output_filename: str = sys.stdin.readline().strip()

    if output_filename:
        print(f"Saving data to '{output_filename}'")
        try:
            output_file: IO[str] = open(output_filename, "w")
            output_file.write(transformed_content)
            output_file.close()
            print(f"Data saved in file '{output_filename}'.")
        except OSError as err:
            sys.stderr.write(
                f"[STDERR] Error opening file '{output_filename}': {err}\n"
            )
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    process_archive_creation()
