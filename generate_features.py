import pandas as pd

data = pd.read_csv('weather_data.csv')

# Show the column names
print("📄 Column names in weather_data.csv:")
print(data.columns)
