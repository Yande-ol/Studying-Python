import os


def handle_crisis(filename: str) -> None:

    print(f"CRISIS ALERT: Attempting access to '{filename}'")
    
    try:
        with open(filename, "r") as vault:
            content = vault.read().strip()
            print("...")
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
            
    except FileNotFoundError:
        print("...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        
    except PermissionError:
        print("...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        
    except Exception as e:
        print("...")
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, anomaly contained")

def run_crisis_test() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    
    handle_crisis("lost_archive.txt")
    print()

    handle_crisis("classified_vault.txt")
    print()

    handle_crisis("standard_archive.txt")
    
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    run_crisis_test()
