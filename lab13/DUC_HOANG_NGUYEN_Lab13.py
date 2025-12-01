import pandas as pd
from matplotlib import pyplot as plt

# load population dataset from a CSV file (populations.csv)
# this dataset contains columns: 'country_code', 'country_name', 'Populations for Years between 1970 and 2024'
# We will focus on the year 2024
# TODO: Load the dataset into a pandas DataFrame
# use pd.read_csv to load the CSV file
population = pd.read_csv('populations.csv')
# TODO: Display the shape and first 3 rows of the DataFrame
# use df.head(n) to display the first n rows
# use df.shape to display the shape of the DataFrame
print(population.head(3))
print("Population Data Shape: ", population.shape)

# TODO: Filter the DataFrame for the year 2024
# Your code here
print("Population Data 2024: ")
population = population.filter(items=['country_code', '2024'])
print(population)


# TODO: Filter out countries with population less than 2 million
# your code here
print("Population: ")
population = population[population['2024'] < 2000000]
print(population)

# TODO: Display the shape and first 3 rows of the filtered DataFrame
# your code here
print("Population: ")
print(population.head(3))





# load Global Greenhouse Gas Emissions dataset from a CSV file (GHG_2025.csv)
# this dataset contains columns: 'country_code', 'country_name', 'Million Tonnes of carbon dioxide equivalent (MtCO2e) for years between 1970 and 2024'
# TODO: Load the dataset into a pandas DataFrame
# your code here
greenHouse = pd.read_csv('GHG_2025.csv')

# TODO: Display the first few rows of the DataFrame
# Your code here

print(greenHouse.head(3))
print("Green House Data Shape: ", greenHouse.shape)
# TODO: Filter the DataFrame for the year 2024
# your code here
print("Green House Data 2024: ")
greenHouse = greenHouse.filter(items=['country_code', '2024'])
print(greenHouse)
# TODO: Display the first 3 rows of the filtered DataFrame
# your code here
print("Green House")
print(greenHouse.head(3))


# Merge the two datasets on 'country_code' and save it to a new DataFrame df_merged
# use pd.merge to merge the two DataFrames
# Refer to Pandas documentation for merging DataFrames here (https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
# Tour code here

df_merged = pd.merge(population, greenHouse, how= 'left', left_on='country_code', right_on= 'country_code')
# TODO: Display the shape and first 3 rows of the merged DataFrame
# your code here
print("Merged Data: ")
print(df_merged.head(3))
print(df_merged.shape)


# Calculate per capita GHG emissions
# TODO: Create a new column 'GHG_per_capita' in the merged DataFrame. Use the formula: GHG_per_capita = GHG_2024 / Population_2024 to calculate per capita emissions.
# TODO: Change unit for GHG_per_capita from million tonnes to tonnes
# your code here
df_merged['GHG_per_capita'] = (df_merged['2024_y'] / df_merged['2024_x'])*1000000
# TODO: Display the first 3 rows of the DataFrame with per capita GHG emissions
# your code here
print(df_merged.head(3))






# --------------------
# Plotting the results
# --------------------
# Create a scatter plot with Population on the x-axis and GHG Emissions on the y-axis. Use logarithmic scales for both axes.
# TODO: create a plot with appropriate size (12, 8)
# your code here
plt.figure(figsize=(12, 8))

# TODO: use plt.scatter to create the scatter plot
    # Refer to Matplotlib documentation for scatter plots here (https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py)
# your code here
plt.scatter(df_merged['2024_x'], df_merged["2024_y"])


# TODO: plot labels and title appropriately; 
    # x-axis: Population (log scale), 
    # y-axis: GHG Emissions (MtCO2e), 
    # title: GHG Emissions vs Population (2024)
# your code here
plt.xscale("log")
plt.yscale("log")

plt.xlabel("Population (log scale)")
plt.ylabel("GHG Emissions (MtCO2e)")
plt.title("GHG Emissions vs Population (2024)")
# TODO: save the plot as 'ghg_vs_population.png'
    # you can use plt.savefig to save the plot
# your code here
plt.savefig("ghg_vs_population")




# Create a scatter plot with Population on the x-axis and GHG Emissions per capita on the y-axis. Use logarithmic scales for both axes.
# TODO: create a plot with appropriate size (12, 8)
# your code here
plt.figure(figsize=(12,8))
# TODO: use plt.scatter to create the scatter plot
# your code here
plt.scatter(df_merged["2024_x"],df_merged["GHG_per_capita"])
# TODO: plot labels and title appropriately; 
    # x-axis: Population (log scale), 
    # y-axis: GHG Emissions Per Capita (tCO2e), 
    # title: GHG Emissions Per Capita vs Population (2024)
# your code here
plt.xscale('log')
plt.yscale('log')

plt.xlabel("Population (log scale)")
plt.ylabel('GHG Emissions Per Capita (tCO2e)')
plt.title('GHG Emissions Per Capita vs Population (2024)')
# TODO: save the plot as 'ghg_vs_population_per_capita.png'
    # you can use plt.savefig to save the plot
# your code here
plt.savefig('ghg_vs_population_per_capita')



# Create a bar chart showing the top 10 countries with the highest GHG emissions.
# TODO: extract the top 10 countries by GHG emissions and save it to a new DataFrame with the name top_10_ghg
    # You can use df.nlargest to get the top 10 rows based on GHG emissions
# your code here
top_10_ghg = df_merged.nlargest(10, "2024_y")
print('result')
print(top_10_ghg)
# TODO: create a plot with appropriate size (12, 8)
# your code here
plt.figure(figsize=(12,8))
# TODO: use plt.bar to create the bar chart
# your code here
plt.bar(df_merged['country_code'], df_merged['2024_y'])
# TODO: plot labels and title appropriately; 
    # x-axis: Country, 
    # y-axis: GHG Emissions (MtCO2e), 
    # title: Top 10 Countries by GHG Emissions (2024)
# your code here
plt.xlabel("Country")
plt.xticks(rotation=45, ha='right', fontsize = 7)
plt.ylabel('GHG Emissions (MtCO2e)')
plt.title('Top 10 Countries by GHG Emissions (2024)')
# TODO: save the plot as 'top_10_ghg_emissions.png'
    # you can use plt.savefig to save the plot
# your code here
plt.savefig('top_10_ghg_emissions')


# Create a bar chart showing the top 10 countries with the highest GHG emissions per capita.
# TODO: extract the top 10 countries by GHG emissions per capita and save it to a new DataFrame with the name top_10_ghg_per_capita
    # You can use df.nlargest to get the top 10 rows based on GHG emissions
# your code here
top_10_ghg_per_capita = df_merged.nlargest(10, "GHG_per_capita")

# TODO: create a plot with appropriate size (12, 8)
# your code here
plt.figure(figsize=(12,8))
# TODO: use plt.bar to create the bar chart
# your code here
plt.bar(df_merged['country_code'],df_merged['GHG_per_capita'])
# TODO: plot labels and title appropriately; 
    # x-axis: Country, 
    # y-axis: GHG Emissions per capita(tCO2e), 
    # title: Top 10 Countries by GHG Emissions Per Capita (2024)
# your code here
plt.xlabel("Country")
plt.xticks(rotation=45, ha='right', fontsize = 7)
plt.ylabel("GHG Emissions per capita(tCO2e)")
plt.title('Top 10 Countries by GHG Emissions Per Capita (2024)')
# TODO: save the plot as 'top_10_ghg_per_capita.png'
    # you can use plt.savefig to save the plot
# your code here
plt.savefig('top_10_ghg_per_capita')

