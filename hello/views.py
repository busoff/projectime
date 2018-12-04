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

def index(request):
    context = {
        'user_list': User.objects.all()
    }
    return render(request, 'projecttime/index.html', context)

def projecttime(request, user_id):
    user = User.objects.get(user_id=user_id)

    # booststrap style
    return render(request, 'projecttime/report_table_bs.html', {'user_name':user.name, 'user_id':user.user_id})

def get_projects(request):
    projects = [project.name for project in Project.objects.all()]
    data = json.dumps(projects)
    print(data)
    return HttpResponse(data)

def get_entries(request):
    records = ProjectTimeEntry.objects.filter(user__user_id=request.GET['user'],
                                              date__gte=request.GET['from'],
                                              date__lte=request.GET['to'])

    entries = [{'user': r.user.name,
                'project': r.project.name,
                'date': r.date.isoformat(),
                'hour': r.hour} for r in records]
    
    data = json.dumps(entries)
    print(entries)
    return HttpResponse(data)
    
@csrf_exempt
def submit_entries(request):
    entries=json.loads(request.body)
    
    #FIXME: there is flaw that if the new entries are invalid, e.g, invalid project,
    # the existing entries will be removed and no entries added to datebase
    #
    # We should make sure  the existing entries are not deleted until all 
    # the new entries are valid to be added to database
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



#################
# Test function #
#################
def test(request):
    return render(request, 'projecttime/bootstrap.html', {})
