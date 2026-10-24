import requests

API_KEY = "684f8dca2f9c4efc216f1201951e5a0d"

def get_weather(city):
    try:

        city = city.strip().title()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:
            return "City not found"

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"{city.title()}: {temperature}°C, {description}"

    except Exception as e:
        print(e)
        return "Weather not found"