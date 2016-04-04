# coding: utf8
from django.http import JsonResponse
import glob, json

def Rules(request):
    array = None
    if request.method == 'GET':
        rules_root = '/data/development/inform_me/text/rules/'
        file_list = sorted(glob.glob(rules_root + '*.json'), key=str.lower)
        idx = 0
        array = {}
        for item in file_list :
            with open(item, 'r') as file :
                raw_data = file.read().decode('utf8')
            array[idx] = json.loads(raw_data)
            idx += 1

    return JsonResponse(array)
