from rest_framework import serializers;
from .models import Projects, Photos, Categories, Blog, Quotes
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'image_name', 'project_image']


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'quote', 'quote_author']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'slug', 'category', 'category_name', 'website', 'website_button_text', 'title', 'tagline', 'description', 'technology', 'quotes', 'quote_string', 'image', 'image_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Blog
        fields = ['id', 'slug', 'title', 'author', 'created_on', 'updated_on', 'blog']

