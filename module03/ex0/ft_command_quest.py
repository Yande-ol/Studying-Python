import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    argc: int = len(sys.argv)
    if argc < 2:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if argc >= 2:
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {argc}")
