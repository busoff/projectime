from django.urls import path, include
from . import views

app_name = 'projecttime'
urlpatterns = [
    path('projects', views.get_projects, name="get_projects"),
    path('entries', views.get_entries, name='get_entries'),
    path('submit_entries', views.submit_entries, name='submit_entries'),
    path('', views.index, name="index"),
    path('test', views.test, name="test"),
]