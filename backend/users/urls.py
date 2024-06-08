from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
