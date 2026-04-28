import sys


def analyze_scores() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = []
    i: int = 1
    while i < len(sys.argv):
        value_text: str = sys.argv[i]
        try:
            value: int = int(value_text)
            scores.append(value)
        except ValueError:
            print(f"Invalid parameter: '{value_text}'")
        i += 1

    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    total_players: int = len(scores)
    total_sum: int = sum(scores)
    avg: float = total_sum / total_players

    high: int = max(scores)
    low: int = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_sum}")
    print(f"Average score: {avg:.1f}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    analyze_scores()
