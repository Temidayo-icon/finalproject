from django.urls import path
from . import views

urlpatterns = [
    path('readings/create/', views.create_reading, name='create_reading'),
]
