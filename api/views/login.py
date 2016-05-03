from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        print('ok')
        print request
        param = json.loads(request.body)
        username = param['username'].decode('utf8')
        password = param['password'].decode('utf8')
        print username + ' ' + password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse("Logged in !", safe=False)
            else:
                return JsonResponse("Your account has been disabled", safe=False)
        else:
            return JsonResponse("Invalid login/password", safe=False)
    return JsonResponse("Permission denied", safe=False)

def IsLogged(request):
    if request.user.is_authenticated():
        return JsonResponse(request.user.username, safe=False)
    return JsonResponse('', safe=False)

def Logout(request):
    logout(request)
    return JsonResponse('', safe=False)
