from django.contrib import admin
from .models import Category, Post, Project

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'time')
    list_filter = ('category', 'created')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time')
    list_filter = ('created',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('title',)}
