import requests
import pandas as pd

# --- Configuration ---
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
CITY_NAME = "London"
API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

# --- 1. Extraction Stage ---
def extract_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

# --- 2. Transformation Stage ---
def transform_weather_data(raw_data):
    if not raw_data:
        return None

    try:
        weather_info = {
            "city": raw_data["name"],
            "temperature_celsius": raw_data["main"]["temp"],
            "feels_like_celsius": raw_data["main"]["feels_like"],
            "humidity_percent": raw_data["main"]["humidity"],
            "weather_description": raw_data["weather"][0]["description"],
            "wind_speed_m_s": raw_data["wind"]["speed"]
        }
        return pd.DataFrame([weather_info])
    except KeyError as e:
        print(f"Missing key in raw data: {e}")
        return None

# --- 3. Loading Stage ---
def load_data(transformed_data, output_path="weather_data.csv"):
    if transformed_data is not None:
        transformed_data.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
    else:
        print("No data to save.")

# --- Main Execution ---
if __name__ == "__main__":
    print(f"Running weather ETL pipeline for {CITY_NAME}...")
    raw_data = extract_weather_data(API_URL)
    transformed_data = transform_weather_data(raw_data)
    load_data(transformed_data)
