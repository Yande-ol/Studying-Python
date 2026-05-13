def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # validator import is inside function to avoid circular import during
    # module initialization
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} - {result})"
