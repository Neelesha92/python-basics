import os
import requests

API_KEY = os.getenv('OPENWEATHER_API_KEY', '341b11d8eeb4f32201f7097074fa9c8b')  # Replace with a real key
  # Load API key from environment variable

# Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city_name):
    # Make a request to the API
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(request_url)
    

    # Check if the request was successfull
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display the weather information
        print(f"Weather in {city_name}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error: Could not fetch weather data. Please check the city name or API key.")

def main():
    print("Welcome to the CLI Weather Application!")
    
    city_name = input("Enter the city name: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()