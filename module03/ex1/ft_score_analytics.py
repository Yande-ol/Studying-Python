import sys


def analyze_scores() -> None:
    argc: int = len(sys.argv)

    print("=== Player Score Analytics ===")

    if argc < 2:
        print("No scores provided."
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []

    try:
        for i in range(1, argc):
            value = int(sys.argv[i])
            scores.append(value)

    except ValueError:
        print("Error: All arguments must be numeric scores (integers).")
        return

    total_players = len(scores)
    total_sum = sum(scores)
    avg = total_sum / total_players

    high = max(scores)
    low = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_sum}")
    print(f"Average score: {avg:.1f}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    analyze_scores()
