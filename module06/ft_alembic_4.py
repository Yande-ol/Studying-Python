import alchemy
from typing import Any


print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print("Testing create_air:")
print(alchemy.create_air())
print("Now show that not all functions can be reached")
print("This will raise an exception!")

try:
    create_earth_fn: Any = getattr(alchemy, "create_earth")
    print("Testing the hidden create_earth: " + create_earth_fn())
    #print(alchemy.create_earth())
except AttributeError:
    raise
