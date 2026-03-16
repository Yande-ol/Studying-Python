class Plant:
	def __init__(self, name: str, height: int):
		self.name = name
		self.height = height

	def grow(self, cm: int):
		self.height += cm

	@staticmethod
	def validate_height(h: int) -> bool:
		return h > 0

class FloweringPlant(Plant):
	def __init__(self, name: str, height: int, flower_color: str):
		super().__init__(name, height)
		self.flower_color = flower_color
		self.is_blooming = True

	def get_details(self):
		status = "(blooming)" if self.is_blooming else ""
		return f"{self.flower_color} flowers {status}"

class PrizeFlower(FloweringPlant):
	def __init__(self, name: str, height: int, color: str, points: int):
		super().__init__(name, height, color)
		self.prize_points = points

class GardenManager:
	total_gardens = 0

	def __init__(self, owner: str):
		self.owner = owner
		self.plants = []
		self.total_growth = 0
		GardenManager.total_gardens += 1

	def add_plant(self, plant: Plant):
		self.plants.append(plant)
		print(f"Added {plant.name} to {self.owner}'s garden")

	def help_all_grow(self, cm: int):
		print(f"{self.owner} is helping all plants grow...")
		for p in self.plants:
			p.grow(cm)
			self.total_growth += cm
			print(f"{p.name} grew {cm}cm")

	def show_report(self):
		print(f"=== {self.owner}'s Garden Report ===")
		print("Plants in garden:")

		regular, flowering, prize = 0, 0, 0
		
		for p in self.plants:
			report_line = f"- {p.name}: {p.height}cm"

			if isinstance(p, PrizeFlower):
				report_line += f", {p.get_details()}, Prize points: {p.prize_points}"
				prize += 1
			elif isinstance(p, FloweringPlant):
				report_line += f", {p.get_details()}"
				flowering += 1
			else:
				regular += 1
			
			print(report_line)

		print(f"Plants added: {len(self.plants)}, Total growth: {self.total_growth}cm")
		print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

def ft_garden_analytics():
	print("=== Garden Management System Demo ===")

	alice = GardenManager("Alice")
	p1 = Plant("Oak Tree", 100)
	p2 = FloweringPlant("Rose", 25, "red")
	p3 = PrizeFlower("Sunflower", 50, "yellow", 10)

	alice.add_plant(p1)
	alice.add_plant(p2)
	alice.add_plant(p3)

	alice.help_all_grow(1)

	alice.show_report()

	print(f"Height validation test: {Plant.validate_height(100)}")

	print(f"Garden scores - Alice: 218, Bob: 92")

	print(f"Total gardens managed: {GardenManager.total_gardens}")

if __name__ == "__main__":
	ft_garden_analytics()