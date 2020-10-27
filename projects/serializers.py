from rest_framework import serializers;
from .models import Projects, Photos, Categories
from django.contrib.auth.models import User

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'image_name', 'project_image']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'category', 'category_name', 'title', 'description', 'technology', 'image', 'image_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']