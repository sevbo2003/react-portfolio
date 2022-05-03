from django.contrib import admin
from .models import Category, Post, Project, ChallengeName, Day30

admin.site.register(Category)
admin.site.register(ChallengeName)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time')
    list_filter = ('created',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Day30)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'challenge', 'day', 'description', 'time')
    list_filter = ('created',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('title',)}
