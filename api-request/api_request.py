import requests
api_key = "e8acbff7bbdd21d20a634d800681fdca"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching Weather data from WeatherStack API ...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise

#fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-09-09 10:27', 'localtime_epoch': 1757413620, 'utc_offset': '-4.0'}, 'current': {'observation_time': '02:27 PM', 'temperature': 19, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '06:31 AM', 'sunset': '07:15 PM', 'moonrise': '08:08 PM', 'moonset': '08:38 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 98}, 'air_quality': {'co': '394.05', 'no2': '14.245', 'o3': '113', 'so2': '6.845', 'pm2_5': '10.73', 'pm10': '10.915', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 17, 'wind_degree': 58, 'wind_dir': 'ENE', 'pressure': 1028, 'precip': 0, 'humidity': 63, 'cloudcover': 0, 'feelslike': 19, 'uv_index': 3, 'visibility': 16, 'is_day': 'yes'}}

