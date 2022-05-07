from django.contrib import admin
from .models import MySetup, DailyUses, Accessories, Development, Keyboard, Link

admin.site.register(MySetup)
admin.site.register(Link)


@admin.register(DailyUses)
class DailyUsesAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'active')
    list_filter = ('active',)
    search_fields = ('type', 'name')


@admin.register(Accessories)
class DailyUsesAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'active')
    list_filter = ('active',)
    search_fields = ('type', 'name')


@admin.register(Development)
class DailyUsesAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'active')
    list_filter = ('active',)
    search_fields = ('type', 'name')


@admin.register(Keyboard)
class DailyUsesAdmin(admin.ModelAdmin):
    list_display = ('name', 'added')
    list_filter = ('added',)
    search_fields = ('name', 'description')
    search_help_text = 'Search by name'

