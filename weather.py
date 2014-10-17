#!/usr/bin/env python

from urllib2 import Request, urlopen, URLError
import json
import datetime
request = Request('http://api.openweathermap.org/data/2.5/forecast/daily?q=London&units=imperial&cnt=14')
def summarise_forecast(city):
    try:
        response = urlopen(request)
        cities = json.loads(response.read().decode("UTF-8"))
        if cities["city"]["name"] == city:
            for data in cities:
                if data == "city":
                    forecast={'city':cities[data]["name"]}
                elif data == "list":
                    rain=[]
                    clear=[]
                    for lst in cities[data]:
                        date=datetime.datetime.fromtimestamp(lst["dt"]).strftime('%Y-%m-%d')
                        mini = lst["temp"]["min"]
                        maxi = lst["temp"]["max"]
                        forecast["min"]=mini
                        forecast["max"]=maxi
                        if 'rain' in lst:
                            rain.append(date)
                        else:
                           clear.append(date)
                    forecast['Rain']=rain
                    forecast['Clear']=clear
            print forecast
    except URLError, e:
        print 'No kittez. Got an error code:', e

cityname=raw_input("Enter City name: ")
summarise_forecast(cityname)
