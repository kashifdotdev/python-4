import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

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

# Function to get the latest news articles from OpenWeather Blog using BeautifulSoup
def get_articles():
    url = "https://openweather.co.uk/blog/category/weather"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the response contains the expected content
    st.write("Raw HTML:", soup.prettify())  # Debug: Print the raw HTML to see the structure

    # Extract article titles, dates, summaries, and tags
    articles = []
    for article in soup.find_all('article'):
        title = article.find('h2').text.strip() if article.find('h2') else 'No Title'
        date = article.find('time')['datetime'] if article.find('time') else None
        summary = article.find('div', class_='entry-summary').text.strip() if article.find('div', class_='entry-summary') else 'No summary available'
        
        # Extract hashtags (if present)
        tags = [tag.text.strip() for tag in article.find_all('a', class_='tag')]  # Example of extracting tags (if available)
        
        # Append the article information to the list
        articles.append({
            "Title": title,
            "Date": date,
            "Summary": summary,
            "Tags": ', '.join(tags)  # Combine tags as a string for display
        })

    # Convert to DataFrame
    articles_df = pd.DataFrame(articles)

    # Only convert Date to datetime if it exists
    if 'Date' in articles_df.columns:
        articles_df['Date'] = pd.to_datetime(articles_df['Date'], errors='coerce')

    return articles_df

# Streamlit UI elements
def display_weather_and_articles():
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

    # Fetch and display news articles
    st.subheader("Latest Weather News Articles")
    articles_df = get_articles()

    if articles_df.empty:
        st.write("No articles found.")
    else:
        # Filter for the latest 5 articles, or modify the number to suit your needs
        latest_articles = articles_df.head(5)

        for _, article in latest_articles.iterrows():
            with st.expander(article['Title']):
                st.write(f"**Date**: {article['Date']}")
                st.write(f"**Tags**: {article['Tags']}")
                st.write(f"**Summary**: {article['Summary']}")

# Run the app
if __name__ == "__main__":
    display_weather_and_articles()