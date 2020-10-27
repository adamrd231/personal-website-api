from django.db import models

# Create your models here
class Photos(models.Model):
    image_name = models.TextField()
    project_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name_plural = "Photos"    

    def __str__(self):
        return self.image_name

class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent', )
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


# Projects model to display on portfolio section
class Projects(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ManyToManyField(Photos, related_name='photos', blank=True)
    
    def image_url(self): 
        return Photos.objects.filter(photos=self).values_list('project_image', flat=True)

    class Meta:
        verbose_name_plural = "Projects"    

    def __str__(self):
        return self.title
