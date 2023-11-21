from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from userApp.models import *
from userApp.serializer import *
from django.db.models import Q

# Create your views here.
@csrf_exempt
def registerView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        serializer_data = UserSerializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"User data Addded Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"User data Adding Unsuccessful"}))
        
@csrf_exempt
def displayUserView(request):
    if request.method =="POST":
        data= json.loads(request.body)
        getId = data['id']
        data = UserAddModel.objects.filter(Q(id__exact=getId)).values()
        data = list(data)
        return HttpResponse(json.dumps(data))
    
@csrf_exempt
def LoginView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        getEmail = data['email']
        getPassword = data['password']
        loginData = UserAddModel.objects.filter(Q(email__exact=getEmail) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
        