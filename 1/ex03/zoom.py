from PIL import Image
import numpy as np
from load_image import ft_load as load_image
import matplotlib.pyplot as plt

def zoom(path: str, factor: int) -> None:
	"""Zoom the image."""
	img = load_image(path)
	print(img)
	if img.size == 0:
		print("Image not loaded")
		return
	img = img[:round(img.shape[0] / factor), :round(img.shape[1] / factor), 1]
	print(f"New shape after slicing: {img.shape}")
	print(img)
	img = Image.fromarray(img)
	#display the image with x and y axis
	plt.imshow(img, cmap='gray')
	plt.xlabel('X-axis (pixels)')
	plt.ylabel('Y-axis (pixels)')
	plt.title('Image with XY Axes')
	plt.show()

# def main() -> int:
# 	try:
# 		zoom("image.jpeg", 2)
# 	except AssertionError as e:
# 		print(f"AssertionError: {e}")
# 		return 1
# 	return 0

# if __name__ == '__main__':
# 	main()