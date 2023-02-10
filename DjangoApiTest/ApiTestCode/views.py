from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def Curves(request):
    response = open('static/curve-group.json').read()
    curves = json.loads(response)
    print(curves)    

    return render(request, "ApiTest.html", {'curves': Curves})
    pass


def Unis(request):
    response = requests.get('http://universities.hipolabs.com/search?country=Netherlands')
    Unis = response.json()
    print(Unis)    

    return render(request, "universities.html", {'universities': Unis})
    pass