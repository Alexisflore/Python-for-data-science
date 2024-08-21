from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
	vector = list(args)
	if not all(isinstance(x, (int, float)) for x in vector):
		print("ERROR")
		return
	
	if "mean" in kwargs.values():
		if len(vector) == 0:
			print("ERROR")
		else:
			print(f"Mean: {sum(vector) / len(vector)}")
	
	if "median" in kwargs.values():
		if len(vector) == 0:
			print("ERROR")
		else:
			vector.sort()
			if len(vector) % 2 == 0:
				print(f"Median: {(vector[len(vector) // 2] + vector[len(vector) // 2 - 1]) / 2}")
			else:
				print(f"Median: {vector[len(vector) // 2]}")
		
	if "quartile" in kwargs.values():
		if len(vector) == 0:
			print("ERROR")
		else:
			vector.sort()
			if len(vector) % 2 == 0:
				print(f"[{vector[len(vector) // 4]}, {vector[3 * len(vector) // 4]}]")
			else:
				print(f"[{vector[len(vector) // 4]}, {vector[3 * len(vector) // 4]}]")
	
	if "std" in kwargs.values():
		if len(vector) == 0:
			print("ERROR")
		else:
			mean = sum(vector) / len(vector)
			print(f"Std: {(sum([(x - mean) ** 2 for x in vector]) / len(vector) )** 0.5}")

	if "var" in kwargs.values():
		if len(vector) == 0:
			print("ERROR")
		else:
			mean = sum(vector) / len(vector)
			print(f"Var: {sum([(x - mean) ** 2 for x in vector]) / len(vector)}")
	