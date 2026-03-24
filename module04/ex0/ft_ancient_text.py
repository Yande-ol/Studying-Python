import os


def recover_ancient_data(filename: str = "ancient_fragment.txt") -> None:

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")

    if not os.path.exists(filename):
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")
    print("RECOVERED DATA:")

    with open(filename, 'r') as vault:
        content = vault.read()
        print(content)

    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    recover_ancient_data()
