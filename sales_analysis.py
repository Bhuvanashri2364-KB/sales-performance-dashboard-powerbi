# ================================
# IMPORT LIBRARIES
# ================================

# Import pandas for data manipulation and analysis
import pandas as pd

# ================================
# DATA LOADING
# ================================

# Load dataset from the data folder
# encoding='latin1' avoids encoding errors
df = pd.read_csv("data/superstore.csv", encoding="latin1")

# Preview dataset to understand structure
print("\nPreview of dataset:")
print(df.head())

# Display column names
print("\nColumn names:")
print(df.columns)

# ================================
# DATA UNDERSTANDING
# ================================

# Check dataset size (rows and columns)
print("\nShape of data:")
print(df.shape)

# Check data types and null values
print("\nData Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate records
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ================================
# DATA CLEANING
# ================================

# Convert 'Order Date' to datetime format
# Required for time-based analysis (monthly/yearly trends)
print("\nConverting Order Date to datetime...")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Confirm datatype conversion
print(df['Order Date'].dtype)

# ================================
# FEATURE ENGINEERING
# ================================

# Create 'Month' and 'Year' columns from Order Date
# Helps analyze seasonal trends
print("\nCreating Month and Year columns...")

df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Display sample
print(df[['Order Date', 'Month', 'Year']].head())

# Create Profit Margin column
# Profit Margin = Profit / Sales
# Key metric to evaluate business efficiency
print("\nCreating Profit Margin column...")

df['Profit Margin'] = df['Profit'] / df['Sales']

print(df[['Sales', 'Profit', 'Profit Margin']].head())


# ================================
# CATEGORY ANALYSIS
# ================================

# Analyze total sales by category
# Identifies revenue-generating categories
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# Analyze total profit by category
# Identifies most profitable categories
print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# ================================
# PROFIT LEAKAGE ANALYSIS
# ================================

# Identify products with high sales but low or negative profit
# Step 1: Select top 50 records by sales
# Step 2: From those, find lowest profit products
print("\nTop 10 Products with HIGH Sales but LOW Profit:")

high_sales_low_profit = df.sort_values(by="Sales", ascending=False).head(50)

print(high_sales_low_profit.sort_values(by="Profit").head(10)[["Product Name", "Sales", "Profit"]])

# ================================
# DISCOUNT IMPACT ANALYSIS
# ================================

# Analyze how discount levels affect profit
# Helps understand if discount strategy is causing losses
print("\nDiscount vs Profit:")

print(df.groupby("Discount")["Profit"].mean().sort_index())

# ================================
# REGION ANALYSIS
# ================================

# Analyze total sales by region
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

# Analyze total profit by region
print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum())

# ================================
# CUSTOMER SEGMENT ANALYSIS
# ================================

# Analyze sales by customer segment
print("\nSales by Segment:")
print(df.groupby("Segment")["Sales"].sum())

# Analyze profit by customer segment
print("\nProfit by Segment:")
print(df.groupby("Segment")["Profit"].sum())

# ================================
# CORRELATION ANALYSIS
# ================================

# Check relationship between discount and profit
# Negative value indicates discount reduces profit
print("\nCorrelation between Discount and Profit:")
print(df["Discount"].corr(df["Profit"]))

# ================================
# CATEGORY DEEP DIVE (FURNITURE)
# ================================

# Analyze discount impact specifically for Furniture
# Helps understand why Furniture has low profitability
print("\nFurniture Discount Analysis:")
furniture = df[df["Category"] == "Furniture"]

print(furniture.groupby("Discount")["Profit"].mean())

# ================================
# PROFIT MARGIN ANALYSIS
# ================================

# Compare profit margins across categories
# Identifies most efficient category
print("\nProfit Margin by Category:")
print(df.groupby("Category")["Profit Margin"].mean())
