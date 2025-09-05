import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns

# Optional for better plots
sns.set(style="whitegrid")

# Step 1: Combine Monthly CSVs into a Single DataFrame
path = "./data"
all_files = glob.glob(os.path.join(path, "sales_*.csv"))
df = pd.concat((pd.read_csv(file) for file in all_files), ignore_index=True)

# Step 2: Quick Overview of the Data
print("Data Preview:")
print(df.head())
print("\nColumns:", df.columns)
print("\nMissing values:\n", df.isnull().sum())

# Step 3: Clean the Data
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Hour'] = df['Date'].dt.hour

# Step 4: Add New Columns
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Step 5: Sales Summary
monthly_sales = df.groupby('Month')['Revenue'].sum()
print("\nMonthly Sales:\n", monthly_sales)

# Step 6: Top-Selling Products
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop-Selling Products:\n", top_products)

# Step 7: Customer Behavior
avg_purchase = df.groupby('CustomerID')['Revenue'].mean().sort_values(ascending=False)
print("\nTop Customers by Avg Purchase:\n", avg_purchase.head())

# Step 8: Sales by Hour (Customer Visit Trend)
hourly_sales = df.groupby('Hour')['Revenue'].sum()
plt.figure(figsize=(10,6))
sns.lineplot(x=hourly_sales.index, y=hourly_sales.values)
plt.title("Sales by Hour of the Day")
plt.xlabel("Hour")
plt.ylabel("Revenue")
plt.xticks(range(0,24))
plt.grid(True)
plt.show()

# Step 9: Product Revenue Trends
product_monthly = df.groupby(['Product', 'Month'])['Revenue'].sum().unstack()
print("\nMonthly Revenue per Product:\n", product_monthly.head())

# Step 10: Correlation Between Quantity and Revenue
correlation = df[['Quantity', 'Revenue']].corr()
print("\nCorrelation Matrix:\n", correlation)

# Optional: Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)
print("\n✅ Cleaned data saved to 'cleaned_sales_data.csv'")
