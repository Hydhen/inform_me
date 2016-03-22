#import pyexcel as pe
#import pyexcel.ext.xlsx

#records = pe.get_records(url="http://your.domain.com/path/to/your_file.xls")
#for record in records:
#    print("%s is aged at %d" % (record['Name'], record['Age']))

from django.shortcuts import render
import json

def staff(request):
    user1 = dict()
    user1['FirstName'] = 'Loic'
    user1['LastName'] = 'Juillet'
    user1['Position'] = 'Manager'
    user1['Domain'] = 'Embedded'
    user1['Status'] = 'false'
    user1['Image'] = '/static/home/img/profile/RedPanda.jpg'
    user2 = dict()
    user2['FirstName'] = 'John'
    user2['LastName'] = 'Doe'
    user2['Position'] = 'Manager'
    user2['Domain'] = 'Virtuality'
    user2['Status'] = 'true'
    user2['Image'] = '/static/home/img/profile/Axolotl.jpg'
    users = list()
    users.append(user1)
    users.append(user2)
    users.append(user2)
    users.append(user1)
    users.append(user1)
    users.append(user2)
    users.append(user2)

    return render(request, 'home/staff.html', {'user1': user1, 'users': users})
