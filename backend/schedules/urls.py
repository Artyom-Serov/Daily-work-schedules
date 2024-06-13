from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('create/', views.schedule_create, name='schedule_create'),
    path('<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('<int:pk>/update/', views.schedule_update, name='schedule_update'),
    path('<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),
    path('work/create/<int:schedule_pk>/', views.work_create, name='work_create'),
    path('work/update/<int:pk>/', views.work_update, name='work_update'),
    path('work/delete/<int:pk>/', views.work_delete, name='work_delete'),
    path('resource/create/<int:work_pk>/', views.resource_create, name='resource_create'),
    path('resource/update/<int:pk>/', views.resource_update, name='resource_update'),
    path('resource/delete/<int:pk>/', views.resource_delete, name='resource_delete'),
]
