def NULL_not_found(object: any) -> int:
	if object == None:
		print("Nothing: None ", end='')
	elif isinstance(object, float) and object != object:
		print("Cheese: nan ", end='')
	elif object == 0:
		print("Zero: 0 ", end='')
	elif object == '':
		print("Empty: ", end='')
	elif object == False:
		print("Fake: False ", end='')
	else:
		print("Type not found ")
		return 1
	objectType = type(object).__name__
	print(f"<class '{objectType}'>")
	return 0

# def main() -> int:
# 	Nothing = None
# 	Garlic = float("NaN")
# 	Zero = 0
# 	Empty = ''
# 	Fake = False
# 	NULL_not_found(Nothing)
# 	NULL_not_found(Garlic)
# 	NULL_not_found(Zero)
# 	NULL_not_found(Empty)
# 	NULL_not_found(Fake)
# 	print(NULL_not_found("Brian"))
# 	return 0

# if __name__ == '__main__':
# 	main()