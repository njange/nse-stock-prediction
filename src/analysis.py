import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('/home/njange/Projects/nse-stock-prediction/data/NSE_featured_data.csv')

# Basic Data Exploration
print(data.head())
print(data.info())
print(data.describe())

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Example 1: Histogram of 'Close' prices
plt.figure(figsize=(10, 6))
sns.histplot(data['Close'], bins=30, kde=True)
plt.title('Distribution of Close Prices')
plt.xlabel('Close Price')
plt.ylabel('Frequency')
plt.show()

# Example 2: Scatter plot between 'Volume' and 'Close'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Volume', y='Close', data=data)
plt.title('Scatter Plot between Volume and Close Price')
plt.xlabel('Volume')
plt.ylabel('Close Price')
plt.show()

# Example 3: Box plot of 'Close' prices by 'Symbol'
plt.figure(figsize=(14, 8))
sns.boxplot(x='Symbol', y='Close', data=data)
plt.title('Box Plot of Close Prices by Symbol')
plt.xlabel('Symbol')
plt.ylabel('Close Price')
plt.xticks(rotation=90)
plt.show()

# Example 4: Correlation heatmap
plt.figure(figsize=(12, 8))
# Exclude non-numeric columns for correlation matrix
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Save the plots to a PDF file
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('/home/njange/Projects/nse-stock-prediction/output_plots.pdf') as pdf:
    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Close'], bins=30, kde=True)
    plt.title('Distribution of Close Prices')
    plt.xlabel('Close Price')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()

    # Scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Volume', y='Close', data=data)
    plt.title('Scatter Plot between Volume and Close Price')
    plt.xlabel('Volume')
    plt.ylabel('Close Price')
    pdf.savefig()
    plt.close()

    # Box plot
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='Symbol', y='Close', data=data)
    plt.title('Box Plot of Close Prices by Symbol')
    plt.xlabel('Symbol')
    plt.ylabel('Close Price')
    plt.xticks(rotation=90)
    pdf.savefig()
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    pdf.savefig()
    plt.close()