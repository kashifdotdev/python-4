import streamlit as st
import requests
import pandas as pd

# OpenWeather API key
api_key = "6633aef8728360190c222298e07b8a56"

# Display the title at the top
st.title("Weather Forecasting Panel-Muhammad Kashif")

# Function to get weather data for a given city using the OpenWeather API
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature (°C)": data["main"]["temp"],
            "Weather": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

# Streamlit UI elements
def display_weather():
    # Allow the user to enter any city name
    city_search = st.text_input("Enter any city name:", "").strip()

    # Fetch and display weather data for the searched city
    if city_search:
        weather_data = get_weather_data(city_search)
        if weather_data:
            st.write(f"**Weather in {weather_data['City']}**:")
            st.write(f"Temperature: {weather_data['Temperature (°C)']}°C")
            st.write(f"Weather Condition: {weather_data['Weather']}")
        else:
            st.error("City not found. Please enter a valid city name.")

# Run the app
if __name__ == "__main__":
    display_weather()
