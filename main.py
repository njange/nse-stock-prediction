import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from src.preprocess import preprocess_data
from src.train import train_model
from src.gui import StockPredictorGUI

def main():
    # Step 1: Preprocess Data
    print("📊 Preprocessing stock data...")
    preprocess_data("data/NSE_cleaned_data.csv", "data/NSE_featured_data.csv")

    # Step 2: Train LSTM Model
    print("🔄 Training LSTM model...")
    train_model()

    # Step 3: Launch PyQt GUI
    print("🖥️ Launching GUI...")
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)  # Disable Help Button
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)  # Improve rendering

    window = StockPredictorGUI()
    window.show()

    sys.exit(app.exec_())  # Start the event loop

if __name__ == "__main__":
    main()
