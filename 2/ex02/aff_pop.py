from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def aff_pop(df: pd.DataFrame) -> None:
	"""Display the row of France in a graph."""

	# Display the row of France and Germany in a graph
	def convert_population(pop_str):
		"""Convert population string with 'M' or 'k' into numeric values."""
		if 'M' in pop_str:
			return float(pop_str.replace('M', '')) * 1e6
		elif 'k' in pop_str:
			return float(pop_str.replace('k', '')) * 1e3
		elif 'B' in pop_str:
			return float(pop_str.replace('B', '')) * 1e9
		else:
			return float(pop_str)
    
	# Apply the conversion to all data (except the 'country' column)
	df.iloc[:, 1:] = df.iloc[:, 1:].applymap(convert_population)
	country_name1 = 'France'
	country_name2 = 'Belgium'

	# Filter data for France and Germany
	country_data1 = df[df['country'] == country_name1]
	country_data2 = df[df['country'] == country_name2]

	# Reshape the data to have years as a column
	country_data1 = country_data1.melt(id_vars=['country'], var_name='Year', value_name='Population')
	country_data2 = country_data2.melt(id_vars=['country'], var_name='Year', value_name='Population')

	# Convert the 'Year' column to integer
	country_data1['Year'] = country_data1['Year'].astype(int)
	country_data2['Year'] = country_data2['Year'].astype(int)

	# Plot the data for both countries
	plt.figure(figsize=(10, 6))
	plt.plot(country_data1['Year'], country_data1['Population'], label=country_name1, color='red')
	plt.plot(country_data2['Year'], country_data2['Population'], label=country_name2, color='blue')

	# Set labels and title
	plt.xlabel('Year')
	plt.ylabel('Population')
	plt.title(f'Population of {country_name1} and {country_name2}')
	plt.legend()

	# Display the plot
	plt.show()

# def main() -> int:
# 	df = load('population_total.csv')
# 	aff_pop(df)
# 	return 0

# if __name__ == '__main__':
# 	main()
