import sys


def manage_streams() -> None:

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    print("Input Stream active. ", end="")
    archivist_id: str = input("Enter archivist ID: ")

    print("Input Stream active. ", end="")
    status_report: str = input("Enter status report: ")

    sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")

    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    manage_streams()