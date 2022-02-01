from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import firstFunction
from rest_framework.routers import DefaultRouter
from .views import CarViewset

router = DefaultRouter()
router.register('cars', CarViewset, basename = 'cars')


urlpatterns = [
    url('first', firstFunction),
    url('', include(router.urls))
]