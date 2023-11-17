from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from blogApp.models import *
from blogApp.serializer import *
from django.db.models import Q

# Create your views here.
@csrf_exempt
def addView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        serializer_data = BlogSerializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Blog App data Addded Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Blog App data Adding Unsuccessful"}))
    
@csrf_exempt
def searchView(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        getTitle = recieved_data['title']
        data = BlogAddModel.objects.filter(Q(title__icontains=getTitle)).values()
        searchData= list(data)
        return HttpResponse(json.dumps(searchData))
    

@csrf_exempt
def displayView(request):
    if request.method =="POST":
        data = BlogAddModel.objects.all()
        serializer_data = BlogSerializer(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))
    
@csrf_exempt
def displayMyView(request):
    if request.method == "POST":
        # recieved_data = json.loads(request.body)
        # getUserid = recieved_data["userid"]
        getUserid = 59
        data = BlogAddModel.objects.filter(Q(userid__icontains=getUserid)).values()
        myPost = list(data)
        return HttpResponse(json.dumps(myPost))