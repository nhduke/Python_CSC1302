import pandas as pd
import matplotlib.pyplot as plt

# 1
# df import and shape
df = pd.read_csv("car_info.csv")
print("1. Shape of dataframe:", df.shape)

# 2
# v6 & japan
japanV6 = df[(df["cylinders"] == 6) & (df["origin"] == "japan")]
print("2. Japanese v6 cars:")
print(japanV6["name"].to_string(index=False))

# 3
# missing horsepower data
missHP = df[df["horsepower"].isna()]
print("3. Cars with missing horsepower data:")
print(missHP["name"].to_string(index= False))

# 4
# cars with mpg >= 20
mpg20Count = (df["mpg"] >= 20).sum()
print("4. Number of cars having mpg >= 20:", mpg20Count)

# 5
# name of car with highest mpg
maxMpg = df.loc[df["mpg"].idxmax()]
print("5. Most fuel-efficient car:", maxMpg["name"])

# 6
# weight stat
print("6. Weight statistics:")
print("Maximum weight:", df["weight"].max())
print("Minimum weight:", df["weight"].min())
print(f"Average weight:, {df["weight"].mean():.2f}")

# 7
# drop missing value
df_clean = df.dropna()
print("7. Shape after removing the missing values: ", df_clean.shape)

# 8
# pie chart of car origin
origin_counts = df["origin"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(origin_counts, labels=origin_counts.index, autopct="%1.1f%%")
plt.title("Proportion of Cars by Country of Origin")
plt.show()

# 9
# plot w/ xlabels, ylabels, legends. Place vertically (2,1)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# scatter plot of mpg vs weight
ax1.scatter(df["weight"], df["mpg"])
ax1.set_xlabel("Weight")
ax1.set_ylabel("MPG")
ax1.legend(["mpg vs weight"])
ax1.set_title("MPG vs Weight")


# scatter plot of mpg vs displacement
ax2.scatter(df["displacement"], df["mpg"])
ax2.set_xlabel("Displacement")
ax2.set_ylabel("MPG")
ax2.legend(["mpg vs displacement"])
ax2.set_title("MPG vs Displacement")


plt.tight_layout()
plt.show()
