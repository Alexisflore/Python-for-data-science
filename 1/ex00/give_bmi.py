# import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""Return the BMI of the people."""
	if len(height) != len(weight):
		raise AssertionError("the arguments are bad")
	for i in range(len(height)):
		if not isinstance(height[i], (int, float)) or not isinstance(weight[i], (int, float)):
			raise AssertionError("the arguments are bad")
		if height[i] <= 0 or weight[i] <= 0:
			raise AssertionError("the arguments are bad")
	return [weight[i] / (height[i] ** 2) for i, weigh in enumerate(weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""Return True if the BMI is higher than the limit."""
	if not isinstance(limit, int) or limit <= 0:
		raise AssertionError("the arguments are bad")
	for i in range(len(bmi)):
		if not isinstance(bmi[i], (int, float)) or bmi[i] <= 0:
			raise AssertionError("the arguments are bad")
	return [True if elem > limit else False for elem in bmi]

# def main() -> int:
# 	try:
# 		height = [2.71, 1.15]
# 		weight = [165.3, 38.4]
# 		bmi = give_bmi(height, weight)
# 		print(bmi, type(bmi))
# 		print(apply_limit(bmi, 26))
# 	except AssertionError as e:
# 		print(f"AssertionError: {e}")
# 		return 1
# 	return 0

# if __name__ == '__main__':
# 	main()