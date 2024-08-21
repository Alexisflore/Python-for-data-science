class calculator:

	def __init__(self, values) -> None:
		self.values = values


	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		if len(V1) != len(V2):
			print("Vectors must have the same length")
			return
		value = sum([V1[i] * V2[i] for i in range(len(V1))])
		print(f"Dot product is: {value}")
	
	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		if len(V1) != len(V2):
			print("Vectors must have the same length")
			return
		print("Add vector is: ", end="")
		print([V1[i] + V2[i] for i in range(len(V1))])

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		if len(V1) != len(V2):
			print("Vectors must have the same length")
			return
		print("Sous vector is: ", end="")
		print([V1[i] - V2[i] for i in range(len(V1))])