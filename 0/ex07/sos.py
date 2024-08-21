import sys

def sos(string: str) -> str:
	"""Return the string coded in morse code."""
	NESTED_MORSE = {
		'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
		'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
		'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
		'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
		'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', " ": "/"
	}
	return ' '.join([NESTED_MORSE.get(char.upper(), char) for char in string])

def main() -> int:
	"""Return 0 if the string is coded in morse code."""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("the arguments are bad")
		for char in sys.argv[1]:
			if not char.isalnum() and char != ' ':
				raise AssertionError("the arguments are bad")
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return 1
	print(sos(sys.argv[1]))
	return 0

if __name__ == '__main__':
	sys.exit(main())