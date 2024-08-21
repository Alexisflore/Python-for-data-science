from typing import Any

def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args: Any, **kwds: Any):
			nonlocal count
			count += 1
			if count <= limit:
				return function(*args, **kwds)
			else:
				print(f"Error <function {function.__name__} at {hex(id(function))}> called to many times")
		return limit_function
	return callLimiter