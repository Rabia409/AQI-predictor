import pandas as pd
from datetime import datetime

# Load your latest CSV (adjust filename if needed)
data = pd.read_csv("data.csv")

# Drop rows with missing values just in case
data.dropna(inplace=True)

# Create time-based features
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['hour'] = data['timestamp'].dt.hour
data['day'] = data['timestamp'].dt.day
data['month'] = data['timestamp'].dt.month

# Add derived features (examples)
data['temp_diff'] = data['main.temp'].diff()  # change in temperature
data['aqi_change'] = data['aqi'].diff()       # change in AQI

# Save the processed features to a new file
data.to_csv("features.csv", index=False)
print("✅ Features generated and saved to features.csv")
