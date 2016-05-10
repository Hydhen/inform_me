from django.http import JsonResponse
import json

def Contact(request):
    print 'contact..'
    if request.method == 'GET':
        file_path = '/data/development/inform_me/text/contact.json'
        with open(file_path, 'r') as file :
            raw_data = file.read().decode('utf8')
        data = json.loads(raw_data)
    return JsonResponse(data, safe=False)
