from django.contrib import admin
from .models import Projects, Photos, Categories, Blog, Quotes

# Register your models here.
admin.site.register(Projects)
admin.site.register(Photos)
admin.site.register(Categories)
admin.site.register(Blog)
admin.site.register(Quotes)