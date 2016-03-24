#import pyexcel as pe
#import pyexcel.ext.xlsx

#records = pe.get_records(url="http://your.domain.com/path/to/your_file.xls")
#for record in records:
#    print("%s is aged at %d" % (record['Name'], record['Age']))

from django.shortcuts import render
from django.core import serializers
from django.contrib.staticfiles.templatetags.staticfiles import static
import json

from ..models import Domain, Role, Staff

def staff(request):
    queryset = Staff.objects.order_by('-role')
    list = []
    for row in queryset:
        list.append({
            'image': static('home/img/profile/' + row.login + ".jpg"),
            'first_name':row.first_name,
            'last_name': row.last_name,
            'status': 'false',
            'domain': row.domain.name,
            'role': row.role.name,
        })
        staffs = json.dumps(list)

    return render(request, 'home/staff.html', {'staffs': staffs})
