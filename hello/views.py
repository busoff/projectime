from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import ProjectTimeEntry, Project
from django.contrib.auth.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@login_required
def index(request):
    print("index {}".format(request.user.profile))

    if request.user.profile is None:
        raise Http404("invalid user login")

    return redirect("/projecttime/%s"%(request.user.profile.myid))

@login_required
def projecttime(request, user_id):
    user = User.objects.get(profile__myid=user_id)

    # booststrap style
    return render(request, 'projecttime/report_table_bs.html', {'user_name':user.username, 'user_id':user.profile.myid})

def get_projects(request):
    projects = [project.name for project in Project.objects.all()]
    data = json.dumps(projects)
    print(data) 
    return HttpResponse(data)

def get_entries(request):
    records = ProjectTimeEntry.objects.filter(user__profile__myid=request.GET['user'],
                                              date__gte=request.GET['from'],
                                              date__lte=request.GET['to'])

    entries = [{'user': r.user.username,
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
        e.user = User.objects.get(profile__myid=entry['user'])
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
