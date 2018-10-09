from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import User, ProjectTimeEntry
# Create your views here.

def index(request):
    return HttpResponse("Hello, Django")

def user_list(request):
    template = loader.get_template("user/index.html")
    context = {
        'user_list': User.objects.all()
    }

    return HttpResponse(template.render(context, request))

def user_id(request, user_id):
    template = loader.get_template("user/project_time.html")
    context = {
        "project_time_list": ProjectTimeEntry.objects.filter(user__user_id=user_id)
    }

    return HttpResponse(template.render(context, request))

def user_name(request, name):
    template = loader.get_template("user/project_time.html")
    context = {
        "project_time_list": ProjectTimeEntry.objects.filter(user__name=name)
    }
    return HttpResponse(template.render(context, request))