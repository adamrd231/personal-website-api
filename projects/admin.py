from django.contrib import admin
from .models import Projects, Photos, Categories, Blog, Quotes
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'blog', 'description'

# Register your models here.
admin.site.register(Blog, BlogPostAdmin)
admin.site.register(Projects, BlogPostAdmin)
admin.site.register(Photos)
admin.site.register(Categories)
admin.site.register(Quotes)