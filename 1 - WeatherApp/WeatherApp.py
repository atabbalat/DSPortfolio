# Weather App
# Abed Tabbalat

import requests
import json
import pprint

# This class holds the weather data return from the API
class WeatherData:
    def __init__(self, zipcode, city, city_name,country, feels_like, weather_description, humidity, wind_speed, curr_temp, high_temp, low_temp, wind_degree):
        self.zipcode = zipcode
        self.city = city
        self.city_name = city_name
        self.country = country
        self.feels_like = feels_like
        self.weather_description = weather_description
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.curr_temp = curr_temp
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.wind_degree = wind_degree
    
    # Dynamically prints out the weather data based on user inputs regarding temperature unit type.
    def print(self, temp_type):
        if temp_type.lower() == 'celcius':
            c_f_k = 'C'
            wind_speed_units = 'm/s'
        elif temp_type.lower() == 'fahrenheit':
            c_f_k = 'F'
            wind_speed_units = 'mph'
        elif temp_type.lower() == 'kelvin':
            c_f_k = 'K'
            wind_speed_units = 'm/s'

        feels_like_description = f'Feels like {self.feels_like}°{c_f_k}. {self.weather_description}. Humidity at {self.humidity}%'
        if self.city:
            print(f'\nWeather conditions for the city of {self.city}, {self.country} in {temp_type} (°{c_f_k}):')
        elif self.zipcode:
            print(f'\nWeather conditions for the area {self.zipcode}, {self.city_name} {self.country} in {temp_type} (°{c_f_k}):')

        print(feels_like_description)
        print('-' * len(feels_like_description))
        print(f'Current temperature: {self.curr_temp}°{c_f_k}')
        print(f'High temperature: {self.high_temp}°{c_f_k}')
        print(f'Low temperature: {self.low_temp}°{c_f_k}')
        print(f'Wind speed: {self.wind_speed} {wind_speed_units} {self.wind_degree}')
        print('-' * len(feels_like_description))

# Fetches data from open weather map API based on user input for city/zipcode & temperature units, 
# and returns a new WeatherData object containing data from the API 
def fetch_data(city, zipcode, units):
    if units == 'c':
        units_query = '&units=metric'
    elif units == 'f':
        units_query = '&units=imperial'
    elif units == 'k':
        units_query = ''

    if city:
        loc_query = f'q={city}'
    elif zipcode:
        loc_query = f'zip={zipcode},us'

    api_key = 'api here'
    url = f'http://api.openweathermap.org/data/2.5/weather?{loc_query}{units_query}&appid={api_key}'
    resp = requests.request ('GET', url)
    data = json.loads (resp.text)

    city_name = data['name']
    country = data['sys']['country']
    feels_like = data['main']['feels_like']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    curr_temp = data['main']['temp']
    high_temp = data['main']['temp_max']
    low_temp = data['main']['temp_min']
    wind_degree = wind_direction (data ['wind']['deg'])

    return WeatherData(zipcode if zipcode else None, city if city else None, city_name, country, feels_like, weather_description, humidity, wind_speed, curr_temp, high_temp, low_temp, wind_degree)

# Translates wind direction degrees into cardinal directions.
def wind_direction(angle):
    val=int((angle/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return(arr[(val % 16)])

def main():
    print('Welcome to Rezan Weather Application')
    
    while True:
        print('\nFor City, type 1')
        print('For Zip Code, type 2\n')
        
        while True:
            try:
                city_or_zip = int(input('Please choose between City or Zip Code: '))
                break
            except ValueError:
                print ('please input valid number!')
                continue

        if city_or_zip == 1:
            while True:
                city_input = input('Please enter city name: ')
                print('\nFor Fahrenheit, type 1')
                print('For Celcius, type 2')
                print('For Kelvin, type 3\n')
                while True:
                    try:
                        temp_type_input = int(input('Input temperature type of choice: '))
                        break
                    except ValueError:
                        print ('please input valid number!')
                        continue
                if temp_type_input == 1:
                    try:
                        weather_data = fetch_data(city_input, None, 'f')
                        weather_data.print('Fahrenheit')
                        break
                    except:
                        print('Please input a valid city name.')
                        continue
                elif temp_type_input == 2:
                    try:
                        weather_data = fetch_data(city_input, None, 'c')
                        weather_data.print('Celcius')
                        break
                    except:
                        print('Please input a valid city name.')
                        continue
                elif temp_type_input == 3:
                    try:
                        weather_data = fetch_data(city_input, None, 'k')
                        weather_data.print('Kelvin')
                        break
                    except:
                        print('Please input a valid city name.')
                        continue
                else:
                    print('Input Error: Please input a valid number!')
                    continue

        elif city_or_zip == 2:
            while True:
                zip_input = input('Please enter zip code (zip code allowed only in US territory): ')
                print('\nFor Fahrenheit, type 1')
                print('For Celcius, type 2')
                print('For Kelvin, type 3\n')
                while True:
                    try:
                        temp_type_input = int(input('Input temperature type of choice: '))
                        break
                    except ValueError:
                        print ('please input valid number!')
                        continue
                if temp_type_input == 1:
                    try:
                        weather_data = fetch_data(None, zip_input, 'f')
                        weather_data.print('Fahrenheit')
                        break
                    except:
                        print('Please input a valid Zip Code. Make sure it is in US territory.')
                        continue
                elif temp_type_input == 2:
                    try:
                        weather_data = fetch_data(None, zip_input, 'c')
                        weather_data.print('Celcius')
                        break
                    except:
                        print('Please input a valid Zip Code. Make sure it is in US territory.')
                        continue
                elif temp_type_input == 3:
                    try:
                        weather_data = fetch_data(None, zip_input, 'k')
                        weather_data.print('Kelvin')
                        break
                    except:
                        print('Please input a valid Zip Code. Make sure it is in US territory.')
                        continue
                else:
                    print('Input Error: Please input a valid number!')
                    continue

        else:
            print('Input Error: Please input a valid number!')
            continue

        again_input = input('Would you like to search again? (Y/N): ').lower()
        if again_input == 'y':
            continue
        else:
            print('Thank you for using Rezan Weather, have a great day!')
            break

if __name__ == "__main__":
    main()
