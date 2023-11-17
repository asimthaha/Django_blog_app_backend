from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from userApp.models import *
from userApp.serializer import *
from django.db.models import Q

# Create your views here.
@csrf_exempt
def addView(request):
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
def displayView(request):
    if request.method =="POST":
        data = UserAddModel.objects.all()
        serializer_data = UserSerializer(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))