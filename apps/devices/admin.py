from django.contrib import admin
from .models import MySetup, DailyUses, Accessories, Development

admin.site.register(MySetup)


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
