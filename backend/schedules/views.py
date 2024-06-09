from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Schedule, Work
from .forms import ScheduleForm, WorkFormSet


def schedule_list(request):
    schedules = Schedule.objects.all()
    template = 'schedules/schedule_list.html'
    return render(request, template, {'schedules': schedules})


def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    works = Work.objects.filter(schedule=schedule)
    template = 'schedules/schedule_detail.html'
    return render(request, template, {'schedule': schedule, 'works': works})


@login_required
def schedule_create(request):
    template = 'schedules/schedule_form.html'
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        formset = WorkFormSet(request.POST, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            schedule = form.save(commit=False)
            schedule.author = request.user
            schedule.save()
            formset.instance = schedule
            formset.save()
            return redirect('schedules:schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm()
        formset = WorkFormSet(instance=form.instance)
    return render(request, template, {'form': form, 'formset': formset})


@login_required
def schedule_edit(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    template = 'schedules/schedule_form.html'
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        formset = WorkFormSet(request.POST, instance=schedule)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('schedules:schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm(instance=schedule)
        formset = WorkFormSet(instance=schedule)
    return render(request, template, {'form': form, 'formset': formset})


@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    template = 'schedules/schedule_confirm_delete.html'
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedules:schedule_list')
    return render(request, template, {'schedule': schedule})


@login_required
def work_delete(request, pk):
    work = get_object_or_404(Work, pk=pk)
    schedule_pk = work.schedule.pk
    work.delete()
    return redirect('schedules:schedule_edit', pk=schedule_pk)
