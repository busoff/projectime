from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import User, ProjectTimeEntry, Project
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
# Create your views here.


def index(request):
    return render(request, 'projecttime/add.html', 
        {'users': User.objects.all(),
         'projects': Project.objects.all()})


def user_list(request):
    context = {
        'user_list': User.objects.all()
    }
    return render(request, 'projecttime/user.html', context)

def user_id(request, user_id):
    template = loader.get_template("projecttime/index.html")
    context = {
        "project_time_list": ProjectTimeEntry.objects.filter(user__user_id=user_id)
    }

    return HttpResponse(template.render(context, request))

def user_name(request, name):
    template = loader.get_template("projecttime/index.html")
    context = {
        "project_time_list": ProjectTimeEntry.objects.filter(user__name=name)
    }
    return HttpResponse(template.render(context, request))

def add_entry(request):
    project = Project.objects.get(name=request.POST['project'])
    user = User.objects.get(name=request.POST['user'])
    entry = ProjectTimeEntry()
    entry.hour = int(request.POST['hour'])
    entry.date =  datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
    entry.project = project
    entry.user = user
    entry.save()
    return HttpResponse("entry1 added {}".format(request.POST))

def get_entries(request):
    entries = []
    for entry in ProjectTimeEntry.objects.filter(user__user_id=request.GET['user'],
                                                 date__gte=request.GET['from'],
                                                 date__lte=request.GET['to']):
        entry_struct = {'user': entry.user.name,
                        'project': entry.project.name,
                        'date': entry.date.isoformat(),
                        'hour': entry.hour}

        entries.append(entry_struct)

    data = json.dumps(entries)
    print(data)
    return HttpResponse(data)
    
@csrf_exempt
def submit_entries(request):
    entries=json.loads(request.body)
    
    # delete existing entries from given dates
    for entry in entries:
        print(entry["date"])
        ProjectTimeEntry.objects.filter(date=entry["date"]).delete()

    # add new entries
    for entry in entries:
        print(entry)
        e = ProjectTimeEntry()
        e.project = Project.objects.get(name=entry['project'])
        e.user = User.objects.get(user_id=entry['user'])
        e.date =  datetime.datetime.strptime(entry['date'], "%Y-%m-%d").date()
        if entry['hour'].strip() == '':
            e.hour = 0
        else:
            e.hour = int(entry['hour'])
        e.save()

    return HttpResponse("OK")

def example(request):
    return render(request, 'projecttime/test.html', {})


@csrf_exempt
def report(request):
    return HttpResponse("OK")


