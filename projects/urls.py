from django.contrib import admin;
from django.urls import path;
from rest_framework import routers;
from django.conf.urls import include;
from .views import ProjectViewSet, PhotoViewSet, CategoryViewSet, BlogViewSet, QuoteViewSet;

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('photos', PhotoViewSet)
router.register('categories', CategoryViewSet)
router.register('blog', BlogViewSet)
router.register('quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summernote/', include('django_summernote.urls')),
] 