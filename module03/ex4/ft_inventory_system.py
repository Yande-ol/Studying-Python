import sys


def manage_inventory() -> None:
    raw_items: list[str] = sys.argv[1:]

    print("=== Inventory System Analysis ===")

    if not raw_items:
        print("No inventory provided. Usage: python3 "
              "ft_inventory_system.py <item:quantity> ...")
        return

    inventory: dict[str, int] = {}

    for entry in raw_items:
        parts: list[str] = entry.split(":")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(f"Error - invalid parameter '{entry}'")
            continue

        name: str = parts[0]
        qty_text: str = parts[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            inventory[name] = int(qty_text)
        except ValueError as err:
            print(f"Quantity error for '{name}': {err}")

    if len(inventory) == 0:
        print("No valid items found in inventory.")
        return

    print(f"Got inventory: {inventory}")

    items_list: list[str] = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_units: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_units}")

    for item, qty in inventory.items():
        percentage: float = round((qty / total_units) * 100, 1)
        print(f"Item {item} represents {percentage:.1f}%")

    most_item: str = items_list[0]
    least_item: str = items_list[0]
    for item in items_list:
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item

    print(
        "Item most abundant: "
        f"{most_item} with quantity {inventory[most_item]}"
    )
    print(
        "Item least abundant: "
        f"{least_item} with quantity {inventory[least_item]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    manage_inventory()
