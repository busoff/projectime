from django.urls import path
from . import views

app_name = 'projecttime'
urlpatterns = [
    path('report/entries/', views.get_entries, name='get_entries'),
    path('report/submit_entries', views.submit_entries, name='submit_entries'),
    path('report/projects', views.get_projects, name="report"),
    path('report/<int:user_id>', views.projecttime, name="report"),
    path('', views.user_list, name="user_list"),
]