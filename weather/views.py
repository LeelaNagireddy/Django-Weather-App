import requests
from django.shortcuts import render
from decouple import config 

def index(request):
    weather_data = {}

    if 'city' in request.GET:
        city = request.GET['city']
        api_key = config('OPENWEATHER_API_KEY') 
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                
            }
        else:
            weather_data['error'] = "City not found. Try again."

    return render(request, 'weather/index.html', {'weather': weather_data})
