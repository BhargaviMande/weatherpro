import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5c432a55670099f8f2fd2766f11d863d'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form=CityForm()
    cities=City.objects.all()
    weather_data=[]
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data}


    return render(request, 'weather.html', context)



# Create your views here.
