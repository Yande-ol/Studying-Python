def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a.get('power', 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m.get('power', 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m.get('power', 0), mages))
    if not powers:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    mx = max(powers)
    mn = min(powers)
    avg = round(sum(powers) / len(powers), 2)
    return {'max_power': mx, 'min_power': mn, 'avg_power': avg}


if __name__ == '__main__':
    print('Testing artifact sorter...')
    artifacts = [{'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
                 {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'}]
    sorted_a = artifact_sorter(artifacts)
    print(
        f"{sorted_a[0]['name']} ({sorted_a[0]['power']} power) comes before "
        f"{sorted_a[1]['name']} ({sorted_a[1]['power']} power)"
    )
    print('Testing spell transformer...')
    spells = ['fireball', 'heal', 'shield']
    print(' '.join(spell_transformer(spells)))
