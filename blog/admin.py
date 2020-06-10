from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'date_posted', 'picture']

admin.site.register(Comment)
