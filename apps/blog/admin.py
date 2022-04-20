from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'time')
    list_filter = ('category', 'created')
    search_fields = ('name', 'description')
