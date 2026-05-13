def validate_ingredients(ingredients: str) -> str:
    # import inside function to avoid circular import at module load
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = set(light_spell_allowed_ingredients())
    parts = [
        p.strip().lower()
        for p in ingredients.replace("and", ",").replace("&", ",").split(",")
    ]
    valid = any(p in allowed for p in parts if p)
    return "VALID" if valid else "INVALID"
