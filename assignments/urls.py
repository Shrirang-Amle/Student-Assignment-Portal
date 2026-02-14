from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_preferences, name='home'),
    path('set/', views.set_preferences, name='set_preferences'),
    path('show/', views.show_preferences, name='show_preferences'),
    path('submit/', views.submit_assignment, name='submit_assignment'),
    path('list/', views.list_assignments, name='list_assignments'),
]
