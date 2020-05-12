import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.core.paginator import Paginator
from mvc.forms import *
from utils.formatter import pageBar

# Create your views here.
PAGE_SIZE = 3

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
def getExamList(request, pageIndex):
    print("the pageIndex is {}".format(pageIndex))
    pageIndex = int(pageIndex)
    #_template = loader.get_template('examList.html')
    examList = Exam.objects.all().order_by('id')  #'-id'倒序
    _paginator = Paginator(examList, PAGE_SIZE)
    currentPage = _paginator.get_page(pageIndex)
    context = {
        'examList' :  currentPage,
        'request' :  request,
        'pagiator' :  _paginator,
        'has_pages' :  _paginator.num_pages > 1,
        'has_next' :  _paginator.page(pageIndex).has_next(),
        'has_prev' : _paginator.page(pageIndex).has_previous(),
        'page_index' : pageIndex,
        'page_next' : pageIndex + 1,
        'page_prev' : pageIndex - 1,
        'page_count' : _paginator.num_pages,
        'row_count' : _paginator.count,
        'page_nums' : range(_paginator.num_pages + 1)[1:],
    }
    #_output = _template.render(_context)
    #return HttpResponse(_output)
    #index_page(request, pageIndex)
    return render(request, "examList.html", context)


@csrf_exempt
def setPrintService(request):
     return HttpResponse("<h1>这里是准考证或通知书设置页面！</h1>")