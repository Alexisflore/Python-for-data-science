def count_characters(input_text: str) -> dict:
	"""
	Count the number of characters, upper letters, lower letters, punctuation marks, spaces, and digits in the input text.
	"""
	dict_types = { "characters": 0, "upper letters": 0,  "lower letters": 0,  "punctuation marks": 0, "spaces": 0, "digits": 0}
	
	for character in input_text:
		if character.isdigit():
			dict_types["digits"] += 1
		elif character.isspace() and character != "\n":
			dict_types["spaces"] += 1
		elif character.isalpha():
			if character.islower():
				dict_types["lower letters"] += 1
			elif character.isupper():
				dict_types["upper letters"] += 1
		else:
			dict_types["punctuation marks"] += 1
		dict_types["characters"] += 1
	return dict_types

def print_dict(dict_types: dict) -> None:
	"""
	Print the number of characters, upper letters, lower letters, punctuation marks, spaces, and digits in the input text.
	"""
	print(f"The text contains ", end="")
	for key, value in dict_types.items():
		print(f"{value} {key}")
 
def main() -> int:
	try:
		if len(sys.argv) > 2:
			raise AssertionError("more than one argument is provided")
		if len(sys.argv) == 1:
			try:
				input_text = input("What is the text to count?\n") + "\r"
			except EOFError:
				pass
		else:
			input_text = sys.argv[1] + "\n"
		dict_types = count_characters(input_text)
		print_dict(dict_types)
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return 1
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main())