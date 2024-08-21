from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def aff_life(df: pd.DataFrame) -> None:
	"""Display the row of France in a graph."""
	country_name = 'France'
	country_data = df[df['country'] == 'France']

	country_data = country_data.melt(id_vars=['country'], var_name='Year', value_name='Life Expectancy')

	# Convert the 'Year' column to integer
	country_data['Year'] = country_data['Year'].astype(int)
	plt.figure(figsize=(10, 6))
	plt.plot(country_data['Year'], country_data['Life Expectancy'])
	plt.title(f'Evolution of Life Expectancy in {country_name} Over Time')
	plt.xlabel('Year')
	plt.ylabel('Life Expectancy (Years)')
	plt.grid(True)
	plt.show()

def main() -> int:
	path = "life_expectancy_years.csv"
	df = load(path)
	aff_life(df)
	return 0

if __name__ == '__main__':
	main()