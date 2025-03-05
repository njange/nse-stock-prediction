import pandas as pd
import numpy as np

# Load cleaned NSE stock data
df = pd.read_csv("data/NSE_cleaned_data.csv")

# Convert Date to datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Select important columns and drop missing values
df = df[["Date", "Symbol", "Close", "Volume"]].dropna()

# Clean the Volume column
df["Volume"] = df["Volume"].replace("-", "0")  # Replace "-" with "0"
df["Volume"] = df["Volume"].str.replace(",", "").astype(float)  # Remove commas and convert to float

# Generate Technical Indicators for Each Stock
def compute_indicators(stock_df):
    stock_df["SMA_10"] = stock_df["Close"].rolling(window=10).mean()  # 10-day Moving Average
    stock_df["SMA_50"] = stock_df["Close"].rolling(window=50).mean()  # 50-day Moving Average
    stock_df["Daily_Return"] = stock_df["Close"].pct_change()  # Daily Returns
    stock_df["Volatility"] = stock_df["Daily_Return"].rolling(window=10).std()  # Volatility (Standard Deviation)
    return stock_df

# Apply indicators stock by stock
df = df.groupby("Symbol", group_keys=False).apply(compute_indicators)

# Drop NaN values caused by rolling calculations
df.dropna(inplace=True)

# Save updated dataset
df.to_csv("data/NSE_featured_data.csv", index=False)

print("✅ Data with features saved as 'NSE_featured_data.csv'")
print(df.info())
print(df.head())
