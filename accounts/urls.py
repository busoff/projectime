from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('user_exists/', views.user_exists, name='user_exists'),
    path('userid_exists/', views.userid_exists, name='userid_exists'),
    path('', views.signin, name="home")
]