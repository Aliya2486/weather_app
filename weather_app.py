import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        print("DEBUG - API returned:", data)  # Add this line
        return None

def main():
    api_key = "3458bd0770f122603831d668945e5ff4" # Replace this with your real API key
    city = input("Enter city name: ")
    weather = get_weather(city, api_key)

    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or error retrieving data.")

if __name__ == "__main__":
    main()
