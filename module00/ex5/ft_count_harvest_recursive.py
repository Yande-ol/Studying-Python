def ft_count_harvest_recursive():
	limit = int(input("Days until harvest: "))

	def count_recursive(current_day):
		if current_day > limit:
			return
		print("Day", current_day)
		count_recursive(current_day + 1)

	count_recursive(1)
	print("Harvest time!")
