from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Resource, Schedule, Work
from .forms import ResourceForm, ResourceFormSet, ScheduleForm, WorkForm, WorkFormSet


def schedule_list(request):
    schedules = Schedule.objects.all()
    template = 'schedules/schedule_list.html'
    return render(request, template, {'schedules': schedules})


def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    works = Work.objects.filter(schedule=schedule)
    resources = Resource.objects.all()
    template = 'schedules/schedule_detail.html'
    return render(request, template, {
        'schedule': schedule,
        'works': works,
        'resources': resources
    })


@login_required
def schedule_create(request):
    template = 'schedules/schedule_create.html'
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        work_form = WorkForm(request.POST)
        if form.is_valid() and work_form.is_valid():
            schedule = form.save(commit=False)
            schedule.author = request.user
            schedule.save()
            work = work_form.save(commit=False)
            work.schedule = schedule
            work.save()
            return redirect('schedules:schedule_update', pk=schedule.pk)
    else:
        form = ScheduleForm()
        work_form = WorkForm()
    return render(request, template, {'form': form, 'work_form': work_form})


@login_required
def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    template = 'schedules/schedule_update.html'
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedules:schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, template, {'form': form})


@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    template = 'schedules/schedule_confirm_delete.html'
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedules:schedule_list')
    return render(request, template, {'schedule': schedule})


@login_required
def work_create(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    template = 'schedules/work_create.html'
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.schedule = schedule
            work.save()
            return redirect('schedules:schedule_update', pk=schedule.pk)
    else:
        form = WorkForm()
    return render(request, template, {
        'form': form,
        'schedule_pk': schedule_pk
    })


@login_required
def work_update(request, pk):
    work = get_object_or_404(Work, pk=pk)
    schedule_pk = work.schedule.pk
    template = 'schedules/work_update.html'
    if request.method == "POST":
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('schedules:schedule_update', pk=schedule_pk)
    else:
        form = WorkForm(instance=work)
    return render(request, template, {
        'form': form,
        'schedule_pk': schedule_pk
    })


@login_required
def work_delete(request, pk):
    work = get_object_or_404(Work, pk=pk)
    schedule = work.schedule
    template = 'schedules/work_confirm_delete.html'
    if request.method == 'POST':
        work.delete()
        return redirect('schedules:schedule_update', pk=schedule.pk)
    return render(request, template, {'work': work})


@login_required
def resource_create(request, work_pk):
    work = get_object_or_404(Work, pk=work_pk)
    template = 'schedules/resource_form.html'
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.work = work
            resource.save()
            return redirect('schedules:work_update', pk=work.pk)
    else:
        form = ResourceForm()
    return render(request, template, {'form': form, 'work_pk': work_pk})


@login_required
def resource_update(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    template = 'schedules/resource_form.html'
    work = resource.work
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('schedules:work_update', pk=work.pk)
    else:
        form = ResourceForm(instance=resource)
    return render(request, template, {'form': form})


@login_required
def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    template = 'schedules/resource_confirm_delete.html'
    work = resource.work
    if request.method == "POST":
        resource.delete()
        return redirect('schedules:work_update', pk=work.pk)
    return render(request, template, {'resource': resource})
