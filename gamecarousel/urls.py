from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='splashpage'),
path('main/', views.mainpage, name='mainpage'),
]