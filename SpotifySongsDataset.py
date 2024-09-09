import pandas as pd

file_path = r"C:\Users\Hardy\OneDrive\Desktop\Datasets\Most Streamed Spotify Songs 2024.csv"

# Attempt to read the file using different encodings
encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']

for enc in encodings:
    try:
        topSongs24 = pd.read_csv(file_path, encoding=enc)
        print(f'Successfully read the file with encoding: {enc}')
        print(topSongs24.head())  # Display the first few rows of the dataframe
        break
    except Exception as e:
        print(f'Failed to read the file with encoding {enc}: {e}')
