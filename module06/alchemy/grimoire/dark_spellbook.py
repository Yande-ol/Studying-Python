def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    # import validator inside function to intentionally still demonstrate
    # circular import errors when validator imports back at module level
    from .dark_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    return f"Dark Spell recorded: {spell_name} ({ingredients} - {result})"
