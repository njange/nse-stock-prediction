import matplotlib.pyplot as plt

def plot_predictions(y_test, y_pred):
    plt.figure(figsize=(12,6))
    plt.plot(y_test.values, label="Actual Prices", linestyle='dashed')
    plt.plot(y_pred, label="Predicted Prices", alpha=0.8)
    plt.legend()
    plt.title("Actual vs Predicted Stock Prices")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")
    plt.show()
