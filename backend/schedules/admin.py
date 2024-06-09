from django.contrib import admin
from .models import Schedule, Work


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'last_modified', 'description')
    search_fields = ('title', 'author__username')
    list_filter = ('last_modified', 'author')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'start_date', 'end_date', 'schedule',
        'resource_name', 'resource_unit', 'resource_quantity'
    )
    search_fields = ('name', 'schedule__title', 'resource_name')
    list_filter = ('start_date', 'end_date', 'schedule')
