from django.urls import path
from . import views

app_name = 'projecttime'
urlpatterns = [
    # path('', views.index, name='home'),
    path('user/', views.user_list, name="user_list"),
    path('user/<int:user_id>/', views.user_id, name='user_id'),
    path('user/<name>/', views.user_name, name='user_name'),
    path('entries/', views.get_entries, name='get_entries'),
    path('submit_entries', views.submit_entries, name='submit_entries'),

    path('', views.projecttime, name="projecttime"),
    path('<user_id>', views.projecttime, name="home"),
]