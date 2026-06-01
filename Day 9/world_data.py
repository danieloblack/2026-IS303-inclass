import pandas as pd
df = pd.read_csv("Day 9/world_development_data.csv")
"""
print(df.head())
print(df.describe())
print(df.shape)
print(df.info())
"""
#Life expectancy below 60
life_exp=df[df["life_expectancy"] < 60]
print(life_exp[["country", "life_expectancy"]])

# Highest life expectancy
highest = df.loc[df["life_expectancy"].idxmax()]
print(highest[["country", "life_expectancy"]])

# Unique regions
df["region"] = df["region"].str.title().str.strip()
regions = df["region"].unique()
print(regions)

#missing values in entire dataset
print(df.isnull().sum())

#How many countires in "Sub Saharan Africa" region
ssa = df[df["region"] == "Sub Saharan Africa"]
print(ssa[["country", "region"]])

#fill in water
df["clean_water_pct"].fillna(0)

assert df["clean_water_pct"].notna().sum() == df.shape[0], "Missing clean water data!"


