from django.contrib import admin
from .models import Projects, Photos, Categories, Blog, Quotes
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe



# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'blog', 'description'


class PhotoAdmin(admin.ModelAdmin):
    fields = ('image_name', 'admin_photo', 'project_image')

    list_display = [
        'image_name',
        'admin_photo',
        'project_image',
        
    ]

    readonly_fields = ('admin_photo',)

# Register your models here.
admin.site.register(Blog, BlogPostAdmin)
admin.site.register(Projects, BlogPostAdmin)
admin.site.register(Categories)
admin.site.register(Quotes)
admin.site.register(Photos, PhotoAdmin)


