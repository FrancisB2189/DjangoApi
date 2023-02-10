from django.shortcuts import render
from django.http import HttpResponse
import requests

def Products(request):
    response = requests.get('https://fakestoreapi.com/products')
    Products = response.json()
    print(Products)    

    return render(request, "ApiTest.html", {'products': Products})
    pass


def Unis(request):
    response = requests.get('http://universities.hipolabs.com/search?country=Netherlands')
    Unis = response.json()
    print(Unis)    

    return render(request, "universities.html", {'universities': Unis})
    pass