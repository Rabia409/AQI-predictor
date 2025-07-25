import os
import requests
import pandas as pd
from datetime import datetime

# Get the key from your Replit secrets
import os
API_KEY = os.environ.get('RABIA_API_KEY')
CITY = "Lahore"

if not API_KEY:
    raise ValueError("API Key is missing! Check GitHub secrets.")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Extract useful features
features = {
    "city": CITY,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "temperature": data['main']['temp'],
    "humidity": data['main']['humidity'],
    "pressure": data['main']['pressure'],
    "wind_speed": data['wind']['speed'],
    "weather": data['weather'][0]['main']
}

# Convert to a pandas DataFrame
df = pd.DataFrame([features])

# Save as CSV file
csv_file = "weather_data.csv"
if os.path.exists(csv_file):
    df.to_csv(csv_file, mode='a', header=False, index=False)
else:
    df.to_csv(csv_file, index=False)

print("✅ Data saved successfully to weather_data.csv")

