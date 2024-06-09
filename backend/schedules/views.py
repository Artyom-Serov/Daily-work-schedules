from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Resource, Schedule, Work, WorkResource
from .forms import ResourceForm, ScheduleForm, WorkForm


def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(
        request,
        'schedules/schedule_list.html',
        {'schedule': schedules}
    )


def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    works = Work.objects.filter(schedule=schedule)
    return render(
        request,
        'schedules/schedule_detail.html',
        {'schedule': schedule, 'works': works}
    )


@login_required
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.author = request.user
            schedule.save()
            return redirect('schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm()
    return render(
        request,
        'schedules/schedule_form.html',
        {'form': form}
    )


@login_required
def schedule_edit(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.save()
            return redirect('schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedules/schedule_form.html', {'form': form})


@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(
        request,
        'schedules/schedule_confirm_delete.html',
        {'schedule': schedule}
    )
