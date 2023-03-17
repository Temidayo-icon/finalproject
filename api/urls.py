from django.urls import path
from .views import create_reading

urlpatterns = [
    path('api/post', create_reading, name='create_reading'),
     path('api/get', get_readings, name='get_readings'),
]
