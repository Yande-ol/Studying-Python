import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events_list) > 0:
        event_index: int = random.randrange(len(events_list))
        yield events_list.pop(event_index)


def process_stream() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        current_event: tuple[str, str] = next(event_generator)
        print(
            "Event "
            f"{i}: Player {current_event[0]} did action {current_event[1]}"
        )

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_generator))
    print(f"Built list of 10 events: {ten_events}")

    for consumed_event in consume_event(ten_events):
        print(f"Got event from list: {consumed_event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    process_stream()
