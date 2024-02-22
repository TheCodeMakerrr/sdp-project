from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('yash21/', url_shortener, name='url_shortener'),
    path('yash20/', redirect_to_original, name='redirect_to_original'),
]