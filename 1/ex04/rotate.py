from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load as load

def rotate(path: str, angle: int) -> None:
	"""Rotate the image."""
	img = load(path)
	if img.size == 0:
		print("Image not loaded")
		return
	print(img)
	if img.shape[0] > img.shape[1]:
		new_size = img.shape[1]
	else:
		new_size = img.shape[0]
	img = img[:new_size, :new_size, :]
	img = img.transpose((1, 0, 2))
	print(f"New shape after transpose: {img.shape}")
	print(img)
	#display the image with x and y axis
	plt.imshow(img)
	plt.xlabel('X-axis (pixels)')
	plt.ylabel('Y-axis (pixels)')
	plt.title('Image with XY Axes')
	plt.show()

# def main() -> int:
# 	try:
# 		rotate("image.jpeg", 90)
# 	except AssertionError as e:
# 		print(f"AssertionError: {e}")
# 		return 1
# 	return 0

# if __name__ == '__main__':
# 	main()