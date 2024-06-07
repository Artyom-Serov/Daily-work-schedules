from django.contrib import admin
from .models import Schedule, Work, Resource


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'last_modified', 'description')
    search_fields = ('title', 'author__username')
    list_filter = ('last_modified', 'author')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'schedule')
    search_fields = ('name', 'schedule__title')
    list_filter = ('start_date', 'end_date', 'schedule')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    search_fields = ('name',)
    list_filter = ('unit', 'name')
