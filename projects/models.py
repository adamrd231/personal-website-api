from django.db import models

# Create your models here
class Photos(models.Model):
    image_name = models.TextField()
    project_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ManyToManyField(Photos, related_name='photos', blank=True)