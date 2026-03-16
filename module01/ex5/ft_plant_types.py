class Plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age

class Flower(Plant):
	def __init__(self, name: str, height:int, age: int, color: str):
		super().__init__(name, height, age)
		self.color = color

	def bloom(self):
		print(f"{self.name} is blooming beutifully!")

class Tree(Plant):
	def __init__(self, name: str, height: int, age: int, trunk_diamenter: int):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diamenter

	def produce_shade(self):
		shade_area = self.height * 0.15
		print(f"{self.name} provides {shade_area: 1f} square meters of shade")

class Vedgetable(Plant):
	def __init__(self, name: str, height: int, age: int, harvest_season: str):
		super().__init__(name, height, age)
		self.harvest_season = harvest_season

	def nutrition_info(self):
		print(f"{self.name} is rich in vitamins and ready for {self.harvest_season} harvest")

def ft_plant_types():
	print("=== Garden Plant Types ===")

	rose = Flower("Rose", 25, 30, "red")
	oak = Tree("Oak", 500, 1825, 50)
	tomato = Vedgetable("Tomato", 80, 90, "summer")

	print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} color")
	rose.bloom()
	print(f"\n{oak.name} (Tree): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
	oak.produce_shade()
	print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, {tomato.harvest_season} harvest")
	tomato.nutrition_info()

if __name__ == "__main__":
	ft_plant_types()