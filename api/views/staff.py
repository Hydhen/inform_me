from django.http import JsonResponse
from django.core import serializers
from django.contrib.staticfiles.templatetags.staticfiles import static
import json
import os.path

from ..models import Domain, Role
from ..models import Staff as model_Staff

def Staff(request):
    queryset = model_Staff.objects.order_by('-role')
    staffs = []
    idx = 0
    image = "/images/profile/axolotl.jpg"
    for row in queryset:
        if os.path.isfile('./webapp/images/profile/' + row.login + '.jpg') == True :
            image = "/images/profile/" + row.login + ".jpg"
        staff = {
            'image': image,
            'first_name':row.first_name,
            'last_name': row.last_name,
            'status': 'true',
            'domain': row.domain.name,
            'role': row.role.name,
        }
        staffs.append(staff)
    return JsonResponse(staffs, safe=False)
