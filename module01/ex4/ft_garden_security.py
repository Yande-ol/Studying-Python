class SecurePlant:
	def __init__(self, name: str):
		self.name = name
		self._height = 0
		self._age = 0

	def set_height(self, value: int) -> None:
		if value < 0:
			print(f"Invalid operation attempted: height {value}cm [REJECTED]")
			print("Security: Negative height rejected")
		else:
			self._height = value
			print(f"Height update: {value}cm [OK]")

	def set_age(self, value: int) -> None:
		if value < 0:
			print(f"Invalid operation attempted: age {value} ays [REJECTED]")
			print("Security: Negative age rejected")
		else:
			self._age = value
			print(f"Age update: {value} days [OK]")

	def get_height(self) -> int:
		return self._height
	def get_age(self) -> int:
		return self._age
	
def ft_garden_security():
	print("=== Garden Security System ===")
	rose = SecurePlant("Rose")
	print(f"Plant created: {rose.name}")

	rose.set_height(25)
	rose.set_height(30)
	rose.set_age(30)
	rose.set_height(-5)

	print(f"Current plant: {rose.name} ({rose.get_height()}cm, {rose.get_age()})")

if __name__ == "__main__":
	ft_garden_security()