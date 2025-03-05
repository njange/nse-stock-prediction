import pandas as pd
import os

# Define the data folder path
data_folder = "data"

# Get all CSV file names
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
csv_files.sort()  # Ensure files are merged in chronological order

# Read and concatenate all files
df_list = []
for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    df_list.append(df)

# Merge all data
df_merged = pd.concat(df_list, ignore_index=True)

# Save the merged file
df_merged.to_csv("data/NSE_merged_data.csv", index=False)

print("✅ Merged all CSV files into 'NSE_merged_data.csv'")
