from .elements import create_air  # expose air
from .potions import heal as heal  # expose alias used in distillation
from . import transmutation  # expose transmutation subpackage

# purposely do NOT expose create_earth to demonstrate limited interface

__all__ = ["create_air", "heal", "transmutation"]
