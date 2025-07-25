import requests
import csv
import os

# Get API key from environment variable
API_KEY = os.environ.get("RABIA_API_KEY")
if not API_KEY:
    raise ValueError("API Key is missing. Check if GitHub secret is set properly.")

# Set up URL
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# Get data
response = requests.get(url)
data = response.json()

# Extract useful info
weather_info = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "weather": data["weather"][0]["description"]
}

# Save to CSV
with open("weather_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature", "Humidity", "Weather"])
    writer.writerow([weather_info["city"], weather_info["temperature"], weather_info["humidity"], weather_info["weather"]])

print("Weather data saved successfully.")


