# Weather App (Python (streamlit))

# Weather App

Welcome to the Weather App! This Python application uses the Streamlit library to provide you with current weather information based on the OpenWeatherMap API. With a clean and user-friendly interface, you can quickly get essential weather details for any city around the world.

## Features

- **Current Weather Information:** Get real-time weather updates, including temperature, humidity, and wind speed.
- **Sunrise and Sunset Times:** Know when the sun will rise and set in your selected location.
- **Multi-Language Support:** Choose your preferred language for weather information.

## Usage

1. **Select Language:** Choose your preferable language from the dropdown menu.
2. **Enter City:** Input the name of the city you want to get weather information for.
3. **Weather Details:** View detailed information such as weather type, description, humidity, and temperature.
4. **Sunrise and Sunset Times:** Find out when the sun will rise and set in the selected city.
5. **Wind Information:** Check the wind speed in the specified location.
6. **Current Date and Time:** See the current date and time in the selected city's timezone.

## Developer Section

Explore the API usage and example codes in the developer section:

- **API Documentation:** Understand how to use the OpenWeatherMap API to retrieve weather data.

```python
# GET WEATHER DATA BY CITY_NAME
https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}
```

## Getting Started
To run the Weather App locally, make sure you have Python installed. Install the required libraries using:

```python
#install streamlit and requests
pip install streamlit requests
```

```python
#run streamlit application
streamlit run Main.py
```

Feel free to explore and contribute to the project! 🌦️

```javascript
Please replace `{city_name}`, `{api_key}` with your actual values.
```
