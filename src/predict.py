import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/stock_price_model.pkl")

# Load dataset to get recent data
df = pd.read_csv("data/NSE_featured_data.csv")

# Select Features
features = ["SMA_10", "SMA_50", "Daily_Return", "Volatility", "Volume"]
df = df.dropna(subset=features)  # Remove missing values

# Get the latest row with feature names
latest_data = df[features].iloc[-1:].copy()  # Ensures it keeps column names

# Run the prediction
predicted_price = model.predict(latest_data)[0]

print(f"📈 Predicted Stock Price for Next Day: {predicted_price:.2f}")
