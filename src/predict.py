import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

model = tf.keras.models.load_model("models/stock_lstm.h5")
scaler = MinMaxScaler()
df = pd.read_csv("data/processed_stock_data.csv")
prices = scaler.fit_transform(df["Close"].values.reshape(-1, 1))

def predict_future(days=30):
    last_30_days = prices[-30:].reshape(1, 30, 1)
    future_prices = []
    
    for _ in range(days):
        pred = model.predict(last_30_days)
        future_prices.append(pred[0][0])
        last_30_days = np.roll(last_30_days, -1, axis=1)
        last_30_days[0, -1, 0] = pred

    return scaler.inverse_transform(np.array(future_prices).reshape(-1, 1))

if __name__ == "__main__":
    print(predict_future(30))
