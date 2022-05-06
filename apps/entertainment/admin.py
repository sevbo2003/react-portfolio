from django.contrib import admin
from .models import Music, Gallery


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'added')
    list_filter = ('added',)
    search_fields = ('name', 'author')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'time', 'size')
    search_fields = ('name',)
