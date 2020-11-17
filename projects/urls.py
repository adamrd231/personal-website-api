from django.contrib import admin;
from django.urls import path;
from rest_framework import routers;
from django.conf.urls import include;
from .views import ProjectViewSet, PhotoViewSet, CategoryViewSet, BlogViewSet, QuoteViewSet;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('photos', PhotoViewSet)
router.register('categories', CategoryViewSet)
router.register('blog', BlogViewSet)
router.register('quotes', QuoteViewSet)


    path('summernote/', include('django_summernote.urls')),
] 

url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':"path\to\your\static\folder"}),

urlpatterns = [
    path('', include(router.urls)),
urlpatterns += staticfiles_urlpatterns()
