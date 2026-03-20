def track_achievements() -> None:

    print("=== Achievement Tracker System ===")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common}")

    alice_only_vs_bob = alice.difference(bob)
    print(f"Alice unique vs Bob: {alice_only_vs_bob}")

    rare = (alice - bob - charlie) | (bob - alice - charlie)
    (charlie - alice - bob)
    print(f"Rare achievements (only 1 player has): {rare}")


if __name__ == "__main__":
    track_achievements()
