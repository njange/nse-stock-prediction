import pandas as pd

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Convert Date to datetime and sort
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # Select relevant columns and drop missing values
    df = df[["Date", "Symbol", "Close", "Volume"]].dropna()

    # Clean Volume column
    df["Volume"] = df["Volume"].replace("-", "0")  # Replace "-" with "0"
    df["Volume"] = df["Volume"].str.replace(",", "").astype(float)  # Convert to float

    # Generate technical indicators
    def compute_indicators(stock_df):
        stock_df["SMA_10"] = stock_df["Close"].rolling(window=10).mean()
        stock_df["SMA_50"] = stock_df["Close"].rolling(window=50).mean()
        stock_df["Daily_Return"] = stock_df["Close"].pct_change()
        stock_df["Volatility"] = stock_df["Daily_Return"].rolling(window=10).std()
        return stock_df

    # Apply indicators to each stock
    df = df.groupby("Symbol", group_keys=False).apply(compute_indicators)

    # Drop NaN values caused by rolling calculations
    df.dropna(inplace=True)

    # Save processed data
    df.to_csv(output_file, index=False)
    print(f"✅ Data saved as '{output_file}'")
