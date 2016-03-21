#import pyexcel as pe
#import pyexcel.ext.xlsx

#records = pe.get_records(url="http://your.domain.com/path/to/your_file.xls")
#for record in records:
#    print("%s is aged at %d" % (record['Name'], record['Age']))

from django.shortcuts import render

def staff(request):
    return render(request, 'home/staff.html')
