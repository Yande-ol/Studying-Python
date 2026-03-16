class Plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age

def ft_plant_factory():

	plants = [
		Plant("Rose", 25, 30),
		Plant("0ak", 200, 365),
		Plant("Cactus", 5, 90),
		Plant("Sunflower", 80, 45),
		Plant("Fern", 15, 120)
	]

	print("=== Plant Factory Output ===")

	for p in plants:
		print(f"Created: {p.name} ({p.height}cm, {p.age})")

	print(f"Total plants created: {len(plants)}")

if __name__ == "__main__":
	ft_plant_factory()