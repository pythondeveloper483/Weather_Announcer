import requests
import json
import time

# If running on Windows with pywin32 installed this will provide TTS.
# If not available, the program will print to console instead of speaking.
try:
    import win32com.client as wincl
except Exception:
    wincl = None

# -------------------------
# Put your API key here.
# You gave this key: "24a2f401dcac49bc8a515905260205"
# It's placed here because you asked; for security consider using an environment
# variable or a local config file instead.
# -------------------------
API_KEY = "YOUR_API_KEY_HERE"

BASE_URL = "https://api.weatherapi.com/v1/forecast.json"
REQUEST_TIMEOUT = 10  # seconds


def fetch_weather(city: str) -> dict | None:
    """
    Fetch weather JSON for the given city.
    Returns parsed JSON dict on success, or None on failure (network, HTTP, parse).
    This function handles exceptions so the caller doesn't crash on network errors.
    """
    params = {"key": API_KEY, "q": city, "days": 3, "aqi": "no", "alerts": "no"}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()  # raise for HTTP errors (4xx/5xx)
        return resp.json()
    except requests.exceptions.RequestException:
        # Network error, DNS failure, refused connection, timeout, etc.
        return None
    except ValueError:
        # JSON decode error
        return None


def format_and_speak(wdict: dict, city: str, speaker) -> None:
    """
    Build a single continuous weather report string and either speak it (if speaker)
    or print it to console. This avoids multiple short Speak() calls so the TTS
    reads the whole report continuously.
    """
    parts: list[str] = []

    try:
        current = wdict.get("current", {})
        # Current weather fields (use .get to avoid KeyError)
        temp_c = current.get("temp_c")
        temp_f = current.get("temp_f")
        condition = current.get("condition", {}).get("text")
        humidity = current.get("humidity")
        wind_kph = current.get("wind_kph")
        wind_dir = current.get("wind_dir")
        feels_like_c = current.get("feelslike_c")
        uv_index = current.get("uv")
        pressure_mb = current.get("pressure_mb")
        visibility_km = current.get("vis_km")
        last_updated = current.get("last_updated")

        parts.append(f"Weather report for {city}.")

        if temp_c is not None and temp_f is not None:
            parts.append(f"Current temperature is {temp_c} degrees Celsius, {temp_f} Fahrenheit.")
        elif temp_c is not None:
            parts.append(f"Current temperature is {temp_c} degrees Celsius.")
        if condition:
            parts.append(f"Condition: {condition}.")
        if humidity is not None:
            parts.append(f"Humidity: {humidity} percent.")
        if wind_kph is not None and wind_dir:
            parts.append(f"Wind: {wind_kph} kilometers per hour, {wind_dir}.")
        if feels_like_c is not None:
            parts.append(f"It feels like {feels_like_c} degrees Celsius.")
        if uv_index is not None:
            parts.append(f"UV index {uv_index}.")
        if pressure_mb is not None:
            parts.append(f"Pressure {pressure_mb} millibars.")
        if visibility_km is not None:
            parts.append(f"Visibility {visibility_km} kilometers.")
        if last_updated:
            parts.append(f"Last updated at {last_updated}.")

        # Forecast (3 days)
        forecast_days = wdict.get("forecast", {}).get("forecastday", [])
        if forecast_days:
            parts.append("Forecast for the next days:")
            for day in forecast_days:
                date = day.get("date")
                day_info = day.get("day", {})
                day_condition = day_info.get("condition", {}).get("text")
                max_temp = day_info.get("maxtemp_c")
                min_temp = day_info.get("mintemp_c")
                avg_humidity = day_info.get("avghumidity")
                astro = day.get("astro", {})
                sunrise = astro.get("sunrise")
                sunset = astro.get("sunset")

                day_fragments: list[str] = []
                if date:
                    day_fragments.append(f"On {date}")
                if day_condition:
                    day_fragments.append(f"{day_condition}")
                if max_temp is not None and min_temp is not None:
                    day_fragments.append(f"high {max_temp}, low {min_temp} degrees Celsius")
                elif max_temp is not None:
                    day_fragments.append(f"high {max_temp} degrees Celsius")
                if avg_humidity is not None:
                    day_fragments.append(f"average humidity {avg_humidity} percent")
                if sunrise and sunset:
                    day_fragments.append(f"sunrise at {sunrise}, sunset at {sunset}")

                if day_fragments:
                    parts.append(", ".join(day_fragments) + ".")

        # Join into one continuous string so TTS speaks it without stopping between lines
        report = " ".join(parts).strip()
        if not report:
            report = "No weather information available."

        if speaker:
            # Speak once for the whole report
            try:
                speaker.Speak(report)
            except Exception:
                # If TTS fails for any reason, fallback to printing
                print(report)
        else:
            print(report)

    except Exception:
        # Any unexpected error while formatting/speaking should not crash the program.
        fallback = "An error occurred while preparing the weather report."
        if speaker:
            try:
                speaker.Speak(fallback)
            except Exception:
                print(fallback)
        else:
            print(fallback)


def main():
    # Initialize speaker if available
    speaker = None
    if wincl:
        try:
            speaker = wincl.Dispatch("SAPI.SpVoice")
        except Exception:
            speaker = None

    print("Weather TTS Reporter. Type 'stop' to quit.")
    while True:
        try:
            city = input("Enter the name of the city (or type 'stop' to quit): ").strip()
        except (KeyboardInterrupt, EOFError):
            goodbye = "Goodbye! Program stopped."
            print()
            if speaker:
                try:
                    speaker.Speak(goodbye)
                except Exception:
                    print(goodbye)
            else:
                print(goodbye)
            break

        if not city:
            continue
        if city.lower() == "stop":
            goodbye = "Goodbye! Program stopped."
            if speaker:
                try:
                    speaker.Speak(goodbye)
                except Exception:
                    print(goodbye)
            else:
                print(goodbye)
            break

        # Fetch weather safely
        wdict = fetch_weather(city)
        if wdict is None:
            err_msg = "Network unavailable or weather service could not be reached or you have not configured your API key, Please configure your API key. Please check your connection."
            print(err_msg)
            if speaker:
                try:
                    speaker.Speak(err_msg)
                except Exception:
                    pass
            # wait a short moment to avoid hammering the API on repeated failures
            time.sleep(1)
            continue

        # Validate response shape before using it
        if not isinstance(wdict, dict) or "current" not in wdict:
            err_msg = "Received unexpected data from weather service."
            print(err_msg)
            if speaker:
                try:
                    speaker.Speak(err_msg)
                except Exception:
                    pass
            continue

        # Format and speak the report in one continuous utterance
        format_and_speak(wdict, city, speaker)


if __name__ == "__main__":
    main()