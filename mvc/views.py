import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("<h1>欢迎来到人事考试管理系统！</h1>")