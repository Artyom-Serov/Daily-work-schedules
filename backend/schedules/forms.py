from django import forms
from .models import Resource, Schedule, Work


class ScheduleForm(forms.ModelForm):
    """Форма для создания и редактирования графика."""
    class Meta:
        model = Schedule
        fields = ['title', 'description']
        labels = {
            'title': 'Название',
            'description': 'Описание',
        }


class WorkForm(forms.ModelForm):
    """Форма для создания и редактирования работ."""
    class Meta:
        model = Work
        fields = ['name', 'start_date', 'end_date']
        labels = {
            'name': 'Вид работ',
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
        }


class ResourceForm(forms.ModelForm):
    """Форма для создания и редактирования ресурсов."""
    class Meta:
        model = Resource
        fields = ['name', 'quantity', 'unit']
        labels = {
            'name': 'Наименование ресурса',
            'quantity': 'Количество ресурса',
            'unit': 'Единицы измерения',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
        }


WorkFormSet = forms.inlineformset_factory(
    Schedule, Work, form=WorkForm, extra=1, can_delete=True
)
ResourceFormSet = forms.inlineformset_factory(
    Work, Resource, form=ResourceForm, extra=1, can_delete=True
)
