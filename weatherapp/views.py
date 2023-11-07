import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    appid='82b797b6ebc625032318e16f1b42c016'
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid
    city='London'
    res=requests.get(url.format(city)).json()
    print(res.text)
    city_info={
        'city':city,
        'temp':res['main']['temp'],
        'icon':res['weather'][0]['icon'],
    }
    
    context={
        'info':city_info
    }
    
    return render(request,'weather/index.html')