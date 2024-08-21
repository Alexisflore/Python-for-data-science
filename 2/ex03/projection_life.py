import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load

def convert_gnp_value(gnp_str):
    """Convert GNP string with 'M' or 'k' into numeric values."""
    if isinstance(gnp_str, str):
        if 'M' in gnp_str:
            return float(gnp_str.replace('M', '')) * 1e6
        elif 'k' in gnp_str:
            return float(gnp_str.replace('k', '')) * 1e3
    return float(gnp_str)

def plot_life_expectancy_vs_gnp(life_expectancy_df, gnp_df):
    """Plot the life expectancy in 1900 against GNP in 1900 for each country."""

	# Check if DataFrames are not None
    if life_expectancy_df is None or gnp_df is None:
        raise ValueError("Input DataFrames cannot be None")

    # Extract data for the year 1900
    life_expectancy_1900 = life_expectancy_df[['country', '1900']].rename(columns={'1900': 'Life Expectancy'})
    gnp_1900 = gnp_df[['country', '1900']].rename(columns={'1900': 'GNP'})

    # Convert GNP values to numeric
    gnp_1900['GNP'] = gnp_1900['GNP'].apply(convert_gnp_value)

    # Merge life expectancy and GNP data on 'country'
    merged_df = pd.merge(life_expectancy_1900, gnp_1900, on='country')

    # Drop any rows with missing values (NaN)
    merged_df = merged_df.dropna()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['GNP'], merged_df['Life Expectancy'], color='green', edgecolors='black')
    plt.xlabel('Gross National Product (GNP) per capita in 1900')
    plt.ylabel('Life Expectancy in 1900')
    plt.title('Life Expectancy vs GNP per capita in 1900')
    plt.grid(True)

    # Annotate countries with high or low life expectancy
    for i, row in merged_df.iterrows():
        plt.annotate(row['country'], (row['GNP'], row['Life Expectancy']), fontsize=8, alpha=0.7)

    # Show the plot
    plt.show()

def main() -> int:
	# Load the life expectancy data
	life_expectancy_df = load('life_expectancy_years.csv')

	# Load the GNP data
	gnp_df = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
	# Call the function to plot the data
	plot_life_expectancy_vs_gnp(life_expectancy_df, gnp_df)

	return 0

if __name__ == '__main__':
     main()
