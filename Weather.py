import requests

WEATHERSTACK_API_KEY = "5b29a320d021aa5aa8f035f4ecd38fac"  # Replace with your API key
WEATHERSTACK_BASE_URL = "http://api.weatherstack.com/current"
location="Mumbai"


def get_weather(location):
    """Fetch current weather for a given location using Weatherstack API."""
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": location
    }
    response = requests.get(WEATHERSTACK_BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            return {
                
                "location": data.get("location", {}).get("name", "Unknown"),
                "temperature": data["current"]["temperature"],
                "description": data["current"]["weather_descriptions"][0],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_speed"]
            }
        else:
            return {"error": "Unable to fetch weather data. Please check the location."}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}

weather = get_weather(location)

print(f"**Location:** {weather['location']}")
print(f"**Temperature:** {weather['temperature']}°C")
print(f"**Description:** {weather['description']}")
print(f"**Humidity:** {weather['humidity']}%")
print(f"**Wind Speed:** {weather['wind_speed']} km/h")

