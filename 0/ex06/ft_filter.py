def ft_filter(function, iterable):
	"""filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
	return [item for item in iterable if function(item)]

# def main() -> int:
# 	"""
# 	Compare this snippet from ex05/building.py:
# 	"""
# 	tab_ft = ft_filter(lambda x: x % 2 == 0, range(10))
# 	tab = (filter(lambda x: x % 2 == 0, range(10)))
# 	print(list(tab_ft))
# 	print(list(tab))
# 	print(filter.__doc__)
# 	print(ft_filter.__doc__)
# 	return 0

# if __name__ == '__main__':
# 	import sys
# 	sys.exit(main())