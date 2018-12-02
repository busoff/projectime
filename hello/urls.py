from django.urls import path
from . import views

app_name = 'projecttime'
urlpatterns = [
    path('report/entries/', views.get_entries, name='get_entries'),
    path('report/submit_entries', views.submit_entries, name='submit_entries'),

    path('', views.user_list, name="user_list"),
    path('report/<int:user_id>', views.projecttime, name="report"),
]