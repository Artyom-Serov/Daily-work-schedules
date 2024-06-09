from django import forms
from .models import Resource, Schedule, Work, WorkResource


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'start_date', 'end_date']


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'unit']


class WorkResourceForm(forms.ModelForm):
    class Meta:
        model = WorkResource
        fields = ['resource', 'quantity']
