from django.shortcuts import render
from decouple import config
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        key = config('WEATHER_API_KEY')

        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid='+ key

        source = urllib.request.urlopen(url).read()

        list_of_data = json.loads(source)
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinates': str(list_of_data['coord']['lon']) + ', '+ str(list_of_data['coord']['lat']) ,
            'temp': str(list_of_data['main']['temp']),
            'feels_like': str(list_of_data['main']['feels_like']),
            'temp_min': str(list_of_data['main']['temp_min']),
            'temp_max': str(list_of_data['main']['temp_max']),
            'wind_speed': str(list_of_data['wind']['speed']),
            'pressure': str(list_of_data['main']['pressure']), 
            'humidity': str(list_of_data['main']['humidity']), 
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'], 
        }

        print(data)
    else:
        data = {}

    return render(request, 'weather/index.html', data)

<h4><span class="badge badge-primary">Temperature (feels like) :</span> {{feels_like}}</h4>
        <h4><span class="badge badge-primary">Temperature min. :</span> {{temp_min}}</h4>
        <h4><span class="badge badge-primary">Temperature max. :</span> {{temp_max}}</h4>
        <h4><span class="badge badge-primary">Wind Speed:</span> {{wind_speed}}</h4>
