import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

def create_lstm_model():
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(10, 1)),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return model

def train_model():
    df = pd.read_csv("data/NSE_featured_data.csv")

    # Extract stock symbols
    stock_symbols = df["Symbol"].unique()

    # Select one stock (for now)
    symbol = stock_symbols[0]
    stock_data = df[df["Symbol"] == symbol][["Close"]]

    # Normalize data
    scaler = MinMaxScaler()
    stock_data_scaled = scaler.fit_transform(stock_data)

    # Create sequences
    X_train, y_train = [], []
    for i in range(10, len(stock_data_scaled)):
        X_train.append(stock_data_scaled[i-10:i, 0])
        y_train.append(stock_data_scaled[i, 0])

    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    # Train model
    model = create_lstm_model()
    model.fit(X_train, y_train, epochs=20, batch_size=16)

    # Save model
    model.save("stock_model.h5")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()
