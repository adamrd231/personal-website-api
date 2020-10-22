from django.shortcuts import render;
from rest_framework import viewsets;
from rest_framework import viewsets;
from rest_framework.response import Response;

from .serializers import ProjectSerializer, PhotoSerializer
from .models import Projects, Photos;

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer