from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products, name = 'ApiTest'),
    path('universities', views.Unis, name = 'Universities'),
]