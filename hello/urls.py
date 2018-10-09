from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user/', views.user_list, name="user_list"),
    path('user/<int:user_id>/', views.user_id, name='user_id'),
    path('user/<name>/', views.user_name, name='user_name'),
]