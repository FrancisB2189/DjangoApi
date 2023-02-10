from django.urls import path
from . import views

urlpatterns = [
    path('', views.Curves, name = 'ApiTest'),
    path('universities', views.Unis, name = 'Universities'),
]