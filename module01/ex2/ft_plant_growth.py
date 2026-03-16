class Plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age

	def grow(self, cm: int):
		self.height += cm

	def age_plant(self, days: int):
		self.age += days

	def get_info(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

def ft_plant_growth():
	rose = Plant("Rose", 25, 30)
	print("=== Day 1 ===")
	print(rose.get_info())

	rose.grow(6)
	rose.age_plant(7)

	print("=== Day 7 ===")
	print(rose.get_info())
	print("Growth this week: +6cm")

if __name__== "__main__":
	ft_plant_growth()