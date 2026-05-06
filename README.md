# 🌦️ Python Weather Announcer with Voice

A Python-based weather assistant that fetches **current conditions** and a **3-day forecast** using the [WeatherAPI](https://www.weatherapi.com/) and announces them aloud with Windows’ built-in text-to-speech (SAPI).

---
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![WeatherAPI](https://img.shields.io/badge/API-WeatherAPI-green)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Made by Shashank](https://img.shields.io/badge/Made%20by-Shashank%20Raut-orange?logo=github)
![Powered by SAPI Voice](https://img.shields.io/badge/Powered%20by-SAPI%20Voice-lightblue)

## 🚀 Features
- 🎙️ Voice output using `win32com.client` (SAPI.SpVoice)
- 🌡️ Current weather: temperature (°C/°F), condition, humidity, wind speed & direction, feels-like temp
- ☀️ Extra details: UV index, pressure, visibility, last updated time
- 📅 3-day forecast: condition, high/low temps, average humidity
- 🌄 Sunrise & sunset times for each forecast day
- 🛑 Exit anytime by typing `stop`

---

## 📂 Project Structure
- `weather_announcer.py` → Main script with voice + weather logic  
- `README.md` → Documentation for setup and usage  

---

## 🔧 Requirements
- Python 3.x  
- Libraries:  
  - `requests`  
  - `json` (built-in)  
  - `pywin32` (for Windows voice engine)  

Install dependencies:
```bash
pip install requests pywin32




# 🌦️ Python Weather Announcer with Voice

A Python-based weather assistant that fetches **current conditions** and a **3-day forecast** using the [WeatherAPI](https://www.weatherapi.com/) and announces them aloud with Windows’ built-in text-to-speech (SAPI).

---
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![WeatherAPI](https://img.shields.io/badge/API-WeatherAPI-green)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Made by Shashank](https://img.shields.io/badge/Made%20by-Shashank%20Raut-orange?logo=github)
![Powered by SAPI Voice](https://img.shields.io/badge/Powered%20by-SAPI%20Voice-lightblue)

## 🚀 Features
- 🎙️ Voice output using `win32com.client` (SAPI.SpVoice)
- 🌡️ Current weather: temperature (°C/°F), condition, humidity, wind speed & direction, feels-like temp
- ☀️ Extra details: UV index, pressure, visibility, last updated time
- 📅 3-day forecast: condition, high/low temps, average humidity
- 🌄 Sunrise & sunset times for each forecast day
- 🛑 Exit anytime by typing `stop`

---

## 📂 Project Structure
- `weather_announcer.py` → Main script with voice + weather logic  
- `README.md` → Documentation for setup and usage  

---

## 🔧 Requirements
- Python 3.x  
- Libraries:  
  - `requests`  
  - `json` (built-in)  
  - `pywin32` (for Windows voice engine)  

Install dependencies:
```bash
pip install requests pywin32
