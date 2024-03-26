import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Assuming the file is in Excel format
df = pd.read_csv("./archive/suicide_rates_1990-2022.csv")

print(df.head())

print(df.isnull().sum())

df.describe()

# Group by year and calculate the mean suicide rate
yearly_mean = df.groupby('Year')['SuicideCount'].mean()

# Plotting the trend
plt.figure(figsize=(10, 6))
yearly_mean.plot(marker='o', linestyle='-')
plt.title('Trend of Suicide Rates (1990-2022)')
plt.xlabel('Year')
plt.ylabel('Mean Suicide Rate')
plt.grid(True)
plt.show()

# Calculate correlation matrix
corr_matrix = df.corr()

# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Plotting regional suicide rates
plt.figure(figsize=(12, 6))
sns.boxplot(x='RegionName', y='SuicideCount', data=df)
plt.title('Regional Suicide Rates')
plt.xlabel('Region')
plt.ylabel('Suicide Rate')
plt.xticks(rotation=45)
plt.show()


