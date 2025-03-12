import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QTableWidget, QTableWidgetItem
from datetime import datetime, timedelta

class StockPredictorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select Stock Symbol:")
        layout.addWidget(self.label)

        # Load available stocks
        try:
            self.df = pd.read_csv("data/NSE_cleaned_data.csv")
            self.df["Date"] = pd.to_datetime(self.df["Date"])  # Ensure Date is in datetime format
            stock_symbols = self.df["Symbol"].unique().tolist() if "Symbol" in self.df.columns else ["N/A"]
        except Exception as e:
            print(f"⚠️ Error loading stock symbols: {e}")
            stock_symbols = ["N/A"]

        self.combo_stock = QComboBox()
        self.combo_stock.addItems(stock_symbols)
        layout.addWidget(self.combo_stock)

        self.label_time = QLabel("Select Time Range:")
        layout.addWidget(self.label_time)

        # Dropdown for time ranges
        self.combo_time = QComboBox()
        self.combo_time.addItems([
            "Last Week", "Last 3 Months", "Last 1 Month",
            "Last 5 Years", "Last 10 Years", "All Time"
        ])
        layout.addWidget(self.combo_time)

        # Button to update data
        self.button = QPushButton("Show Prices")
        self.button.clicked.connect(self.update_prices)
        layout.addWidget(self.button)

        # Table to display stock prices
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Date", "Close Price"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.setWindowTitle("Stock Predictor")

    def update_prices(self):
        """ Update the stock prices based on selected stock and time range """
        selected_stock = self.combo_stock.currentText()
        selected_range = self.combo_time.currentText()

        # Filter dataset for the selected stock
        stock_data = self.df[self.df["Symbol"] == selected_stock].copy()

        # Filter by time range
        today = datetime.today()
        if selected_range == "Last Week":
            start_date = today - timedelta(weeks=1)
        elif selected_range == "Last 1 Month":
            start_date = today - timedelta(weeks=4)
        elif selected_range == "Last 3 Months":
            start_date = today - timedelta(weeks=12)
        elif selected_range == "Last 5 Years":
            start_date = today - timedelta(days=5 * 365)
        elif selected_range == "Last 10 Years":
            start_date = today - timedelta(days=10 * 365)
        else:
            start_date = stock_data["Date"].min()

        stock_data = stock_data[stock_data["Date"] >= start_date]

        # Update table
        self.table.setRowCount(len(stock_data))
        for row, (index, rowData) in enumerate(stock_data.iterrows()):
            self.table.setItem(row, 0, QTableWidgetItem(rowData["Date"].strftime("%Y-%m-%d")))
            self.table.setItem(row, 1, QTableWidgetItem(str(rowData["Close"])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockPredictorGUI()
    window.show()
    sys.exit(app.exec_())
