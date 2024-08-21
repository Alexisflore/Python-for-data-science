from ft_filter import ft_filter
import sys

def string_filter(string: str, number: int) -> list:
	"""
	Return the list of all the word that have a length superior to the number.
	"""
	return ft_filter(lambda x: len(x) > number, string.split())

def main() -> int:
	"""
	Compare this snippet from ex05/building.py:
	"""
	try:
		if len(sys.argv) != 3:
			raise AssertionError("the arguments are bad")
		if not sys.argv[2].isdigit():
			raise AssertionError("the argument are bad")
		print(string_filter(sys.argv[1], int(sys.argv[2])))
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return 1
	return 0

if __name__ == '__main__':
	sys.exit(main())