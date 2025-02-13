import streamlit as st
import requests

# Function to get weather data
def get_weather(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

# Streamlit app
def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

    # Custom CSS for background and styling
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #fff;
        }
        .card {
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 20px rgba(0,0,0,0.2);
            text-align: center;
        }
        .weather-icon {
            font-size: 50px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Title
    st.markdown('<h1 class="title">🌍 Weather App</h1>', unsafe_allow_html=True)

    # API Key and input field
    api_key = 'YOUR_API_KEY'  # Replace with your actual OpenWeatherMap API Key
    city_name = st.text_input("🌆 Enter City Name:", placeholder="e.g., New York, London, Tokyo")

    if city_name:
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather(city_name, api_key)

        if weather_data.get('cod') == 200:
            temp = weather_data['main']['temp']
            desc = weather_data['weather'][0]['description'].title()
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            # Display weather data in a card layout
            st.markdown(
                f"""
                <div class="card">
                    <h2>🌆 {city_name}</h2>
                    <p class="weather-icon">🌤️</p>
                    <h3>{temp}°C</h3>
                    <p><b>Condition:</b> {desc}</p>
                    <p><b>Humidity:</b> {humidity}% 💧</p>
                    <p><b>Wind Speed:</b> {wind_speed} m/s 💨</p>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.error("❌ City not found or invalid API key. Please try again.")

if __name__ == "__main__":
    main()
