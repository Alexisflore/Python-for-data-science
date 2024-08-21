def all_thing_is_obj(object: any) -> int:
	if object == None:
		return 42
	objectType = type(object).__name__
	if objectType == "str":
		print(f"{object} is in the kitchen : <class 'str'>")
	elif objectType == "int":
		print("Type not found")
	else:
		print(f"{objectType.capitalize()} : <class '{objectType}'>")
	return 42

# def main() -> int:
# 	ft_list = ["Hello", "tata!"]
# 	ft_tuple = ("Hello", "toto!")
# 	ft_set = {"Hello", "tutu!"}
# 	ft_dict = {"Hello" : "titi!"}
# 	all_thing_is_obj(ft_list)
# 	all_thing_is_obj(ft_tuple)
# 	all_thing_is_obj(ft_set)
# 	all_thing_is_obj(ft_dict)
# 	all_thing_is_obj("Brian")
# 	all_thing_is_obj("Toto")
# 	print(all_thing_is_obj(10))
# 	return 0

# if __name__ == '__main__':
# 	main()