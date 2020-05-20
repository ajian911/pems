import os
from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.http import HttpResponseRedirect
from django.utils.http import urlquote
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.core.paginator import Paginator
from mvc.forms import *
from utils.dataUtil import excelImport2Db
from django.utils import timezone

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
    #print("the pageIndex is {}".format(pageIndex))
    if(pageIndex == ''):
        pageIndex = 1
    else:
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
def setPrintService(request, examId):
    currentExam = Exam.objects.get(id = examId)
    relatePT = printTemplate.objects.filter(exam_id = examId) #查询当前考试对应的打印模板
    if(relatePT.exists()):
        dic = {'beginTime' : relatePT[0].beginTime,'endTime' : relatePT[0].endTime, 'content': relatePT[0].content, 'state':relatePT[0].state, 'loginURL':relatePT[0].loginURL }
        ptForm = PTForm(dic) 
    else:  #相对应的打印模板还未保存
        basePT = printTemplate.objects.filter(printType = currentExam.examType, ifBase = '1')
        dic = {'beginTime' : basePT[0].beginTime,'endTime' : basePT[0].endTime, 'content': basePT[0].content }
        ptForm = PTForm(dic)   
    #print("The currentExam name is {}".format(currentExam.name))
    #最近上传的导入数据文件
    fileInfoList = FileInfo.objects.filter(examId = examId).order_by('-time')
    #print("The last upload file name is {}".format(lastFileInfo[0].name))
    if(len(fileInfoList) > 0):
        lastFile = fileInfoList[0]
    else:
        lastFile = 'none'
    context = {
        'currentExam' :  currentExam,
        'lastFile' : lastFile,
        'ptForm' : ptForm,
    }
    return render(request, "printService.html", context)

@csrf_exempt
def upload(request, examId):
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #项目根路径
    currentExam = Exam.objects.get(id = examId)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for eachFile in files:
                fileInfo = FileInfo(examId = examId, name = eachFile.name, size = 1 if 0 < eachFile.size < 1024 else eachFile.size / 1024, path = os.path.join(PROJECT_ROOT, 'upload'))
                fileInfo.save()
                destination = open(os.path.join(os.path.join(PROJECT_ROOT, 'upload/'), eachFile.name), 'wb+')
                for chunk in eachFile.chunks():
                    destination.write(chunk)
                    destination.close()
                excelImport2Db(os.path.join(os.path.join(PROJECT_ROOT, 'upload/'), eachFile.name), examId)#excel文件数据导入pems-db
    #return HttpResponse("<h1>文件导入成功</h1>") #应返回打印设置页面
    #return redirect('http://127.0.0.1:8000/mvc/setPrintService/1/') 
    currentExam = Exam.objects.get(id = examId) 
    fileInfoList = FileInfo.objects.filter(examId = examId).order_by('-time')
    if(len(fileInfoList) > 0):
        lastFile = fileInfoList[0]
    else:
        lastFile = 'none'
    context = {
        'currentExam' :  currentExam,
        'lastFile' : lastFile,
    }
    return render(request, "printService.html", context)

@csrf_exempt
def download(request, fileId):
    fileInfo = FileInfo.objects.get(id = fileId)    
    filePath = os.path.join(fileInfo.path, fileInfo.name)   
    file = open(filePath, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(fileInfo.name)
    return response  

@csrf_exempt
def savePrintTemplate(request, examId):
    currentExam = Exam.objects.get(id = examId)
    if request.method == 'POST':
        #ptForm = PTForm(request.POST)
        #print("the endTime is {}".format(request.POST))
        #print("the endTime is {}".format(request.POST['endTime']))
        #if ptForm.is_valid():
        if(request.POST['state'] == 'on'):
            currentState = 1
        else:
            currentState = 0
        relatePT = printTemplate.objects.filter(exam_id = examId) #查询当前考试对应的打印模板
        if(relatePT.exists()): 
            relatePT[0].beginTime = request.POST['beginTime']
            relatePT[0].endime = request.POST['endTime']
            relatePT[0].content = request.POST['content'] 
            relatePT[0].state = request.POST['state']
            relatePT[0].loginURL = request.POST['loginURL']
            relatePT[0].save()
        else:
            PT = printTemplate(exam_id = examId,
                           printType = currentExam.examType,
                           beginTime = request.POST['beginTime'], 
                           endTime = request.POST['endTime'], 
                           content = request.POST['content'], 
                           state = currentState,
                           loginURL = "http://127.0.0.1/printLogin/" + examId + "/"
                           )                  
            PT.save()
        return HttpResponseRedirect(reverse('add-site-result'))