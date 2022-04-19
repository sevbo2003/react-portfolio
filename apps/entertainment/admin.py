from django.contrib import admin
from .models import Music, Gallery


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'length', 'added')
    list_filter = ('length', 'added')
    search_fields = ('name', 'author')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'time', 'size')
    search_fields = ('name',)
