from django.shortcuts import render;
from rest_framework import viewsets;
from rest_framework.response import Response;

from .serializers import ProjectSerializer, PhotoSerializer, CategorySerializer, BlogSerializer, QuoteSerializer;
from .models import Projects, Photos, Categories, Blog, Quotes;

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer