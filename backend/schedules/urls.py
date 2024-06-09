from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('new/', views.schedule_create, name='schedule_create'),
    path('<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
    path('<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),
    path('work/<int:pk>/delete/', views.work_delete, name='work_delete'),
]
