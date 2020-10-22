from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProjectViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls))
]