from django import forms
from .models import Schedule, Work


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = [
            'name', 'start_date', 'end_date',
            'resource_name', 'resource_quantity', 'resource_unit'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
