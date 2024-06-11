from django import forms
from .models import Schedule, Work


class ScheduleForm(forms.ModelForm):
    """Форма для создания и редактирования графика."""
    class Meta:
        model = Schedule
        fields = ['title', 'description']


class WorkForm(forms.ModelForm):
    """Форма для создания и редактирования работ, ресурсов."""
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


class BaseWorkFormSet(forms.BaseInlineFormSet):
    """Набор форм для работ с кастомной валидацией."""
    def clean(self):
        """Проверка наличия дат для каждой работы."""
        if any(self.errors):
            return
        for form in self.forms:
            if not form.cleaned_data.get('name') or not form.cleaned_data.get(
                    'start_date'
            ) or not form.cleaned_data.get('end_date'):
                raise forms.ValidationError(
                    'Каждая работа должа иметь дату начала и окончания'
                )
        super().clean()


WorkFormSet = forms.inlineformset_factory(
    Schedule, Work, form=WorkForm, formset=BaseWorkFormSet, extra=1,
    can_delete=True
)


class BaseResourceFormSet(forms.BaseInlineFormSet):
    """Набор форм для ресурсов с кастомной валидацией."""
    def clean(self):
        """
        Проверка наличия количества и единиц измерения у каждого ресурса.
        """
        if any(self.errors):
            return
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data.get(
                'resource_name'
            ) and (not form.cleaned_data.get(
                'resource_quantity'
            ) or not form.cleaned_data.get(
                'resource_unit'
            )):
                raise forms.ValidationError(
                    'Если указано название ресурса, то количество '
                    'и единицы измерения тоже должны быть указаны.'
                )
        super().clean()


ResourceFormSet = forms.inlineformset_factory(
    Work, Work, form=WorkForm, formset=BaseResourceFormSet, extra=1,
    can_delete=True
)
