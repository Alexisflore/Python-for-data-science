import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
	"""Load the image."""
	try :
		img = Image.open(path)
		img = img.convert("RGB")
		img = np.array(img)
		print(f"The shape of the image is: {img.shape}")
	except FileNotFoundError as e:
		print(f"FileNotFoundError: path {path} not found")
		return np.array([])
	return img

# def main() -> int:
# 	path = "imagqe.jpeg"
# 	print(ft_load(path))
# 	return 0

# if __name__ == '__main__':
# 	main()