class Plant:

	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age

def ft_garden_data():

	p1 = Plant("Rose", 25, 30)
	p2 = Plant("sunflower", 80, 45)
	p3 = Plant("Cactus", 15, 120)
	print("=== Garden Plant Registry ===")

	for p in[p1, p2, p3]:
		print(f"{p.name}: {p.height}cm, {p.age} days old")

if __name__ == "__main__":
	ft_garden_data()