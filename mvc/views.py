import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from mvc.forms import *

# Create your views here.
def index(request):
    return HttpResponse("<h1>欢迎来到人事考试管理系统！</h1>")

def addExamResult(request):
    return HttpResponse("<h1>考试项目已成功保存！</h1>")

def addSiteResult(request):
    return HttpResponse("<h1>考点资源已成功保存！</h1>")

# Create your views here.
@csrf_exempt
def addExam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            exam.save()
            return HttpResponseRedirect(reverse('add-exam-result'))
    else:
        form = ExamForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #项目根路径
    return render(request, os.path.join(PROJECT_ROOT, 'mvc/templates', 'addExam.html'), {'form':form})  

@csrf_exempt
def addSite(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save()
            site.save()
            return HttpResponseRedirect(reverse('add-site-result'))
    else:
        form = SiteForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #项目根路径
    return render(request, os.path.join(PROJECT_ROOT, 'mvc/templates', 'addSite.html'), {'form':form})  

@csrf_exempt
def getExamList(request):
    _template = loader.get_template('examList.html')
    _exams = Exam.objects.order_by('-id')
    print(_exams)
    _context = {
        'exam' :  _exams,
    }
    _output = _template.render(_context)
    return HttpResponse(_output)