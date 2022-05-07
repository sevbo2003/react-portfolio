from django.contrib import admin
from .models import Music, Design


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'added')
    list_filter = ('added',)
    search_fields = ('name', 'author')


@admin.register(Design)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'author',)
    search_fields = ('time', 'author',)
