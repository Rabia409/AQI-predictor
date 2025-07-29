import pandas as pd

# Step 1: Load the weather data you previously collected
df = pd.read_csv('weather_data.csv')

# Step 2: Make sure the 'datetime' column is in proper datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Step 3: Create time-based features
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month

# Step 4: Create change-based features (difference from previous row)
df['temp_change'] = df['temp'].diff()
df['humidity_change'] = df['humidity'].diff()
df['pressure_change'] = df['pressure'].diff()

# Step 5: (Optional) If you already have AQI column, calculate AQI change
if 'AQI' in df.columns:
    df['AQI_change'] = df['AQI'].diff()

# Step 6: Replace missing values (from diff() calculation) with 0
df.fillna(0, inplace=True)

# Step 7: Save the new data with features to a new file
df.to_csv('features.csv', index=False)

print("✅ Feature generation completed and saved to features.csv")
