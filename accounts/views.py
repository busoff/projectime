from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib.auth.models import User
from hello.models import Profile

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {})

    elif request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'])

        profile = Profile()
        profile.user = user
        print("****myid: %s"%(request.POST['userid']))
        profile.myid = request.POST['userid']
        profile.save()

        return redirect("accounts:login")
    else:
        raise Http404("method does not exist for sign in")
    
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', {})

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/projecttime/%s"%(user.profile.myid))
        else:
            print("invalid signin")
            return render(request, 'accounts/signin.html', {"signin_error":True})

    else:
        raise Http404("method does not exist for sign in")


def signout(request):
    logout(request)

    return redirect("accounts:login")