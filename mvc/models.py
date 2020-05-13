from django.db import models
from django.utils import timezone

# Create your models here.
class Exam(models.Model):  #考试模型类
    name = models.CharField('考试名称', max_length = 100)
    date = models.DateField('考试日期')
    siteName = models.CharField('考点名称', max_length = 100)
    adress = models.CharField('考点地址', max_length = 100)
    examineeNum = models.IntegerField('考生人数')
    examType = models.CharField('考试类别', max_length = 20)
    examMethod = models.CharField('考试方式', max_length = 20)
    remarks = models.TextField('备注', max_length = 500)

class Examinee(models.Model): #考生模型类
    name = models.CharField('考生姓名', max_length = 20)
    idNumber = models.CharField('身份证号', max_length = 18)
    examId = models.CharField('准考证号', max_length = 11)


class AdmissionTicket(models.Model): #笔试准考证模型
    theExam = models.ForeignKey(Exam, on_delete = models.CASCADE) #考试-准考证：一对多
    theExaminee = models.OneToOneField(Examinee, on_delete = models.CASCADE, primary_key = True)  #考生-准考证：一对一
    beginTime = models.DateTimeField("开始打印时间", auto_now = False, auto_now_add = False)
    endTime = models.DateTimeField("结束打印时间", auto_now = False, auto_now_add = False)
    ifQuery = models.BooleanField("是否已查询")
    ifPrint = models.BooleanField("是否已打印")
    

class InterviewNotification(models.Model): #面试通知书模型
    theExam = models.ForeignKey(Exam, on_delete = models.CASCADE) 
    theExaminee = models.OneToOneField(Examinee, on_delete = models.CASCADE, primary_key = True) 
    beginTime = models.DateTimeField("开始打印时间", auto_now = False, auto_now_add = False)
    endTime = models.DateTimeField("结束打印时间", auto_now = False, auto_now_add = False) 
    ifQuery = models.BooleanField("是否已查询")
    ifPrint = models.BooleanField("是否已打印")

class ExamSite(models.Model):  #考点模型类
    name = models.CharField('考点名称', max_length = 100)
    address = models.CharField('考点地址', max_length = 100)
    roomNum = models.IntegerField('考场数')
    roomMaxNum = models.IntegerField('最大考场数')
    chiefName = models.CharField('主考', max_length = 20)
    chiefPhone = models.CharField('主考联系方式', max_length = 11)
    directorName = models.CharField('考务负责人', max_length = 20)
    directorPhone = models.CharField('考务联系方式', max_length = 11)
    ifStandardized = models.BooleanField('是否标准化考场')
    remarks = models.TextField('备注', max_length = 500)

class ExamPerson(models.Model): #考务人员模型类
    name = models.CharField('姓名', max_length = 20)
    workUnit = models.CharField('工作单位', max_length = 100)
    post = models.CharField('工作职务', max_length = 30) 
    phone = models.CharField('联系方式', max_length = 11)
    role = models.CharField('考务岗位', max_length = 20)
    ifTemporary = models.BooleanField('是否临聘人员') 
    grade = models.IntegerField('评分')
    remarks = models.TextField('备注', max_length = 500)
    
class ExamStuff(models.Model): #考务材料模型类
    name = models.CharField('材料名称', max_length = 20)
    amount = models.IntegerField('数量')
    stuffType = models.CharField('类别', max_length = 20) #消耗品|非消耗品
    remarks = models.TextField('备注', max_length = 500)

class FileInfo(models.Model):
    examId = models.CharField('关联考试ID', max_length = 20, blank=True)
    name = models.CharField('文件名', max_length = 50)
    size = models.DecimalField("文件大小", max_digits = 10, decimal_places = 0)
    path = models.CharField("文件路径", max_length = 200)
    time = models.DateTimeField("上传时间", default = timezone.now())