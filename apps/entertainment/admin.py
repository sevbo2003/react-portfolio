from django.contrib import admin
from .models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'length', 'added')
    list_filter = ('length', 'added')
    search_fields = ('name', 'author')
