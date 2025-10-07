import requests
from django.shortcuts import render
from decouple import config
from datetime import datetime

def index(request):
    weather_data = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = config('OPENWEATHER_API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'visibility': round(data['visibility'] / 1000, 1),  # convert to km
                'temp_min': data['main']['temp_min'],
                'temp_max': data['main']['temp_max'],
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
                'feels_like': data['main']['feels_like']
            }
        else:
            weather_data['error'] = "City not found. Please try again."

    context = {
        'weather_data': weather_data,
        'current_date': datetime.now().strftime('%A, %d %B %Y')
    }

    return render(request, 'weather/index.html', context)
