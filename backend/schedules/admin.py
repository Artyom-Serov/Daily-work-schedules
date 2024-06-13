from django.contrib import admin
from .models import Schedule, Work, Resource


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1


class WorkInline(admin.TabularInline):
    model = Work
    extra = 1


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'last_modified')
    search_fields = ('title', 'author__username', 'description')
    list_filter = ('author', 'last_modified')
    inlines = [WorkInline]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule', 'start_date', 'end_date')
    search_fields = ('name', 'schedule__title')
    list_filter = ('start_date', 'end_date')
    inlines = [ResourceInline]


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'work')
    search_fields = ('name', 'work__name')
    list_filter = ('unit',)
