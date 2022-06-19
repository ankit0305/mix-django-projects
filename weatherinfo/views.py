from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import requests
from urllib3 import HTTPResponse
from .models import City
from .forms import CityForm
from django.contrib import messages

APIKEY = "61b77db3574dd8be5628f6ccd9abd12c"

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + APIKEY

cities = City.objects.all()

def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        weather = {
            'city' : city,
            'temperature' : (city_weather['main']['temp']-32)//1.80,
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'feels_like' : (city_weather['main']['feels_like']-32)//1.80,
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weatherinfo/index.html', context)

# def delete_city_view(request, id=None):

#     city = get_object_or_404(City, id=id)

#     if request.method == 'POST':
#         city.delete()
#         messages.success(request, "City deleted successfully")
#         return HttpResponseRedirect("/weatherinfo")
    
#     form = CityForm()

#     weather_data = []

#     for city in cities:

#         city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

#         weather = {
#             'city' : city,
#             'temperature' : (city_weather['main']['temp']-32)//1.80,
#             'description' : city_weather['weather'][0]['description'],
#             'icon' : city_weather['weather'][0]['icon']
#         }

#         weather_data.append(weather) #add the data for the current city into our list

#     context = {'weather_data' : weather_data, 'form' : form}

#     return render(request, 'weatherinfo/index.html', context)