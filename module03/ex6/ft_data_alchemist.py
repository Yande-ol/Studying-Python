import random


def run_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    already_capitalized: list[str] = [
        name for name in players if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dict: dict[str, int] = {
        name: random.randint(50, 1000) for name in all_capitalized
    }
    print(f"Score dict: {score_dict}")

    score_average: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(score_average, 2)}")

    high_scores: dict[str, int] = {
        name: score
        for name, score in score_dict.items()
        if score > score_average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    run_data_alchemist()
