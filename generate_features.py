import pandas as pd
import os
from datetime import datetime

# Load the raw data from the CSV file saved by main.py
data = pd.read_csv('weather_data.csv')

# Convert datetime string to actual datetime
data['dt'] = pd.to_datetime(data['dt'], unit='s')

# Create time-based features
data['hour'] = data['dt'].dt.hour
data['day'] = data['dt'].dt.day
data['month'] = data['dt'].dt.month

# Example derived feature: temperature difference from average
data['temp_diff'] = data['main.temp'] - data['main.temp'].mean()

# Save processed features to a new CSV
data.to_csv('features.csv', index=False)

print("Features generated and saved to features.csv.")
