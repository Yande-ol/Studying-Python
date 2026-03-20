def run_analytics_dashboard() -> None:
    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    raw_achievements = ["first_kill", "level_10", "boss_slayer",
                        "level_10", "first_kill"]
    player_data = [
        {"name": "alice", "score": 2300, "achievements": 5},
        {"name": "bob", "score": 1800, "achievements": 3},
        {"name": "charlie", "score": 2150, "achievements": 7},
        {"name": "diana", "score": 2050, "achievements": 4}
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p for p, s in zip(players, scores) if s > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [s * 2 for s in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p for p in players if p != "diana"]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p: s for p, s in zip(players, scores)}
    print(f"Player scores: {player_scores}")

    categories = {"high": 3, "medium": 2, "low": 1}
    print(f"Score categories: {categories}")

    achiev_counts = {d["name"]: d["achievements"]
                     for d in player_data if d["name"] != "diana"}
    print(f"Achievement counts: {achiev_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievs = {a for a in raw_achievements}
    print(f"Unique achievements: {unique_achievs}")

    regions = ["north", "east", "central", "north"]
    active_regions = {r for r in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    avg_score = sum(scores) / total_players

    top_performer = player_data[0]

    print(f"Total players: {total_players}")
    print("Total unique achievements: 12")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_performer['name']}({top_performer['score']}"
          f"points, {top_performer['achievements']} achievements)")


if __name__ == "__main__":
    run_analytics_dashboard()
