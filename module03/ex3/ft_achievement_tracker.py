import random


ACHIEVEMENTS_POOL: list[str] = [
    "First Steps",
    "Crafting Genius",
    "Collector Supreme",
    "World Savior",
    "Master Explorer",
    "Hidden Path Finder",
    "Untouchable",
    "Boss Slayer",
    "Unstoppable",
    "Survivor",
    "Speed Runner",
    "Sharp Mind",
    "Treasure Hunter",
    "Strategist",
]


def gen_player_achievements() -> set[str]:
    picked_count: int = random.randint(5, 9)
    picked_achievements: list[str] = random.sample(
        ACHIEVEMENTS_POOL,
        picked_count,
    )
    return set(picked_achievements)


def track_achievements() -> None:
    print("=== Achievement Tracker System ===")

    player_names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets: list[set[str]] = []

    for player_name in player_names:
        current_set: set[str] = gen_player_achievements()
        player_sets.append(current_set)
        print(f"Player {player_name}: {current_set}")

    all_distinct: set[str] = set()
    for current_set in player_sets:
        all_distinct = all_distinct.union(current_set)
    print(f"All distinct achievements: {all_distinct}")

    common_achievements: set[str] = player_sets[0]
    for current_set in player_sets[1:]:
        common_achievements = common_achievements.intersection(current_set)
    print(f"Common achievements: {common_achievements}")

    index: int = 0
    while index < len(player_names):
        other_achievements: set[str] = set()
        other_index: int = 0
        while other_index < len(player_sets):
            if other_index != index:
                other_achievements = other_achievements.union(
                    player_sets[other_index]
                )
            other_index += 1

        only_this_player: set[str] = player_sets[index].difference(
            other_achievements
        )
        print(f"Only {player_names[index]} has: {only_this_player}")
        index += 1

    full_achievements: set[str] = set(ACHIEVEMENTS_POOL)
    index = 0
    while index < len(player_names):
        missing_achievements: set[str] = full_achievements.difference(
            player_sets[index]
        )
        print(f"{player_names[index]} is missing: {missing_achievements}")
        index += 1


if __name__ == "__main__":
    track_achievements()
