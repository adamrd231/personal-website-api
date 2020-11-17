from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

# Create your models here
class Photos(models.Model):
    image_name = models.TextField()
    project_image = models.ImageField(upload_to='photos/', null=True, blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 15)

    def admin_photo(self):
        print(self.project_image)
        return mark_safe('<img src="{}", height="{height}", width="{width}" />'
            .format("https://website-portfolio-rdconcepts.herokuapp.com/" + str(self.project_image),
            height=100,
            width=100))
        
    admin_photo.short_description = "image_name"
    admin_photo.allow_tags = True

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

class Quotes(models.Model):
    quote = models.TextField()
    quote_author = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.quote_author


# Projects model to display on portfolio section, images will be served and a single-page template will display the work. 
class Projects(models.Model):
    #Basic information about project, used to display information on project templates.
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, default="", blank=True, null=True)
    tagline = models.CharField(max_length=250, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    website_button_text = models.CharField(max_length=100, blank=True, null=True)
    
    technology = models.CharField(max_length=20)

    #Quotes attributed with the project
    quotes = models.ManyToManyField(Quotes, related_name='quotes', blank=True)
    def quote_string(self):
        return Quotes.objects.filter(quotes=self).values_list('quote', 'quote_author')


    # Category used to sort projects
    category = models.ForeignKey('Categories', related_name="categories", on_delete=models.CASCADE, blank=True, null=True)
    def category_name(self):
        return Categories.objects.filter(categories=self).values_list('name', flat=True)

    #Image associated with project
    # TODO Change to one to one relationship.
    image = models.ManyToManyField(Photos, related_name='photos', blank=True)
    def image_url(self): 
        return Photos.objects.filter(photos=self).values_list('project_image', flat=True)


    description = models.TextField()

    # Formats the name displayed when viewing the Django Database
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"    

    


        
# Blog model to keep track of blog posts on the website. No images will be served with the blog posts.
class Blog(models.Model):
    #Basic information about project, used to display information on blog templates.
    title = models.CharField(max_length=100)

    #Slug and Categories used to sort and filter projects
    slug = models.SlugField(max_length=200, unique=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    blog = models.TextField()
    
    def image_url(self): 
        return Photos.objects.filter(photos=self).values_list('project_image', flat=True)

    class Meta:
        verbose_name_plural = "Blog"    

    def __str__(self):
        return self.title