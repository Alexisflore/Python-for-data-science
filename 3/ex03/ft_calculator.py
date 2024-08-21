class calculator:

	def __init__(self, values) -> None:
		self.values = values

	def __add__(self, object) -> None:
		self.values = [x + object for x in self.values]
		print(self.values)
	
	def __sub__(self, object) -> None:
		self.values = [x - object for x in self.values]
		print(self.values)
	
	def __mul__(self, object) -> None:
		self.values = [x * object for x in self.values]
		print(self.values)
	
	def __truediv__(self, object) -> None:
		if object == 0:
			print("Division by 0")
			return
		self.values = [x / object for x in self.values]
		print(self.values)