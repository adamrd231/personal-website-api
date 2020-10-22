from django.contrib import admin
from .models import Projects, Photos, Categories

# Register your models here.
admin.site.register(Projects)
admin.site.register(Photos)
admin.site.register(Categories)