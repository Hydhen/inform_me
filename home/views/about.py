# coding: utf8
from django.shortcuts import render
import glob, json

def about(request):
    about_root = '/data/development/inform_me/text/about/'
    file_list = sorted(glob.glob(about_root + '*.json'), key=str.lower)

    data = '['

    for item in file_list :
        with open(item, 'r') as file :
            raw_data = file.read().decode('utf8')
        data += raw_data.encode('utf8')
        data += ', '

    data += ']'

    return render(request, 'home/rules.html', {'json': data })
