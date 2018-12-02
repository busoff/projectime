from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import User, ProjectTimeEntry, Project
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import logging

logger = logging.getLogger(__name__)


def user_list(request):
    context = {
        'user_list': User.objects.all()
    }
    return render(request, 'projecttime/users.html', context)

def get_projects(request):
    projects = [project.name for project in Project.objects.all()]
    data = json.dumps(projects)
    return HttpResponse(data)

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
    return HttpResponse(data)
    
@csrf_exempt
def submit_entries(request):
    entries=json.loads(request.body)
    
    # delete existing entries from given dates
    for entry in entries:
        ProjectTimeEntry.objects.filter(date=entry["date"]).delete()

    # add new entries
    for entry in entries:
        print(entry)
        e = ProjectTimeEntry()
        e.project = Project.objects.get(name=entry['project'])
        e.user = User.objects.get(user_id=entry['user'])
        e.date =  datetime.datetime.strptime(entry['date'], "%Y-%m-%d").date()

        hour = 0
        try:
            hour = int(entry['hour'])
        except ValueError:
            logger.error('invalid hour format')

        if hour > 0:
            e.hour = hour
            e.save()

    return HttpResponse("OK")

def projecttime(request, user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'projecttime/report_table.html', {'user_name':user.name, 'user_id':user.user_id})
