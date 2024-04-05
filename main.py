import requests
import findCoordinates

is_on = True

while is_on:
    city_name = input(f'\nWhat city? ')
    if city_name == 'Exit':
        is_on = False
    else:
        latitude, longitude = findCoordinates.get_coordinates(city_name)

        
    api_key = '54ca707ff07cfbd845e7d2f87726e4e0'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    try:
      response = requests.get(api_url)

      if response.status_code == 200:
        data = response.json()

        temperature_kelvin = data['main']['temp']
        temperature_fahrenheit = (temperature_kelvin - 273.15)*(9/5)+32
        #(_K − 273.15) × 9/5 + 32 =_°F
        weather_description = data['weather'][0]['description']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        timezone = data['timezone']
        country = data['sys']['country']
        city_name = data['name']
        
        print("City Name:", city_name)
        print(f'Current Temperature: {temperature_fahrenheit:.2f} Fahrenheit')
        print(f'Weather Description: {weather_description}')
        print(f'Latitude: {latitude:.2f}')
        print(f'Longitude: {longitude:.2f}')
        print("Timezone:", timezone)
        print("Country:", country)
      else:
        print('Error:', response.status_code)

    except Exception as e:
      print('Error fetching weather data:', e)
