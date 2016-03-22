# coding: utf8
from django.shortcuts import render
import glob, json

def rules(request):
    rules_root = '/data/development/inform_me/text/rules/'
    rules_list = glob.glob(rules_root + '*.json')

    data = '['

    for rule in rules_list :
        with open(rule, 'r') as file :
            raw_data = file.read().decode('utf8')
        data += raw_data.encode('utf8')
        data += ', '

    data += ']'

    return render(request, 'home/rules.html', {'json': data })
