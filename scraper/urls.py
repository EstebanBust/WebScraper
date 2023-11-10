"""
Archivo de configuración de URLs de la aplicación scraper.

Este archivo define las rutas URL para la aplicación scraper.
"""
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('', views.scrape_url, name='scrape_url'),
]
