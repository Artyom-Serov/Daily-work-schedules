from django.shortcuts import render
from .models import Schedule


def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(
        request,
        'schedules/schedule_list.html',
        {'schedule': schedules}
    )
