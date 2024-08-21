import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""Return the sliced list."""
	size_of_list = len(family[0])
	if (start < 0 and start < - len(family)) or (end < 0 and end < - len(family)):
		raise AssertionError("the arguments areee bad")
	if start >= len(family) or end >= len(family):
		raise AssertionError("the arguments are baqqd")
	if start < 0:
		start += len(family)
	if end < 0:
		end += len(family)
	if start > end:
		raise AssertionError("the argumeeeeents are bad")
	if end - start < 1:
		raise AssertionError("the argumennnnnnnts are bad")
	for i, j in enumerate(family):
		if not isinstance(family[i], list) and len(family[i]) != size_of_list:
			raise AssertionError("the argumentsssssss are bad")
	print(f"My shape is : {np.array(family).shape}")
	family = np.array(family)
	family = family[start:end]
	print(f"My new shape is : {family.shape}")
	return family.tolist()

def main() -> int:
	try:	
		family = [[1.80, 78.4],
		[2.15, 102.7],
		[2.10, 98.5],
		[1.88, 75.2]]
		print(slice_me(family, 0, 2))
		print(slice_me(family, 1, -2))
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return 1
	return 0

if __name__ == '__main__':
	main()