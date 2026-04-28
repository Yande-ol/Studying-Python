import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    program_name: str = sys.argv[0].split("/")[-1]
    print(f"Program name: {program_name}")

    argc: int = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i: int = 1
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {argc}")
