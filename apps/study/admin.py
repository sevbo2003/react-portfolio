from django.contrib import admin
from .models import Book, BookCategory, Reading, Podcast, Talk, Tutorial

admin.site.register(BookCategory)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "status", "added"]
    list_filter = ["category", "status", "added"]
    search_fields = ["name"]


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "added"]
    list_filter = ["type", "added"]
    search_fields = ["name"]


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ("name", "added")
    list_filter = ("added",)
    search_fields = ("name",)
    search_help_text = "Search by name"


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "image_link",
        "time",
    )
    list_filter = ("added",)
    search_fields = ("name", "description")


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "category",
        "time",
    )
    list_filter = ("added",)
    search_fields = ("name", "description")
