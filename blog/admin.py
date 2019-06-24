from django.contrib import admin

# Register your models here.

from blog.models import Blogger, Topic, Blogpost

# admin.site.register(Blogpost)
# admin.site.register(Blogger)
admin.site.register(Topic)

# Define the admin class
class BloggerAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)

# Register the Admin classes for Blogpost using the decorator
@admin.register(Blogpost)
class Blogpost(admin.ModelAdmin):
    list_display = ('title', 'blogger')



