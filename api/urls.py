from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_reading 

router= DefaultRouter()
router.register('api',create_reading)

urlpatterns = [
    path('',include(router.urls)),
]
