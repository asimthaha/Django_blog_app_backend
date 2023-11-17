from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from blogApp.models import *
from blogApp.serializer import *

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
        return HttpResponse(json.dumps({"status":"Blog App data Adding Unsuccessful"}))