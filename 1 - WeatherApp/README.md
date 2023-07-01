# Weather App

The Weather App is a Python application developed by Abed Tabbalat, leveraging OpenWeatherMap's API to fetch weather data based on user input. This application provides users with current, high, and low temperatures, as well as humidity levels, wind speed, wind direction, and a brief description of the weather for a specified location. It supports both city names and US zip codes as input for locations, and users can choose the temperature unit from Celsius, Fahrenheit, or Kelvin.

## Features

1. Accepts city name or US zip code as input.
2. Users can choose their preferred temperature unit: Celsius, Fahrenheit, or Kelvin.
3. Provides comprehensive weather data: current, high, and low temperatures, feels-like temperature, humidity level, wind speed, and wind direction.
4. Translates wind direction degrees into cardinal directions.
5. Prompts for another query after each search, allowing for continuous use.
6. Error handling to ensure correct input values and to handle exceptions during data fetching.

## Code Structure

The project consists of a single Python file with the following key components:

1. `WeatherData`: A class that encapsulates weather information. It includes a print function that dynamically adjusts the displayed data based on the chosen temperature unit.
2. `fetch_data`: A function that fetches weather data from the OpenWeatherMap API. It accepts a city name, US zip code, and temperature unit type as inputs and returns an instance of `WeatherData` with the fetched data.
3. `wind_direction`: A function that translates wind direction from degrees to cardinal directions.
4. `main`: The main function that drives the program. It handles user inputs and calls other functions based on these inputs.

## Prerequisites

1. Python 3.6 or later.
2. The `requests` library for sending HTTP requests.
3. A free API key from [OpenWeatherMap](https://openweathermap.org/api). Replace the placeholder in the `fetch_data` function with your actual API key.

## How to Use

To use the application, simply run the Python script in your terminal or command prompt. The application will guide you through the rest with its prompts.

1. The program will first ask you to choose between providing a city name or a US zip code.
2. After choosing the type of location identifier, you will be asked to input the city name or zip code.
3. Then you will be asked to choose the preferred temperature unit.
4. The program will fetch and display the weather data for the specified location.
5. Finally, you will be asked if you want to perform another search. If you choose to do so, the program will start over from step 1.

## Future Enhancements

1. Add support for zip codes outside the US.
2. Incorporate a graphical user interface (GUI) to enhance user experience.
3. Provide forecast data in addition to the current weather.
4. Add a function to convert wind speed between different units (m/s, mph, km/h).

Please feel free to contribute to the development of this project by submitting pull requests.
