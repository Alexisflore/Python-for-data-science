from tqdm import tqdm
from time import sleep

def ft_tqdm(list: range) -> None: # type: ignore
	"""Print the progress bar.""" 
	yield from tqdm(list)

def main() -> None:
	"""Print the progress bar."""
	for elem in ft_tqdm(range(333)):
		sleep(0.005)
	print()
	for elem in tqdm(range(333)):
		sleep(0.005)
	print()

if __name__ == '__main__':
	main()