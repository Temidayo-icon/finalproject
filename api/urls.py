from django.urls import path
from .views import create_reading
from .views import get_readings
from .views import reset_data


urlpatterns = [
    path('api/post', create_reading, name='create_reading'),
     path('api/get', get_readings, name='get_readings'),
        path('api/reset', reset_data, name='reset_readings'),

]
