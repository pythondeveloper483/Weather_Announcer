import requests
import json
import win32com.client as wincl

# Initialize the voice engine
speaker = wincl.Dispatch("SAPI.SpVoice")

while True:
    city = input("Enter the name of the city (or type 'stop' to quit): ")
    if city.lower() == "stop":
        speaker.Speak("Goodbye! Program stopped.")
        break

    # Weather Forecast API (3 days)
    url = f"https://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q={city}&days=3"
    r = requests.get(url)
    wdict = json.loads(r.text)

    # Current weather
    current = wdict["current"]
    temp_c = current["temp_c"]
    temp_f = current["temp_f"]
    condition = current["condition"]["text"]
    humidity = current["humidity"]
    wind_kph = current["wind_kph"]
    wind_dir = current["wind_dir"]
    feels_like_c = current["feelslike_c"]
    uv_index = current["uv"]
    pressure_mb = current["pressure_mb"]
    visibility_km = current["vis_km"]
    last_updated = current["last_updated"]

    # Speak current weather
    speaker.Speak(f"Currently in {city}, it is {temp_c} degrees Celsius, or {temp_f} Fahrenheit.")
    speaker.Speak(f"The condition is {condition}. Humidity is {humidity} percent.")
    speaker.Speak(f"Wind speed is {wind_kph} kilometers per hour, blowing {wind_dir}.")
    speaker.Speak(f"It feels like {feels_like_c} degrees Celsius.")
    speaker.Speak(f"UV index is {uv_index}. Air pressure is {pressure_mb} millibars.")
    speaker.Speak(f"Visibility is {visibility_km} kilometers.")
    speaker.Speak(f"Last updated at {last_updated}.")

    # Forecast for next 3 days
    forecast_days = wdict["forecast"]["forecastday"]
    for day in forecast_days:
        date = day["date"]
        day_condition = day["day"]["condition"]["text"]
        max_temp = day["day"]["maxtemp_c"]
        min_temp = day["day"]["mintemp_c"]
        avg_humidity = day["day"]["avghumidity"]
        sunrise = day["astro"]["sunrise"]
        sunset = day["astro"]["sunset"]

        # Speak forecast
        speaker.Speak(f"On {date}, expect {day_condition} with a high of {max_temp} and a low of {min_temp} degrees Celsius.")
        speaker.Speak(f"Average humidity will be {avg_humidity} percent.")
        speaker.Speak(f"Sunrise at {sunrise} and sunset at {sunset}.")