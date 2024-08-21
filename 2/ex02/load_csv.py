import pandas as pd

def load(path: str) -> pd.DataFrame:
	"""Load the dataset."""
	try :
		df = pd.read_csv(path)
		print(f"Loading dataset of dimensions {df.shape}")
	except FileNotFoundError as e:
		print(f"FileNotFoundError: path {path} not found")
		return None
	return df

# def main() -> int:
# 	path = "data.csv"
# 	print(load(path))
# 	return 0

# if __name__ == '__main__':
# 	main()
