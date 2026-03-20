from typing import Generator


def game_event_stream(count: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    for i in range(1, count + 1):
        p = players[i % 3]
        e = events[i % 3]
        lvl = (i % 15) + 1
        yield f"Event {i}: Player {p} (level {lvl}) {e}"


def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_gen(n: int) -> Generator[int, None, None]:
    count, num = 0, 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def process_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")

    stream = game_event_stream(1000)
    treasure_count = 0
    high_level_count = 0
    levelup_count = 0
    killedmonster_count = 0

    for i, event in enumerate(stream, 1):
        if i <= 3:
            print(event)
        elif i == 4:
            print("...")

        if "killed monster" in event:
            killedmonster_count += 1
        if "leveled up" in event:
            levelup_count += 1
        if "found treasure" in event:
            treasure_count += 1
        pos = event.find("level 1")
        if pos != -1 and any(
            char.isdigit() for char in event[pos + 7: pos + 8]
        ):
            high_level_count += 1

    print("\n=== Stream Analytics ===")
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-Up events: {levelup_count}")
    print(f"Killed_Monster events: {killedmonster_count}")
    print("Memory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")

    fib_nums = [str(n) for n in fibonacci_gen(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_nums)}")

    prime_nums = [str(n) for n in primes_gen(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_nums)}")


if __name__ == "__main__":
    process_stream()
