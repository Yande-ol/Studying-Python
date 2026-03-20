import sys


def manage_inventory() -> None:
    raw_items = sys.argv[1:]

    print("=== Inventory System Analysis ===")

    if not raw_items:
        print("No items provided. Usage: python3"
              "ft_inventory_system.py item:qty item:qty ...")
        return

    inventory: dict[str, int] = {}

    for entry in raw_items:
        try:
            name, qty = entry.split(":")
            inventory[name] = int(qty)
        except (ValueError, IndexError):
            print(f"Skipping invalid entry: {entry}")

    total_units = sum(inventory.values())
    unique_types = len(inventory)

    most_abundant = max(inventory, key=inventory.get)
    least_abundant = min(inventory, key=inventory.get)

    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    sorted_inventory = dict(sorted(inventory.items(),
                                   key=lambda x: x[1], reverse=True)) # importante para organização.
    for item, qty in sorted_inventory.items():
        percentage = (qty / total_units) * 100
        print(f"{item}: {qty} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(
        f"Least abundant: {least_abundant} "
        f"({inventory[least_abundant]} unit)"
    )

    categories = {"Moderate": {}, "Scarce": {}}

    for item, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    restock = [item for item, qty in inventory.items() if qty == 1]
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {', '.join(restock)}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    manage_inventory()
