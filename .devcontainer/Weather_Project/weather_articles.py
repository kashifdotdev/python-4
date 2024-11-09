import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL of the blog page
url = "https://openweather.co.uk/blog"

# Send a GET request to fetch the content of the page
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all blog post elements (based on the HTML structure)
    posts = soup.find_all('div', class_='post')

    # Get current date for filtering
    current_date = datetime.now()

    # Extract dates and categories for filter options
    available_dates = []
    available_categories = set()

    # Loop through each post to gather dates and categories for filtering
    for post in posts:
        date = post.find('p', class_='post__date')
        category = post.find('span', class_='post__category')

        # Add date to the available dates list
        if date:
            available_dates.append(date.get_text(strip=True))
        
        # Add category to the available categories set
        if category:
            available_categories.add(category.get_text(strip=True))

    # Streamlit filters for date and category
    date_filter = st.selectbox("Select a Date", options=["All"] + sorted(set(available_dates), reverse=True))
    category_filter = st.selectbox("Select a Category", options=["All"] + list(available_categories))

    # Title for the app
    st.title("Filtered Articles from Blog")

    # Loop through each post and apply the filters
    for post in posts:
        title = post.find('h2', class_='post__title')
        if title:
            title_text = title.get_text(strip=True)  # Extract the title text
            link = title.find('a')['href']  # Get the URL of the article

            date = post.find('p', class_='post__date')
            date_text = date.get_text(strip=True) if date else 'Date not available'

            summary = post.find('div', class_='post__summary')
            summary_text = summary.get_text(strip=True) if summary else 'No summary available'

            category = post.find('span', class_='post__category')
            category_text = category.get_text(strip=True) if category else 'Uncategorized'

            # Filter by date
            if date_filter != "All" and date_filter != date_text:
                continue

            # Filter by category
            if category_filter != "All" and category_filter != category_text:
                continue

            # Display the article details on Streamlit
            st.subheader(title_text)  # Display title as a subheader
            st.write(f"**Link**: [Click here]({link})")  # Display the article link
            st.write(f"**Date**: {date_text}")  # Display the article date
            st.write(f"**Category**: {category_text}")  # Display the article category
            st.write(f"**Summary**: {summary_text}")  # Display the article summary
            st.markdown("---")  # Add a separator between articles

else:
    st.error("Failed to retrieve the page. Status code: " + str(response.status_code))
