from django.http import JsonResponse
from django.core import serializers
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth import authenticate
import json

from ..models import Status
from ..models import Project as model_Project

def Project(request):
    queryset = model_Project.objects.order_by('name')
    projects = []
    idx = 0
    for row in queryset:
        project = {
            'id': row.id,
            'name': row.name,
            'description_short': row.description_short,
            'leader': row.leader,
            'status': row.status.name,
        }
        projects.append(project)
    return JsonResponse(projects, safe=False)

def ProjectId(request, id):
    query = model_Project.objects.get(id=id)
    project = {
        'name': query.name,
        'description_short': query.description_short,
        'description': query.description,
        'leader': query.leader,
        'email': query.email,
        'logins': query.logins,
        'status': query.status.name,
        'updated': query.date_updated,
    }
    if request.user.is_authenticated():
        project['created'] = query.date_created
    return JsonResponse(project, safe=False)

def PresentProject(request):
    if request.method == 'GET':
        file_path = '/data/development/inform_me/text/present_project.json'
        with open(file_path, 'r') as file :
            raw_data = file.read().decode('utf8')
        flowchart = json.loads(raw_data)
        flowchart['image'] = '/images/flowchart/project_flowchart.png'
    return JsonResponse(flowchart, safe=False)
