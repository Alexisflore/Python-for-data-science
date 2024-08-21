import sys

#!/usr/bin/env python


def main() -> int:
	try:
		if len(sys.argv) != 2:
			raise AssertionError("more than one argument is provided")
		number = sys.argv[1]
		if not (((number[0] == '-' or number[0] == '+') and number[1:].isdigit()) or number.isdigit()):
			raise AssertionError("argument is not an integer")
		if int(sys.argv[1]) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return 1
	return 0

if __name__ == '__main__':
	sys.exit(main())