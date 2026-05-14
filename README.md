# 🌦️ Weather TTS Reporter

A Python-based weather assistant that fetches **current conditions** and a **3-day forecast** using the [WeatherAPI](https://www.weatherapi.com/) and announces them aloud with Windows’ built-in text-to-speech (SAPI). If TTS is unavailable, the program gracefully falls back to console output.

---

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![WeatherAPI](https://img.shields.io/badge/API-WeatherAPI-green)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Made by Shashank](https://img.shields.io/badge/Made%20by-Shashank%20Raut-orange?logo=github)
![Powered by SAPI Voice](https://img.shields.io/badge/Powered%20by-SAPI%20Voice-lightblue)

---

## 🚀 Features
- 🎙️ Continuous voice output using `win32com.client` (SAPI.SpVoice)  
- 🌡️ Current weather: temperature (°C/°F), condition, humidity, wind speed & direction, feels-like temp  
- ☀️ Extra details: UV index, pressure, visibility, last updated time  
- 📅 3-day forecast: condition, high/low temps, average humidity  
- 🌄 Sunrise & sunset times for each forecast day  
- 🛑 Exit anytime by typing `stop`  

---

## 📂 Project Structure
- `main.py` → Main script with weather fetching + TTS logic  
- `README.md` → Documentation for setup and usage  

---

## 🔧 Requirements
- Python **3.8+**  
- Libraries:  
  - `requests`  
  - `pywin32` (for Windows voice engine; optional fallback to console if unavailable)  

Install dependencies:
```bash
pip install requests pywin32
