from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load as load
from numpy import array

def ft_invert(image: array) -> array:
	"""Invert the image."""
	img = image.copy()
	img = 255 - img
	img = Image.fromarray(img)
	img.show()
	return np.array(img)

def ft_red(image: array) -> array:
	"""Keep only the red channel."""
	img = image.copy()
	img[:, :, 1] = 0
	img[:, :, 2] = 0
	img = Image.fromarray(img)
	img.show()
	return np.array(img)

def ft_green(image: array) -> array:
	"""Keep only the green channel."""
	img = image.copy()
	img[:, :, 0] = 0
	img[:, :, 2] = 0
	img = Image.fromarray(img)
	img.show()
	return np.array(img)

def ft_blue(image: array) -> array:
	"""Keep only the blue channel."""
	img = image.copy()
	img[:, :, 0] = 0
	img[:, :, 1] = 0
	img = Image.fromarray(img)
	img.show()
	return np.array(img)

def ft_grey(image: array) -> array:
	"""Convert the image to grey."""
	img = image.copy()
	img_source = img[:, :, 0]
	img[:, :, 1] = img_source
	img[:, :, 2] = img_source
	img = Image.fromarray(img)
	img.show()
	return np.array(img)

# def main() -> int:
# 	array = load("Image.jpeg")
# 	print(array)
# 	ft_green(array)
# 	ft_invert(array)
# 	ft_red(array)
# 	ft_blue(array)
# 	ft_grey(array)
# 	print(ft_invert.__doc__)
# 	return 0

# if __name__ == '__main__':
# 	main()