def validate_ingredients(ingredients: str) -> str:
    # intentionally import the allowed list from dark_spellbook to create a
    # circular import when dark_spellbook also imports this module at
    # top-level
    from .dark_spellbook import dark_spell_allowed_ingredients

    allowed = set(dark_spell_allowed_ingredients())
    parts = [
        p.strip().lower()
        for p in ingredients.replace("and", ",").replace("&", ",").split(",")
    ]
    valid = any(p in allowed for p in parts if p)
    return "VALID" if valid else "INVALID"
