import requests
import json
import pandas as pd

# --- Configuration ---
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
CITY_NAME = "London"
API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

# --- 1. Extraction Stage (API Call) ---
def extract_weather_data(url):
    """Fetches weather data from the OpenWeatherMap API."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

# --- 2. Transformation Stage ---
def transform_weather_data(raw_data):
    """Transforms raw API data into a structured format (e.g., DataFrame)."""
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
        df = pd.DataFrame([weather_info])
        return df
    except KeyError as e:
        print(f"Error during data transformation: Missing key {e} in raw data.")
        return None

# --- 3. Loading Stage (e.g., Print to Console, Save to CSV) ---
def load_data(transformed_data, output_path="weather_data.csv"):
    """Loads transformed data to a destination (e.g., print, save to CSV)."""
    if transformed_data is not None:
        print("Transformed Weather Data:")
        print(transformed_data)
        transformed_data.to_csv(output_path, index=False)
        print(f"\nData successfully saved to {output_path}")
    else:
        print("No data to load.")

# --- Pipeline Execution ---
if _name_ == "_main_":
    print(f"Starting weather data pipeline for {CITY_NAME}...")

    # Extract
    raw_weather_data = extract_weather_data(API_URL)

    # Transform
    transformed_weather_df = transform_weather_data(raw_weather_data)

    # Load
    load_data(transformed_weather_df)