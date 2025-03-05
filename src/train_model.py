import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

# Ensure 'models/' directory exists
os.makedirs("models", exist_ok=True)

# Load the dataset
df = pd.read_csv("data/NSE_featured_data.csv")

# Select Features and Target
features = ["SMA_10", "SMA_50", "Daily_Return", "Volatility", "Volume"]
df = df.dropna(subset=features + ["Close"])  # Remove rows with missing values

X = df[features]
y = df["Close"].shift(-1)  # Predict next day's closing price

# Remove last row due to NaN
X, y = X[:-1], y[:-1]

# Split into Training (80%) and Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict Stock Prices
y_pred = model.predict(X_test)

# Evaluate Model
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"✅ Random Forest Model trained successfully! RMSE: {rmse:.2f}")

# Save model
joblib.dump(model, "models/stock_price_rf.pkl")
print("✅ Model saved as 'models/stock_price_rf.pkl'")
